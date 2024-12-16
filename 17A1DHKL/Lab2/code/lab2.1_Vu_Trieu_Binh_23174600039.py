import numpy as np
nhiet_do_hang_ngay = np.random.uniform(high=30, low = 10, size = 30)
#lam tron den so thu 2
lam_tron = np.round(nhiet_do_hang_ngay,2)
nhiet_do_trung_binh = np.mean(nhiet_do_hang_ngay)
print(f"nhiet do ngau nhien trong 30 ngay: {nhiet_do_hang_ngay}")
print(f"nhiet do trung binh: {nhiet_do_trung_binh}")

#2. Phan tich xu huong nhiet do
nhiet_do_cao_nhat = np.max(nhiet_do_hang_ngay)
nhiet_do_thap_nhat = np.min(nhiet_do_hang_ngay)

ngay_nhiet_do_cao_nhat = np.argmax(nhiet_do_hang_ngay) + 1
ngay_nhiet_do_thap_nhat = np.argmin(nhiet_do_hang_ngay) + 1

print(f"nhiet do ngay cao nhat trong thang la:", nhiet_do_cao_nhat)
print(f"ngay co nhiet do cao nhat trong thang:", ngay_nhiet_do_cao_nhat)
print(f"nhiet do thap nhat trong thang:", nhiet_do_thap_nhat)
print(f"ngay co nhiet do thap nhat trong thang:", ngay_nhiet_do_thap_nhat)
#su chenh lech giua cac ngay 

chenh_lech_nd = np.diff(nhiet_do_hang_ngay)
chenh_lech_lon_nhat = np.max(np.abs(chenh_lech_nd))
chenh_lech_ngay_lon_nhat = np.argmax(np.abs(chenh_lech_nd))


print(f"su chenh lech nhiet do lon nhat la:", chenh_lech_lon_nhat, "giua ngay thu", chenh_lech_ngay_lon_nhat, "va ngay thu", chenh_lech_ngay_lon_nhat)

#3 fancy indexing

ngay_nhiet_do_tren_20 = np.where(nhiet_do_hang_ngay > 20)[0] + 1
nhiet_do_tren_20 = nhiet_do_hang_ngay[nhiet_do_hang_ngay>20]
print("cac ngay co nhiet do cao hon 20 la:", ngay_nhiet_do_tren_20)
print("nhiet do tuong ung:", nhiet_do_tren_20)

#b)
ngay = [5,10,15,20,25]
nhiet_do_cu_the = nhiet_do_hang_ngay[np.array(ngay) + 1]
print("nhiet do vao cac ngay 5 10 15 20 25 la:", nhiet_do_cu_the)
#c)
ngay_nhiet_do_tren_tb = np.where(nhiet_do_hang_ngay > nhiet_do_trung_binh)[0] + 1
nhiet_do_tren_tb = nhiet_do_hang_ngay[nhiet_do_hang_ngay > nhiet_do_trung_binh]

#d)
ngay_chan = np.arange(2,31,2)
ngay_le = np.arange(1,31,2)

nhiet_do_ngay_chan = nhiet_do_hang_ngay[ngay_chan - 1]
nhiet_do_ngay_le = nhiet_do_hang_ngay[ngay_le - 1]
print("nhiet do cac ngay chan:", nhiet_do_ngay_le)
