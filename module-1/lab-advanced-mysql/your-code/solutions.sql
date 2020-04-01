###### Challenge 1 

# Step 1

CREATE TABLE paso1 (SELECT  ord_num, 
	tit_au.au_id,
	tit_au.title_id,
	(tit_au.price * sales.qty * tit_au.royalty / 100 * tit_au.royaltyper / 100) AS sales_royalty 
	FROM sales
	RIGHT JOIN ( 
		SELECT 
			titleauthor.royaltyper AS royaltyper, 			
			titleauthor.au_id AS au_id, 
			titles.title_id	AS title_id,
			titles.royalty AS royalty,
			titles.price as price
		FROM titles
		RIGHT JOIN titleauthor
		ON titles.title_id = titleauthor.title_id
	) AS tit_au
	ON sales.title_id = tit_au.title_id);

# step 2

SELECT title_id AS `Title ID`, au_id AS `AUTHOR ID`, 
	sum(if(sales_royalty is not null,sales_royalty,0)) AS Aggregate_royalties 
	FROM paso1
	GROUP BY title_id, au_id;

# step 3
SELECT `AUTHOR ID`, sum(Aggregate_royalties) AS Profits
	FROM (
		SELECT title_id AS `Title ID`, au_id AS `AUTHOR ID`, 
			sum(if(sales_royalty is not null,sales_royalty,0)) AS Aggregate_royalties 
			FROM paso1
			GROUP BY title_id, au_id
	    ) AS paso_2
	GROUP BY `AUTHOR ID`
	ORDER BY Profits DESC LIMIT 3;

###### Challenge 2 -> I used create temporary tables in the first step the derivated tables, here I am going to change the order

# setp 1 setp 2 y step 3
 SELECT `AUTHOR ID` AS au_id, sum(Aggregate_royalties) AS profits
	FROM (
	SELECT title_id AS `Title ID`, au_id AS `AUTHOR ID`, 
		sum(if(sales_royalty is not null,sales_royalty,0)) AS Aggregate_royalties 
			FROM (	SELECT  
			ord_num, 
			tit_au.au_id,
			tit_au.title_id,
			(tit_au.price * sales.qty * tit_au.royalty / 100 * tit_au.royaltyper / 100) AS sales_royalty 
			FROM sales
			RIGHT JOIN ( 
				SELECT 
					titleauthor.royaltyper AS royaltyper, 			
					titleauthor.au_id AS au_id, 
					titles.title_id	AS title_id,
					titles.royalty AS royalty,
					titles.price as price
				FROM titles
				RIGHT JOIN titleauthor
				ON titles.title_id = titleauthor.title_id
			) AS tit_au
			ON sales.title_id = tit_au.title_id
			) as step_1
		GROUP BY title_id, au_id
	    ) AS paso_2
	GROUP BY `AUTHOR ID`
	ORDER BY Profits DESC LIMIT 3;

# Challenge 3 -> 

CREATE TABLE most_profiting_authors (
	SELECT `AUTHOR ID`, sum(Aggregate_royalties) AS Profits
	FROM (
	SELECT title_id AS `Title ID`, au_id AS `AUTHOR ID`, 
		sum(if(sales_royalty is not null,sales_royalty,0)) AS Aggregate_royalties 
			FROM (	SELECT  
			ord_num, 
			tit_au.au_id,
			tit_au.title_id,
			(tit_au.price * sales.qty * tit_au.royalty / 100 * tit_au.royaltyper / 100) AS sales_royalty 
			FROM sales
			RIGHT JOIN ( 
				SELECT 
					titleauthor.royaltyper AS royaltyper, 			
					titleauthor.au_id AS au_id, 
					titles.title_id	AS title_id,
					titles.royalty AS royalty,
					titles.price as price
				FROM titles
				RIGHT JOIN titleauthor
				ON titles.title_id = titleauthor.title_id
			) AS tit_au
			ON sales.title_id = tit_au.title_id
			) as step_1
		GROUP BY title_id, au_id
	    ) AS paso_2
	GROUP BY `AUTHOR ID`
	ORDER BY Profits DESC LIMIT 3);

