# 1) Challenge 1 - Who Have Published What At Where?
DROP TABLE IF EXISTS autitpub;

CREATE TEMPORARY TABLE autitpub
(SELECT 
	tb_au.au_id AS au_id,
	tb_au.au_lname AS aln,
	tb_au.au_fname AS afn,
	tit_titau.TITLE AS tit,
	tit_titau.pub_id AS pub_id,
	tit_titau.tit_id AS tit_id
	
	FROM authors AS tb_au

	INNER JOIN 
		(SELECT tit.title as TITLE,
			tit.title_id AS tit_id,
			tb_tiau.au_id as au_id,
		       	tit.pub_id AS pub_id
		       	FROM titles as tit
			INNER JOIN titleauthor as tb_tiau
	       		ON tit.title_id = tb_tiau.title_id) 
		AS tit_titau

	ON tb_au.au_id = tit_titau.au_id);


#SELECT	autitpub.au_id AS `AUTHOR ID`, 
#	autitpub.aln AS `LAST NAME`, 
#	autitpub.afn AS  `FIRST NAME`,
#	autitpub.tit AS TITLE,
#	pub.pub_name AS PUBLISHER 
#
#	FROM publishers AS pub 
#	INNER JOIN autitpub
# 	ON pub.pub_id = autitpub.pub_id;
#
# 2) Who Have Published How Many At Where?

DROP TABLE IF EXISTS basic_data;

CREATE TEMPORARY TABLE basic_data (
	SELECT	autitpub.au_id AS au_id, 
	autitpub.aln AS aln, 
	autitpub.afn AS  afn,
	autitpub.tit AS TITLE,
	autitpub.tit_id AS tit_id,
	pub.pub_name AS PUBLISHER 

	FROM publishers AS pub 
	INNER JOIN autitpub
 	ON pub.pub_id = autitpub.pub_id);

SELECT bd.au_id AS `AUTHOR ID`,
	bd.aln AS `LAST NAME`,
	bd.afn AS `FIRST NAME`,
	bd.PUBLISHER AS PUBLISHER,
	count(bd.TITLE) AS `TITLE COUNT`
	FROM basic_data as bd
	GROUP BY `AUTHOR ID`, `LAST NAME`, `FIRST NAME`, PUBLISHER;

# 3)  Best Selling Authors

SELECT bd.au_id AS `AUTHOR ID`,
	bd.aln AS `LAST NAME`,
	bd.afn AS `FIRST NAME`,
	sum(venta.ventas) AS TOTAL
	FROM basic_data AS bd
	INNER JOIN (
		SELECT tit.title as title,
			tit.title_id as tit_id,
			sum(sales.qty) AS ventas
			FROM titles as tit 
			INNER JOIN sales 
			ON tit.title_id = sales.title_id
			GROUP BY tit.title
	) AS venta
	ON bd.tit_id = venta.tit_id
	GROUP BY `AUTHOR ID`,`LAST NAME`,`FIRST NAME`
	ORDER BY TOTAL DESC LIMIT 3;

# 4) Best Selling Authors Ranking

DROP TABLE IF EXISTS autitpub2;

CREATE TEMPORARY TABLE autitpub2
(SELECT 
	tb_au.au_id AS au_id,
	tb_au.au_lname AS aln,
	tb_au.au_fname AS afn,
	tit_titau.TITLE AS tit,
	tit_titau.pub_id AS pub_id,
	tit_titau.tit_id AS tit_id
	
	FROM authors AS tb_au

	LEFT JOIN 
		(SELECT tit.title as TITLE,
			tit.title_id AS tit_id,
			tb_tiau.au_id as au_id,
		       	tit.pub_id AS pub_id
		       	FROM titles as tit
			LEFT JOIN titleauthor as tb_tiau
	       		ON tit.title_id = tb_tiau.title_id) 
		AS tit_titau

	ON tb_au.au_id = tit_titau.au_id);


DROP TABLE IF EXISTS basic_data2;

CREATE TEMPORARY TABLE basic_data2 (
	SELECT	autitpub2.au_id AS au_id, 
	autitpub2.aln AS aln, 
	autitpub2.afn AS  afn,
	autitpub2.tit AS TITLE,
	autitpub2.tit_id AS tit_id,
	pub.pub_name AS PUBLISHER 

	FROM publishers AS pub 
	RIGHT JOIN autitpub2
 	ON pub.pub_id = autitpub2.pub_id);


SELECT bd.au_id AS `AUTHOR ID`,
	bd.aln AS `LAST NAME`,
	bd.afn AS `FIRST NAME`,
	if(sum(venta.ventas) is null,0, sum(venta.ventas) ) AS TOTAL
	FROM basic_data2 AS bd
	LEFT JOIN (
		SELECT tit.title as title,
			tit.title_id as tit_id,
			sum(sales.qty) AS ventas
			FROM titles as tit 
			LEFT JOIN sales 
			ON tit.title_id = sales.title_id
			GROUP BY tit.title
	) AS venta
	ON bd.tit_id = venta.tit_id
	GROUP BY `AUTHOR ID`,`LAST NAME`,`FIRST NAME`
	ORDER BY TOTAL DESC LIMIT 23;

# BONUS : Most Profiting Authors

DROP TABLE IF EXISTS beneficios;
CREATE TEMPORARY TABLE beneficios (
	SELECT 	tit_au.au_id AS au_id,
	       	sum(tit.advance*(tit_au.royaltyper/100)) as advance,
	       	sum(sales.qty*tit.price*(tit.royalty/100)*(tit_au.royaltyper/100)) as royalty
       		FROM titleauthor as tit_au
		LEFT JOIN titles as tit
		ON tit_au.title_id = tit.title_id
		LEFT JOIN sales
		ON tit_au.title_id = sales.title_id
		GROUP BY tit_au.au_id
		);

SELECT 
	authors.au_id AS `AUTHOR ID`,
	authors.au_lname AS `LAST NAME`,
        authors.au_fname AS `FIRST NAME`,
	IF( sum( tit_prof.royalty + tit_prof.advance ) IS NULL
		,0,
		sum( tit_prof.royalty + tit_prof.advance )) AS PROFIT

	FROM authors
	LEFT JOIN beneficios AS tit_prof
	ON authors.au_id = tit_prof.au_id
	GROUP BY `AUTHOR ID`,`LAST NAME`, `FIRST NAME`
	ORDER BY PROFIT DESC LIMIT 3;

