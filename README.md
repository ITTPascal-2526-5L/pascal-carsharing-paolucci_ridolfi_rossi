[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/5Frp0vjT)


(venv) C:\Users\nicolo.ridolfi\Desktop\carsharing\pascal-carsharing-paolucci_ridolfi_rossi>flask db migrate -m "posts"
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'posts'
Generating C:\Users\nicolo.ridolfi\Desktop\carsharing\pascal-carsharing-paolucci_ridolfi_rossi\migrations\versions\875b3de0c0df_posts.py ...  done

(venv) C:\Users\nicolo.ridolfi\Desktop\carsharing\pascal-carsharing-paolucci_ridolfi_rossi>flask db upgrade
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade 94961ba8ba5a -> 875b3de0c0df, posts