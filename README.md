# פרוייקט מסכם
הפרוייקט בנוי ממודולים העובדים יחד.
1. search_frontend.py

עבור כל פונקציות אחזור שהתבקשנו לממש קיים מודול המממש את הפונקציה.

3. search_backend.py
4. search_title.py
5. search_body.py
6. get_pageviews_backend.py
7. get_page_rank_backend.py

בנוסף קיימים מודולים לעזר.

7. imports.py - ייבוא ספריות
9. dicts_and_indexes.py - קורא אינדקסים ומילונים
10. query_preprossesing.py - עיבוד שאילתות

מילונים.

10. Dl_body.pkl
11. dl_title.pkl
12. id_title_dict.pkl - ממפה מסמך לכותרת שלו
13. pagerank.csv - ממפה מסמך לציון
14. pageviews-202108-user.pkl - ממפה מסמך למספר הצפיות

בנוסף העלנו את המחברת של הניסויים שערכנו:

15.Expiraments.ipynb


יצירת אינדקסים ואובייקטים בGCP

16.	Index_body_and_title.ipynb. -  הקובץ שיוצר את האינדקס לגוף ולכותרת המסמכים
17.	PageRank.ipynb       -   סקיפט ליצירת   pr
18.	Index_anc_creation.ipynb. – סקריפט ליצירת אינדקס לanc 

מחלקות האינדקסים

19.	 Inverted_anc2.py. -  קלאס ליצירת אינדקס לanc
20.	Inverted_title.py. אינדקס ליצירת ה כותרת
21.	Inverted_index_gcp.  -      קובץ ליצירת האינדקס לגוף הטקסט
