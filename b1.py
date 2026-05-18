print(' --- HỆ THONG TIEP NHẬN BENH NHÂN---')
name_patient = input ( 'Nhập tên bệnh nhân: ');
age = int(input('Mời bạn nhập tuổi: '));
symptom = input ('Mời bạn nhập triệu chứng bênh: ');

print(' -- PHIẾU KHÁM BỆNH --- ');
print ('Tên bệnh nhân:', symptom);
print('Tuổi:', name_patient);
print ('Triệu chứng:', age);

# nguyên nhân chương trình không bị crash nhưng dữ liệu in ra sai bởi vì trong bài vẫn sử dụng đúng cú pháp 
# nhưng sắp xếp cú pháp sai 
# Chỉ ra nguyên nhân gây lỗi logic sắp xếp các tên biến lộn xộn.

# Sửa lại :
print(' --- HỆ THONG TIEP NHẬN BENH NHÂN---')
name_patient = input ( 'Nhập tên bệnh nhân: ');
age = int(input('Mời bạn nhập tuổi: '));
symptom = input ('Mời bạn nhập triệu chứng bênh: ');

print(' -- PHIẾU KHÁM BỆNH --- ');
print ('Tên bệnh nhân:',name_patient );
print('Tuổi:', age);
print ('Triệu chứng:', symptom);
