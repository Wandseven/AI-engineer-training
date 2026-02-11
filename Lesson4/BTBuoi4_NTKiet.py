#Hàm tìm số lớn nhất
def tim_so_lon_nhat(x, y, z):
    m = x if x > y else y
    m = z if z > m else m
    return m

#max = tim_so_lon_nhat(1, 2, 3)
#print(max)

#Hàm chuyển đổi nhiệt độ
def chuyen_doi_nhiet_do(c):
    f = c*1.8 + 32
    return f

#f = chuyen_doi_nhiet_do(30)
#print(f)

#Hàm in hình chữ nhật
def in_hinh_chu_nhat(n, m):
    for i in range(n):
        for j in range(m):
            print('*', end='')
        print()

#in_hinh_chu_nhat(4, 5)

#Hàm kiểm tra số chính phương
def kiem_tra_so_chinh_phuong(a):
    c = a ** 0.5
    if c % 1 == 0:
        print(f'{a} là số chính phương')
    else:
        print(f'{a} không phải là số chính phương')

#kiem_tra_so_chinh_phuong(9)

#Hàm tính tiền điện
def tinh_tien_dien(k):
    if 0 <= k <= 50:
        price = k*1678
    elif 50 < k <= 100:
        price = 50*1678 + (k-50)*1734
    elif 100 < k <= 200:
        price = 50*1678 + 50*1734 + (k-100)*2014
    else:
        price = 50*1678 + 50*1734 + 100*2014 + (k-200)*2536

    if k >= 0:
        print(f'Tiền điện là {price:.2f} VND')
    else:
        print('Số điện không hợp lệ.')

if __name__=='__main__':
    while True:
        k = int(input('Mời nhập vào số điện: '))
        tinh_tien_dien(k)
        c = input('Bạn có muốn tiếp tục không? (Y/N): ')
        if c == 'N':
            print('Cảm ơn bạn đã sử dụng dịch vụ.')
            break