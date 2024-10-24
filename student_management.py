class Student:

    def __init__(self, id, name, sex, birth, address, mclass, sclass, number_of_subjects, gpa = 0, cpa = 0, training_score = 0, hocluc = ''):
        self._id = id
        self._name = name
        self._birth = birth
        self._sex = sex         
        self._address = address # Quê
        self._mclass = mclass   # Khoa
        self._sclass = sclass   # Lớp
        self._number_of_subjects = number_of_subjects
        self._gpa = gpa
        self._cpa = cpa
        self._training_score = training_score  
        self._hocluc = hocluc
        
## Chức năng 1: quản lý sinh viên
    def chuan_hoaname(self):
        self._name = ' '.join(word.capitalize() for word in self._name.split())
        return self._name

    def chuan_hoabirth(self):
        specialchr = '-!\#%*&>< '
        for chr in specialchr:
            if chr in self._birth:
                self._birth = self._birth.replace(chr,'/')
        x, y, z = map(str, self._birth.split('/'))
        if len(x) < 2:
            x = '0' + x
        if len(y) < 2:
            y = '0' + y
        self._birth = '/'.join([x, y, z])
        return self._birth

## Chức năng 2: quản lý học tập
# Tính điểm cpa, gpa
    def caculate_score(self):
        self._cpa = 0
        self._gpa = 0
        number_of_credits = 0
        for x in range (self._number_of_subjects):
            name_of_sub = input('Nhập tên môn học:  ')
            credits_of_sub = int(input('Nhập số lượng tín chỉ:  '))
            
            # cc, gk, bt, thí nghiệm: 10% ; ck: 60%
            while True:
                try:
                    cc, gk, bt, thi_nghiem, ck = map(float, input('Nhập điểm cc, gk, bt, thí nghiệm, ck:   ').split())
                    break 
                except ValueError:
                    print("Dữ liệu không hợp lệ. Vui lòng nhập lại các điểm số.")
            
            # Nếu có 1 điểm = 0 thì trượt môn 
            if cc == 0 or bt == 0 or gk == 0 or thi_nghiem == 0 or ck == 0:
                cpa_of_sub = 0.0
            else: cpa_of_sub = (cc + gk + bt + thi_nghiem) * 0.1 + ck * 0.6

            # Tính gpa từ cpa:
            if 0.0 <= cpa_of_sub and cpa_of_sub < 3.95:
                gpa_of_sub = 0.0
            elif cpa_of_sub < 4.95:
                gpa_of_sub = 1.0
            elif cpa_of_sub < 5.45:
                gpa_of_sub = 1.5
            elif cpa_of_sub < 6.45:
                gpa_of_sub = 2.0
            elif cpa_of_sub < 6.95:
                gpa_of_sub = 2.5
            elif cpa_of_sub < 7.95:
                gpa_of_sub = 3.0
            elif cpa_of_sub < 8.45:
                gpa_of_sub = 3.5
            elif cpa_of_sub < 8.95:
                gpa_of_sub = 3.7
            else:
                gpa_of_sub = 4.0
            # cpa/gpa tổng = cpa/gpa 1 môn * số tín chỉ
            self._cpa += cpa_of_sub * credits_of_sub
            self._gpa += gpa_of_sub * credits_of_sub
            # Tính tổng số tín chỉ
            number_of_credits += credits_of_sub
        # tính gpa, cpa cuối cùng = cpa/gpa chia tổng tín chỉ
        self._cpa /= number_of_credits
        self._gpa /= number_of_credits

    def get_gpa(self):
        return self._gpa
    
    def get_cpa(self):
        return self._cpa

# Xếp loại học lực
    def hocluc(self):
        if self._gpa < 2.0:
            return 'Kem'
        elif self._gpa < 2.5:
            return 'Trung Binh'
        elif self._gpa < 3.2:
            return 'Kha'
        elif self._gpa < 3.6:
            return 'Gioi'
        else:
            return 'Xuat Sac'
        
# Xuất thông tin về gpa, cpa, học lực
    def display_gpa(self):
        return f'{self._id} {self.chuan_hoaname()} {self._sex} {self._gpa:.2f}'
    
    def display_cpa(self):
        return f'{self._id} {self.chuan_hoaname()} {self._sex} {self._cpa:.2f}'
    
    def display_hocluc(self):
        return f'{self._id} {self.chuan_hoaname()} {self._sex} {self.hocluc()}'


# Chức năng 3: quản lý điểm rèn luyện
# Xử lí gpa -> điểm rèn luyện
    def xu_li_gpa(self) -> int:
        if self._gpa >= 3.6 : return 10
        elif self._gpa >= 3.2 : return 8
        elif self._gpa >= 3.0 : return 6
        elif self._gpa >= 2.8 : return 4
        elif self._gpa >= 2.5 : return 2
        else : return 0
# Tính điểm rèn luyện
    constant = 70 
    def diem_ren_luyen(self, sk1, sk2, ngoai_tru, thanh_tich) -> float:
        self.xu_li_gpa()
        return sk1 * 0.5 + sk2 * 1 + self.xu_li_gpa() - ngoai_tru + thanh_tich + self.constant

# Xuất thông tin không chứa điểm rèn luyện
    def display_sv(self):
        return f'{self._id} {self.chuan_hoaname()} {self._sex} {self.chuan_hoabirth()} {self._address} {self._mclass} {self._sclass}'

# Xuất thông tin chứa điểm rèn luyện
    def display_drl(self):
        return f'{self._id} {self.chuan_hoaname()} {self._sex} {self._sclass} {self._training_score}'
    
# Xuất thông tin của tất cả thuộc tính
    def display_all(self):
        return f'{self._id} {self.chuan_hoaname()} {self._sex} {self.chuan_hoabirth()} {self._address} {self._mclass} {self._sclass} {self._gpa:.2f} {self._cpa:.2f} {self.hocluc()} {self._training_score}'


# Hàm nhập giới tính
def input_gender():
    while True:
        user_input = input("Nhập giới tính (Nam/Nữ): ").strip().lower()
        if user_input in ["nam", "nữ"]:
            return user_input.capitalize()
        else:
            print("Giới tính không hợp lệ. Vui lòng nhập lại.")

# Hàm nhập msv
def input_id():
    while True:
        id = input("Nhập mã sinh viên (xxx): ").strip()
        if id.isdigit() and len(id) == 3:
            return id
        else:
            print("Mã sinh viên không hợp lệ. Vui lòng nhập lại theo định dạng xxx.")


def main():
    Student_list = []
    while True:
        print('''Chức năng bạn muốn chọn:
              
          0. Thoát
          1. Quản lí sinh viên
          2. Quản lí học tập
          3. Quản lí điểm rèn luyện
              
               ...''')
        M = int(input('Nhập chức năng bạn chọn: '))
        if M == 0:
            break

## Chức năng 1: quản lý sinh viên
        elif M == 1:
            while True:
                print('''Chức năng bạn muốn chọn: 
                    
                    0. Thoát
                    1. Thêm sinh viên mới
                    2. Xóa sinh viên theo msv
                    3. Sửa thông tin sinh viên theo msv
                    4. Tìm kiếm và hiển thị theo msv

                    ''')
                N = int(input('Nhập chức năng bạn chọn: '))

        # Thoát
                if N == 0 : break

        # Thêm sinh viên
                elif N == 1:
                    n1 = int(input('Nhập số lượng sinh viên bạn muốn thêm: '))
                    for i in range(n1):
                        id = input_id()
                    #-> nếu tồn tại mã sinh viên rồi thì nhập lại dữ liệu
                        point = ''
                        for student in Student_list:
                            if student._id == id: 
                                point = id
                                break
                        while point == id:
                            print('Mã sinh viên bạn nhập đã tồn tại, hãy nhập lại') 
                            id = input_id()
                        
                        name = input(f'Nhập tên của sinh viên thứ {i+1}: ').strip()
                        sex = input_gender()
                        birth = input(f'Nhập ngày sinh của sinh viên thứ {i+1}: ').strip()
                        address = input(f'Nhập địa chỉ của sinh viên thứ {i+1}: ').strip()
                        mclass = input(f'Nhập ngành của sinh viên thứ {i+1}: ').strip()
                        sclass = input(f'Nhập lớp của sinh viên thứ {i+1}: ').strip()
                        while True :
                            try:
                                number_of_subjects = int(input('Nhập số lượng môn học: '))
                                break
                            except ValueError:
                                print('Nhập lại số lượng môn học: ')
                        s = Student(id, name, sex, birth, address, mclass, sclass, number_of_subjects)
                        if s._number_of_subjects == 0:
                            Student_list.append(s)
                        else:
                            s.caculate_score()
                            Student_list.append(s)
                        
        # Xóa sinh viên theo mã sinh viên
                elif N == 2:
                    while True:
                        n2 = input("Nhập mã sinh viên bạn muốn xóa(xxx): ").strip()
                        if n2.isdigit() and len(n2) == 3:
                            break
                        else:
                            print("Mã sinh viên không hợp lệ. Vui lòng nhập lại theo định dạng xxx.")
                    for student in Student_list:
                        if student._id == n2:
                            Student_list.remove(student)
                            break

        # Sửa thông tin sinh viên theo mã sinh viên
                elif N == 3:
                    while True:
                        n3 = input("Nhập mã sinh viên bạn muốn sửa(xxx): ").strip()
                        if n3.isdigit() and len(n3) == 3:
                            break
                        else:
                            print("Mã sinh viên không hợp lệ. Vui lòng nhập lại theo định dạng xxx.")
                    for student in Student_list:
                        if student._id == n3:
                            student._name = input('Nhập tên sinh viên mới: ').strip()
                            student._sex = input_gender()
                            student._birth = input('Nhập ngày sinh của sinh viên mới: ').strip()
                            student._address = input('Nhập địa chỉ của sinh viên mới: ').strip()
                            student._mclass = input('Nhập ngành của sinh viên mới: ').strip()
                            student._sclass = input('Nhập lớp của sinh viên mới: ').strip()
                            while True :
                                try:
                                    student.number_of_subjects = int(input('Nhập số lượng môn học: '))
                                    break
                                except ValueError:
                                    print('Nhập lại số lượng môn học: ')
                            if student.number_of_subjects == 0: 
                                break
                            else: 
                                student.caculate_score()
                            break

        # Tìm kiếm và hiển thị thông tin sinh viên
                elif N == 4:
                    while True:
                        n4 = input("Nhập mã sinh viên bạn muốn tìm(xxx): ").strip()
                        if n4.isdigit() and len(n4) == 3:
                            break
                        else:
                            print("Mã sinh viên không hợp lệ. Vui lòng nhập lại theo định dạng xxx.")
                    for student in Student_list:
                        if student._id == n4:
                            print(student.display_sv())
                            break
                else: 
                    break


## Chức năng 2: quản lý học tập
        elif M == 2:
            while True:
                print('''Chức năng bạn muốn chọn là:
                    
                0. Thoát
                1. Hiển thị gpa sinh viên theo msv
                2. Hiển thị cpa sinh viên theo msv
                3. Sắp xếp sinh viên theo gpa giảm dần
                4. Sắp xếp sinh viên theo cpa giảm dần
                5. Hiển thị học lực của sinh viên

                ''')
                N2 = int(input('Nhập chức năng bạn chọn:  '))
                if N2 == 0: break

        # Hiển thị điểm gpa của sinh viên theo mã sinh viên
                elif N2 == 1:
                    while True:
                        n6 = input("Nhập mã sinh viên bạn cần xem gpa(xxx): ").strip()
                        if n6.isdigit() and len(n6) == 3:
                            break
                        else:
                            print("Mã sinh viên không hợp lệ. Vui lòng nhập lại theo định dạng xxx.")
                    check = 0
                    for student in Student_list:
                        if student._id == n6:
                            check = 1
                            print(student.display_gpa())
                            break
                    if check == 0: print('Không tồn tại sinh viên này')

        # Hiển thị điểm cpa của sinh viên theo mã sinh viên
                elif N2 == 2:
                    while True:
                        n7 = input("Nhập mã sinh viên bạn muốn xem cpa(xxx): ").strip()
                        if n7.isdigit() and len(n7) == 3:
                            break
                        else:
                            print("Mã sinh viên không hợp lệ. Vui lòng nhập lại theo định dạng xxx.")
                    check = 0
                    for student in Student_list:
                        if student._id == n7:
                            check = 1
                            print(student.display_cpa())
                            break
                    if check == 0: print('Không tồn tại sinh viên này')

        # Sắp xếp sinh viên theo gpa giảm dần 
                elif N2 == 3:
                    Student_list.sort(key = lambda x : (- x.get_gpa()))
                    for student in Student_list:
                        print(student.display_gpa())

        # Sắp xếp sinh viên theo cpa giảm dần
                elif N2 == 4:
                    Student_list.sort(key = lambda x : (- x.get_cpa()))
                    for student in Student_list:
                        print(student.display_cpa())

        # Hiển thị học lực của sinh viên 
                elif N2 == 5:
                    while True:
                        n10 = input("Nhập mã sinh viên bạn muốn xem học lực(xxx): ").strip()
                        if n10.isdigit() and len(n10) == 3:
                            break
                        else:
                            print("Mã sinh viên không hợp lệ. Vui lòng nhập lại theo định dạng xxx.")

                    check = 0
                    for student in Student_list:
                        if student._id == n10:
                            check = 1
                            print(student.display_hocluc())
                            break
                    if check == 0: print('Không tồn tại sinh viên này')
                else: break
                        

## Chức năng 3: quản lý điểm rèn luyện
        elif M == 3:
            while True:
                print('''
                    
                    0. Thoát
                    1. Hiển thị drl của sinh viên theo msv
                    2. Hiển thị danh sách sinh viên đầy đủ
                    
                    ''')
                N3 = int(input('Nhập chức năng bạn chọn:  '))
                if N3 == 0: break
        # Hiển thị điểm rèn luyện của sinh viên theo msv
                elif N3 == 1:
                    while True:
                        n11 = input("Nhập mã sinh viên bạn muốn xem điểm rèn luyện(xxx): ").strip()
                        if n11.isdigit() and len(n11) == 3:
                            break
                        else:
                            print("Mã sinh viên không hợp lệ. Vui lòng nhập lại theo định dạng xxx.")
                    point = 0
                    for student in Student_list:
                        if student._id == n11:
                            point = 1
                            if student._training_score >  70: 
                                    print(student.display_drl())
                                    break
                            else:   
                                print('Nhập các hoạt động và thành tích đã tham gia của sinh viên:  ')
                                s1 = int(input('Nhập số sự kiện loại 1 đã tham gia (0.5 điểm / 1 sk):  '))
                                s2 = int(input('Nhập số sự kiện loại 2 đã tham gia (1 điểm / 1 sk):    '))
                                s3 = int(input('Nhập 1 nếu sinh viên đã khai báo nội & ngoại trú, 0 nếu chưa: '))
                                s4 = int(input('Nhập số lượng thành tích sinh viên đã đạt được (3 điểm / 1 thành tích): '))
                                if s3 == 0 : point = 5
                                student._training_score = student.diem_ren_luyen(s1, s2 ,point ,s4 * 3)
                                print(student.display_drl())
                                break
                    if point == 0: 
                        print('Không tồn tại sinh viên này')

        # Hiển thị danh sách sinh viên có cả cpa, gpa, đrl, học lực
                elif N3 == 2:  
                    if len(Student_list) == 0:
                        print('Danh sách rỗng!')
                    else:
                        for student in Student_list:
                            print(student.display_all())
                else: break
        else : break

if __name__ == '__main__':
    main()