# 1) Challenge 1 - Who Have Published What At Where?

SELECT 
	tb_au.au_id as `AUTHOR ID`,
	tb_au.au_lname as `LAST NAME`,
	tb_au.au_fname as `FIRST NAME`,

	
	FROM 
	authors as tb_au
	INNER JOINT 
	titleauthor as tb_ti_au
        ON tb_au.au_id=tb_ti_au.au_id


