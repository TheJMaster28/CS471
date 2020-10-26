PROGRAM gaussian_elimination
      IMPLICIT NONE
  
      INTEGER,PARAMETER::n=3
      INTEGER::i,j
  
      REAL::s
      REAL,DIMENSION(n,n+1)::a
      REAL,DIMENSION(n)::x
      

      OPEN(1,FILE='input.txt')
      OPEN(2,FILE='output.txt')
  
      READ(1,*)((a(i,j),j=1,n+1),i=1,n)
  
      WRITE(2,8)"Augmented Matrix",((a(i,j),j=1,n+1),i=1,n)
  
      DO j=1,n
          DO i=j+1,n
              a(i,:)=a(i,:)-a(j,:)*a(i,j)/a(j,j)
          END DO
      END DO
  
      WRITE(2,8)"After Gaussian Elimination",((a(i,j),j=1,n+1),i=1,n)
      
      DO i=n,1,-1
            ! s=a(i,n+1)
            DO j=i-1,1,-1
                  ! s=s-a(i,j)*a(j,n+1)
                  ! s=s-a(i,j)*x(j)
                  s= a(j,i) / a(i,i)
                  a(j,:) = a(j,:) - (s*a(i,:))
            END DO
            a(i,:) = a(i,:) / a(i,i)
      !     x(i)=s/a(i,i)
      !     a(i,n+1)=s/a(i,i)
      END DO
      print *,a
      WRITE(2,9)"X=",(x(i),i=1,n)
  
      8 FORMAT(a,/,3(4(f7.2,3x),/))
      9 FORMAT(a,/,3(f7.2,/))
  
  END PROGRAM