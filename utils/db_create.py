import sqlite3

con=sqlite3.connect("sentiment.db")
cur = con.cursor()

cur.execute("CREATE TABLE sentences(sentence TEXT, score INTERGER, sentiment TEXT)")

#create word list table
cur.execute("Create table words(word TEXT, SCORE int, is_avilable_in_dict BOOLEAN)")

#create analysis table

cur.execute("" \
"           Create table analysis(" \
"               total_sentences INT," \
                "total_paragraph INT," \
                "total_score INT," \
                "total_words INT," \
                "total_negative_words INT," \
                "total_postive_words INT," \
                "total_dict_hits INT," \
                "total_dict_miss INT," \
                "total_positive_sentences INT," \
                "total_negative_sentences INT)"
            )




con.commit()
con.close()