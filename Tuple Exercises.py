record = [("Textbook ID", "Course(s)", "# Books", "Price Per Book", "Publisher ID"),
          ("TEXT-0001", "Basic Anatomy and Physiology", "BIO-100", "400", "$94.00", "PUB-1003"),
          ("TEXT-0002", "Chemistry for Biology Students", "BIO-101-102", "400", "105.30", "PUB-1002"),
          ("TEXT-0003", "Anatomy and Physiology", "BIO-141-142", "330", "$159.75", "PUB-1003")]

r = 0
rcd = []
while r < len(record):
    rcd.append(record[r][1])
    rcd.append(record[r][4])
    r += 1
    print rcd
    rcd = []


data = [("Publisher ID", "Publisher Name", "Address", "City", "State", "Zip", "Phone Number"),
        ("PUB-1001", "Science Books Galore", "525 Allen St", "Trenton", "NJ", "08620", "(609)555-2554"),
        ("PUB-1002", "Books for Chemistry Students Ltd", "142 N SPring St", "Los Angeles", "CA", "90012", "(213)555-8362"),
        ("PUB-1003", "Carliz Publishers Corp", "24 King Ave", "Columbus", "OH", "43201", "(614)555-3322")]

d = 0
da = []
while d < len(data):
    da.append(data[d][1])
    da.append(data[d][6])
    d += 1
    print da
    da = []
