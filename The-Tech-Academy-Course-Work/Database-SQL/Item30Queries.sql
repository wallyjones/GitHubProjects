/*#1 Query for finding Lost Tribe at Sharpstown*/

select Title, BranchName, No_of_Copies
from Book as b inner join Book_Copies as BC
	on b.Book_ID = bc.Book_ID 
		inner join Library_Branch as LB
	on BC.BranchID = LB.BranchID
where title = 'The Lost Tribe'
	and BranchName = 'Sharpstown'

/*#2 Query for finding copies of Lost Tribe at each Library*/

select Title, BranchName, No_of_Copies
from Book as b inner join Book_Copies as BC
	on b.Book_ID = bc.Book_ID 
		inner join Library_Branch as LB
	on BC.BranchID = LB.BranchID
where title = 'The Lost Tribe'

/*#3 Query for retrieving names of borrowers with no books borrowed*/

select name
from Borrower as BO left join Book_Loans as BL
	on BO.CardNO = BL.CardNO
where bl.DueDate is null

/*4 Books loaned from Sharpstown, due date today, retrieve title, borrowers name and address*/

select bl.DueDate, Name, b.title, bo.[Address]
from Library_Branch as LB inner join Book_Loans as BL
	on LB.BranchID = BL.BranchID
		Inner Join Borrower as BO 
	on BL.CardNO = BO.CardNO
		Inner Join Book as B
	on BL.Book_ID = b.Book_ID
where BL.DueDate = cast(getdate() as date)

/*#5 For each Library, retrieve branch and total books loaned*/

select count(lb.BranchID) as [Count], lb.BranchName
from Book_Loans as BL left join Library_Branch as LB
	on bl.BranchID = lb.BranchID 
Group By lb.BranchName

/*#6 Retrieve names, addresses, # of books checked out for the borrowers with more than 5*/

select count(bl.CardNO) as TotalBooks, Bo.Name, bo.[Address]
from Borrower as Bo inner join Book_Loans as BL
	on bo.CardNO = BL.CardNO
group by bo.Name, bo.[Address]
having count(bl.CardNO) >= 5

/*#7 Retrieve title of Stephen King book, and # of copies owned by Central*/

select count(lb.BranchName) as [BookCount], lb.BranchName, b.Title
from Book as B inner join Book_Authors as BA
	on b.Book_ID = ba.Book_ID
		inner join Book_Loans as BL
	on  b.Book_ID = BL.Book_ID
		inner join Library_Branch as LB
	on BL.BranchID = LB.BranchID
Where Ba.AuthorName = 'Stephen King'
	and lb.BranchName = 'Central'
Group By lb.BranchName, b.Title

/*Stored Procedure for One or more of the above queries*/


Create Procedure SearchBookAuthor @Author varchar(30) = NULL
AS
select count(lb.BranchName) as [BookCount], lb.BranchName, b.Title, ba.AuthorName
from Book as B inner join Book_Authors as BA
	on b.Book_ID = ba.Book_ID
		inner join Book_Loans as BL
	on  b.Book_ID = BL.Book_ID
		inner join Library_Branch as LB
	on BL.BranchID = LB.BranchID
Where Ba.AuthorName like '%' + @Author + '%'
Group By lb.BranchName, b.Title, ba.AuthorName