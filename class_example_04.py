#!/usr/local/bin/python3.7
import re
import sys

BookVal = {
 '1' : {
 	'title' : 'Sach khoa hoc tap 1',
 	'price' : '20,000',
 	'quantity' : '5',
 	'published' : '1/1/2020',
	'location_zone' : {
		1 : 2,
		2 : 3,
		3 : 1
	}
  },
  '2' : {
 	'title' : 'Sach khoa hoc tap 2',
 	'price' : '30,000',
 	'quantity' : '5',
 	'published' : '1/1/2020',
 	'location_zone' : {
		1 : 5,
		2 : 0,
		3 : 2
	}
  },
  '3' : {
 	'title' : 'Sach khoa hoc tap 3',
 	'price' : '25,000',
 	'quantity' : '5',
 	'published' : '1/3/2020',
 	'location_zone' : {
		1 : 1,
		2 : 1,
		3 : 3
	}
  },
  '4' : {
 	'title' : 'Sach khoa hoc tap 4',
 	'price' : '25,000',
 	'quantity' : '5',
 	'published' : '1/12/2020',
 	'location_zone' : {
		1 : 2,
		2 : 2,
		3 : 1
	}
  },
  '5' : {
 	'title' : 'Sach khoa hoc tap 5',
 	'price' : '22,000',
 	'quantity' : '11',
 	'published' : '1/12/2020',
 	'location_zone' : {
		1 : 2,
		2 : 6,
		3 : 3
	}
  },
 '6' : {
 	'title' : 'Sach khoa hoc tap 6',
 	'price' : '25,500',
 	'quantity' : '10',
 	'published' : '1/12/2020',
 	'location_zone' : {
		1 : 3,
		2 : 2,
		3 : 5
	}
  }
}
locationZone = {
  1 :  {   'title' : 'Hà Nội'  },
  2 :  {   'title' : 'Hồ Chí Minh'  },	
  3 :  {   'title' : 'Cà Mau'  }
}


class liet_ke_sach_tinh_thanh: 
    def ds_tinh_thanh(self):
        for key_zone in locationZone:
            print("%s.%s" % (key_zone, locationZone[key_zone]["title"]))

class liet_ke_sach_trong_kho:
    def ds_sach(self):
        for key_book in BookVal:
            print(BookVal[key_book]['title'])

class thong_ke_sach:
    '''
    Thống kê số lượng, tiền cao nhất - thấp nhất
    '''

    def tk_sach_tinh_thanh(self):
        for key_zone in locationZone:
            count = 0
            for key_book in BookVal:
                count += BookVal[key_book]["location_zone"][key_zone]
            print("Tỉnh: %s - Tổng số sách: %s " %  (locationZone[key_zone]["title"], count))

    def tk_tong_tien_sach_moi_tinh(self):
        for key_zone in locationZone:
            print("Tỉnh: %s " % locationZone[key_zone]["title"])
            for key_book in BookVal:
                price = int(BookVal[key_book]["price"].replace(',',''))
                so_sach = int(BookVal[key_book]["location_zone"][key_zone])
                tong_tien = price * so_sach
                print("- '%s' : %s x %s = %s" % (BookVal[key_book]["title"], BookVal[key_book]["price"], BookVal[key_book]["location_zone"][key_zone], tong_tien))

    def tk_loai_sach_moi_tinh_thanh(self):
        for key_zone in locationZone:
            print("Tỉnh: %s " % locationZone[key_zone]["title"])
            for key_book in BookVal:
                print("- '%s' : %s cuốn " % (BookVal[key_book]["title"], BookVal[key_book]["location_zone"][key_zone]))

    def tk_gia_cac_loai_sach_moi_tinh_thanh(self):
        for key_zone in locationZone:
            print("Tỉnh: %s " % locationZone[key_zone]["title"])
            for key_book in BookVal:
                print("- '%s' = %s  " % (BookVal[key_book]["title"], BookVal[key_book]["price"]))

    def tk_gia_sach_lon_nho_nhat_moi_tinh_thanh(self):

        key_first = list(BookVal.keys())[0]

        max_gia = int(BookVal[key_first]["price"].replace(',',''))
        flag_max = '1'
        for key_book in BookVal:
            price = int(BookVal[key_book]["price"].replace(',',''))
            if price > max_gia:
                max_gia = price
                flag_max = key_book

        min_gia = int(BookVal[key_first]["price"].replace(',',''))
        flag_min = '1'
        for key_book in BookVal:
            price = int(BookVal[key_book]["price"].replace(',',''))
            if price < min_gia:
                min_gia = price 
                flag_min = key_book

        print("giá sách cao nhất: %s - Tên sách: '%s' " % (BookVal[flag_max]["price"], BookVal[flag_max]["title"]))
        print("giá sách thấp nhất: %s - Tên sách: '%s' " % (BookVal[flag_min]["price"], BookVal[flag_min]["title"]))
    
class timkiem:
    def __init__(self, _nhap_chuoi):
       self.nhap_chuoi = _nhap_chuoi

    def kiem_tra_match(self):
        list_sach = []
        for key_zone in locationZone:
            count_sach = 0
            for key_book in BookVal:
                for value_book in BookVal[key_book]:
                    if re.findall(r'(.*)' + str(self.nhap_chuoi) + '(.*)', str(BookVal[key_book][value_book])):
                        count_sach += BookVal[key_book]["location_zone"][key_zone]
                        out = "Tỉnh: %s - Tên Sách: %s - Giá: %s - Ngày xuất bản: %s - Số lượng: %s cuốn"  % (locationZone[key_zone]["title"], BookVal[key_book]["title"],BookVal[key_book]["price"], BookVal[key_book]["published"], count_sach)
                        list_sach.append(out)

        if len(list_sach) > 0:
            for i in list_sach:
                print(i)
        else:
            print("Không tìm thấy kết quả tìm kiếm nào !!! \n") 


# ------------- Menu ---------------------------- 
def menu_liet_ke():
    print("\nMenu: Liệt kê")
    print("\t1. Liệt kê cửa hàng ở các tỉnh. ")
    print("\t2. Liệt kê tên sách trong kho. ")
    print("\t3. Thoát. ")

    chon_menu = input("Nhập vào một số theo menu trên: ")

    if chon_menu == "1":
        hien_thi_tinh_thanh = liet_ke_sach_tinh_thanh()
        hien_thi_tinh_thanh.ds_tinh_thanh()
    if chon_menu == "2":
        C_liet_ke_sach = liet_ke_sach_trong_kho()
        C_liet_ke_sach.ds_sach()
    if chon_menu == "3":
        sys.exit()

def menu_thong_ke():
    print("\nMenu: thống kê")
    print("\t1. Thống kê tổng số sách ở các tỉnh thành.")
    print("\t2. Thống kê tổng số tiền sách tồn kho ở mỗi tỉnh thành")
    print("\t3. Thống kê các loại sách ở mỗi tỉnh thành")
    print("\t4. Thống kê giá các loại sách ở mỗi tỉnh thành")
    print("\t5. Thống kê giá lớn nhất và giá sách nhỏ nhất mỗi tỉnh thành")
    print("\t6.Thoát ")

    chon = input("Nhập vào một số theo menu trên: ")

    # --- khởi tạo class
    C_thong_ke_sach = thong_ke_sach()

    if chon == "1":
        C_thong_ke_sach.tk_sach_tinh_thanh() 
    if chon == "2":
        C_thong_ke_sach.tk_tong_tien_sach_moi_tinh() 
    if chon == "3":
        C_thong_ke_sach.tk_loai_sach_moi_tinh_thanh()
    if chon == "4":
        C_thong_ke_sach.tk_gia_cac_loai_sach_moi_tinh_thanh()
    if chon == "5":
        C_thong_ke_sach.tk_gia_sach_lon_nho_nhat_moi_tinh_thanh()
    if chon == "6":
        sys.exit()

def menu_tim_kiem():

    print("\nMenu: tìm kiếm")
    print("\t1. Tìm kiếm: tên sách, giá cả, ngày xuất bản, tỉnh thành ")
    print("\t2. Thoát ")
    chon = input("Nhập vào một số theo menu trên: ")

    if chon == "1":
        nhap_chuoi = input("Nhập tìm kiếm: ")
        # khởi tạo class:
        C_tim_kiem = timkiem(nhap_chuoi)
        C_tim_kiem.kiem_tra_match()

    if chon == "2":
        sys.exit()

def main():
    print("\t1. Menu thống kê. ")
    print("\t2. Menu tìm kiếm. ")
    print("\t3. Menu liệt kê. ")
    print("\t4. Thoát. ")
    chon_menu = input("Chọn menu:")
    if chon_menu == "1":
        menu_thong_ke()
    if chon_menu == "2":
        menu_tim_kiem()
    if chon_menu == "3":
        menu_liet_ke()
    if chon_menu == "4":
        sys.exit()

if __name__ == "__main__":
    main()


