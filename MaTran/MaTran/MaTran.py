
def make_matrix(n):
    print(n)
    return [[0]*n for i in range(n)]

def set_matrix(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(n):
            ele = int(input('Phan tu hang %d,cot %d\n>>> '%(i,j)))
            matrix[i][j] = ele
def print_primary_diagonal(matrix):
    n=len(matrix)
    for i in range(n):
        print (matrix[i][i])
      
def main():
    ch = 0
    matrix_N = make_matrix( n= int(input("Nhap chieu dai canh ma tran:")))
    while ch!=3:
        print ("MENU\t1.Chon 1 de Nhap vao ma tran.")
        print ("2. Chon 2 de In cac phan tu duong cheo chinh.")
        print ("4. Chon 4 de In ma tran .")
        print ("3. Chon 3 de Ket thuc.\tMoi ban chon.")
        ch=int(input("Nhap y/c ban chon:"))
        if ch==1:
            print ("Moi nhap vao MA TRAN!!!") 
            set_matrix(matrix_N)
        elif ch==2:
            print_primary_diagonal(matrix_N)   
        elif ch==4:
            print(matrix_N)
        elif ch==3:
            pass
        else:
            print("Nhap sai, moi nhap lai.")

if __name__=="__main__":
    main()