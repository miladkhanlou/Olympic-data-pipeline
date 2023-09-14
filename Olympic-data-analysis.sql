-- counting number of atheletes from each country
SELECT NOC, count (*) as totalAlthlete
FROM athletes 
GROUP BY NOC
ORDER by totalAlthlete desc 

-- calculate total number of medals won each country
SELECT Team_NOC, sum(Gold) as total_golds, sum(Silver) as total_silvers, sum(Bronze) as total_Bronzes 
FROM medals
group by Team_NOC
ORDER BY total_golds DESC;

-- calculate Average number of entries by gender for each discipline:
select Discipline, avg(Female) as average_females, avg(Male) as average_males, avg(Total) as average_participants
FROM entriesgender
GROUP BY Discipline
ORDER BY average_participants DESC
