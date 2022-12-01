from pdf import extract

extract("Advanced-Engineering-Mathematics", 
  list(map(lambda x: (x[0]+26, x[1]+26), [
    (203,237),
    (473,491),
    (495,498),
    (510,517),
    (522,533),
    (540,556),
    (558,574)
  ]))
)
