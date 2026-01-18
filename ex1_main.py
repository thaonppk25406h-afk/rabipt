from ex1_func import *
# import codecs
import re

print("++++++++++++++++++++++++++MENU++++++++++++++++++++++++++")
print("1. Ghi DL - C1")
print("2. Ghi DL - C2")
print("3. Đọc DL - C1")
print("4. Đọc DL - C2")
print("5. In ra số từ có tần suất xuất hiện nhiều nhất.")
print("0. Thoát chương trình.")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

while True:
    c = int(input("Chọn chức năng thực hiện: "))
    if c in [1,2]:
        content = re.sub(r"\\+n", "\n", input("Hãy nhập vào nội dung bạn muốn truyền: "))
        mode = input("Nhập chế độ (w: ghi đè, a: ghi nối): ")
        if c == 1:
            # content = codecs.decode(input("Hãy nhập vào nội dung bạn muốn truyền: "), "unicode_escape")
            ghiDL_1("data/test1.txt",mode,content)
        else:
            ghiDL_2("data/test2.txt", mode, content)
    elif c in [3,4,5]:
        path = input("Nhập đường dẫn của file bạn muốn mở: ")
        if c == 3:
            docDL_1(path)
        elif c == 4:
            docDL_2(path)
        else:
            keyMax, valueMax = tanSuatMax(path)
            print(f"Từ có tần suất xuất hiện nhiều nhất là: ",end='')
            for i in keyMax:
                print(i,end=', ')
            print(f"xuất hiện {valueMax} lần.")
    else:
        print("Tạm biệt!")
        break