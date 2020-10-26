function create_matrix ( N ) result(A)
    ! implicit NONE
    integer, intent(in) :: N
    integer i,j
    real, dimension(:,:), allocatable :: A
    ! integer,parameter :: seed = 86456
  
    ! call srand(seed)
    ALLOCATE(A(N,N+1))
    do i = 1,N
        do j=1,N
            A(i,j) = INT((rand() * (20 - 1 + 1)) + 1 )
        end do
    end do
end function create_matrix  

! source: https://labmathdu.wordpress.com/gaussian-elimination-without-pivoting/
subroutine gaussian_elimination ( a,n )
    ! implicit none
    real, dimension(:,:), intent(inout) ::a
    INTEGER,intent(in)::n
    INTEGER::i,j
    REAL::s


    DO j=1,n
        DO i=j+1,n
            a(i,:)=a(i,:)-a(j,:)*a(i,j)/a(j,j)
        END DO
    END DO

    DO i=n,1,-1
        DO j=i-1,1,-1
              s= a(j,i) / a(i,i)
              a(j,:) = a(j,:) - (s*a(i,:))
        END DO
        a(i,:) = a(i,:) / a(i,i)
    END DO
    
end subroutine gaussian_elimination


function test_case ( N ) result(T)
! implicit NONE
    interface
        function create_matrix(N) result (A)
            integer, intent(in) :: N
            real, dimension(:,:), allocatable :: A
        end function
        subroutine gaussian_elimination(A,N)
            real, dimension(:,:), intent(inout) ::A
            integer,intent(in)::N
        end subroutine
   end interface 
    integer, intent(in) :: N
    real, dimension(:,:),allocatable :: A
    
    REAL :: time_begin, time_end, T
    
    A=create_matrix(N)


    CALL CPU_TIME ( time_begin )

    call gaussian_elimination(A,N)

    CALL CPU_TIME ( time_end )
    
    T=time_end - time_begin
    

end function test_case

program p4
    ! implicit NONE

    integer, dimension (5) :: Sizes

    integer :: n
    integer :: j
    integer :: i
    real :: time

    Sizes(1) = 250
    Sizes(2) = 500
    Sizes(3) = 1000
    Sizes(4) = 1500
    Sizes(5) = 2000

    do j=1,5
        print *,"Test Case ",j 
        do n=1,5
            i = Sizes(n)
            time = test_case(i) *1000
            
            print *, i, " ", time,"milliseconds"
        end do
    end do

end program p4
