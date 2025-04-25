/*1*/
SELECT MAX(budget) FROM DEPARTMENT;
/*2*/
SELECT TEACHER.TP_NAME, TEACHER.SALARY FROM TEACHER WHERE SALARY > (SELECT AVG(SALARY) FROM TEACHER);
/*3*/
SELECT TEACHER.TP_ID AS Teacher_ID,STUDENT.TP_ID AS Student_ID, COUNT(*) AS Nb_cours_pris 
    FROM STUDENT, TAKES,SECTION,TEACHES,TEACHER 
    WHERE STUDENT.TP_ID = TAKES.TP_ID AND  TAKES.SEC_ID = SECTION.SEC_ID AND SECTION.SEC_ID = TEACHES.SEC_ID AND TEACHES.TP_ID = TEACHER.TP_ID
    GROUP BY TEACHER.TP_ID,STUDENT.TP_ID
    HAVING COUNT(TEACHER.TP_ID)>=2;

/*4*/
SELECT T.teachername, T.studentname, T.totalcount
FROM (
    SELECT teacher.tp_name   AS teachername, student.tp_name AS studentname,COUNT(*) AS totalcount
    FROM  teacher,student, takes, teaches
    WHERE 
        teacher.tp_id     = teaches.tp_id
      AND student.tp_id     = takes.tp_id
      AND takes.course_id    = teaches.course_id
      AND takes.sec_id       = teaches.sec_id
      AND takes.semester     = teaches.semester
      AND takes.tp_year      = teaches.tp_year
    GROUP BY 
        teacher.tp_name,
        student.tp_name
) T
WHERE T.totalcount >= 2
ORDER BY T.teachername;


/*5*/
SELECT STUDENT.TP_ID, STUDENT.TP_NAME
    FROM STUDENT
    WHERE STUDENT.TP_ID NOT IN 
    (
        SELECT STUDENT.TP_ID 
        FROM STUDENT, TAKES 
        WHERE STUDENT.TP_ID = TAKES.TP_ID 
            AND TAKES.TP_YEAR <=2010
    );
/*6*/
SELECT TEACHER.* 
    FROM TEACHER
    WHERE TEACHER.TP_NAME LIKE 'E%';

/*7*/
SELECT TP_NAME, SALARY FROM TEACHER ORDER BY SALARY DESC FETCH FIRST 4 ROWS ONLY; 
/*8*/
 SELECT TP_NAME, SALARY FROM TEACHER ORDER BY SALARY ASC FETCH FIRST 3 ROWS ONLY;
/*9*/
SELECT STUDENT.TP_ID, STUDENT.TP_NAME
    FROM STUDENT
    WHERE STUDENT.TP_ID IN
    (
        SELECT STUDENT.TP_ID FROM STUDENT, TAKES WHERE STUDENT.TP_ID = TAKES.TP_ID 
        AND TAKES.TP_YEAR = 2009 
        AND TAKES.SEMESTER = 'Fall'
    );
/*10*/
SELECT s.tp_id, s.tp_name
FROM   student s
WHERE  s.tp_id = SOME 
(
    SELECT t.tp_id
    FROM   takes t
    WHERE  t.tp_year  = 2009
      AND  t.semester = 'Fall'
);


/*11*/
SELECT s.tp_id, s.tp_name
FROM   student s
JOIN  (
          SELECT DISTINCT tp_id
          FROM   takes
          WHERE  tp_year = 2009
            AND    semester = 'Fall'
      ) t
ON    s.tp_id = t.tp_id;

/*12*/
SELECT STUDENT.TP_ID, STUDENT.TP_NAME
    FROM STUDENT
    WHERE EXISTS
    (
        SELECT STUDENT.TP_ID FROM STUDENT, TAKES WHERE STUDENT.TP_ID = TAKES.TP_ID 
        AND TAKES.TP_YEAR = 2009 
        AND TAKES.SEMESTER = 'Fall'
    );
/*13*/
SELECT A.tp_name,
       B.tp_name
FROM (
    SELECT * 
    FROM student 
    INNER JOIN takes USING (tp_id)
) A,
(
    SELECT * 
    FROM student 
    INNER JOIN takes USING (tp_id)
) B
WHERE A.course_id = B.course_id
  AND A.sec_id     = B.sec_id
  AND A.semester   = B.semester
  AND A.tp_year    = B.tp_year
  AND A.tp_id     <> B.tp_id
  AND A.tp_name   <  B.tp_name
GROUP BY A.tp_name,
         B.tp_name
HAVING COUNT(*) >= 1
ORDER BY A.tp_name,
         B.tp_name;


/*14*/
SELECT teacher.tp_name , count (*)
FROM ( takes INNER JOIN teaches 
    USING ( course_id , sec_id , semester , tp_year ) )
INNER JOIN teacher ON teaches.tp_id = teacher.tp_id
GROUP BY teacher.tp_name , teacher.tp_id 
ORDER BY count (*) DESC ;

/*15*/
SELECT teacher.tp_name , count ( course_id )
FROM ( takes INNER JOIN teaches USING ( course_id , sec_id , semester , tp_year ) )
RIGHT OUTER JOIN teacher ON teaches.tp_id = teacher.tp_id
GROUP BY teacher.tp_name , teacher.tp_id ORDER BY count ( course_id ) DESC ;

/*16*/
WITH mytakes ( tp_id , course_id , sec_id , semester , tp_year , grade ) AS 
( 
    SELECT tp_id ,
    course_id , sec_id , semester , tp_year , grade
    FROM takes
    WHERE grade = 'A' 
)
SELECT teacher.tp_name , count ( course_id )
FROM ( mytakes INNER JOIN teaches USING ( course_id , sec_id , semester , tp_year ) )
RIGHT OUTER JOIN teacher ON teaches.tp_id = teacher.tp_id
GROUP BY teacher.tp_name , teacher.tp_id ORDER BY count ( course_id ) DESC ;
/*17*/
SELECT teacher.tp_name , student.tp_name , count (*) FROM ( teacher NATURAL JOIN teaches )
INNER JOIN
( takes NATURAL JOIN student ) USING
( course_id , sec_id , semester ,tp_year ) 
GROUP BY teacher.tp_name , student.tp_name ;

/*18*/

SELECT m.tn, m.sn
FROM (
    SELECT teacher.tp_name   AS tn,
           student.tp_name   AS sn,
           COUNT(*)          AS tc
    FROM   
    (teacher NATURAL JOIN teaches)
    INNER JOIN 
    (takes NATURAL JOIN student)
    USING (course_id, sec_id, semester, tp_year)
    GROUP  BY teacher.tp_name,
              student.tp_name
) m
WHERE m.tc >= 2
ORDER BY m.tn, m.sn;
