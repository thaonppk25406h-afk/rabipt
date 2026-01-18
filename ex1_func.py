def ghiDL_1(path, mode, content):
    f = open(path, mode, encoding = "utf-8")
    f.write(content)
    f.close()

def ghiDL_2(path, mode, content):
    with open(path, mode, encoding = "utf-8") as f:
        f.write(content)

def docDL_1(path):
    f = open(path, 'r', encoding = "utf-8")
    for line in f:
        print(line.strip())
    f.close()

def docDL_2(path):
    with open(path, 'r', encoding = "utf-8") as f:
        print(f.read())

# Viết hàm đọc dữ liệu từ tệp tin và cho biết từ có tần suất xuất hiện nhiều nhất
def tanSuatMax(path):
    with open(path, 'r', encoding = "utf-8") as f:
        s = f.read()
        l = s.split()
        new_l = []

        for i in l:
            new_i = ""
            for j in i:
                if j.isalnum():
                    new_i += j
            if new_i:
                new_l.append(new_i)

        dict = {}
        for i in new_l:
            dict[i] = dict.get(i,0)+1

        valueMax = max(dict.values())
        keyMax = []
        for key, value in dict.items():
            if value == valueMax:
                keyMax.append(key)
        return (keyMax, valueMax)



