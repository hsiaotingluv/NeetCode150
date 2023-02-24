class ArrListLenSolution {
    public int solution(int[] A) {
        int result = 0;
        int index = 0;

        while (A[index] != -1) {
            result += 1;
            index = A[index];
        }
        
        return result+1;
    }
}

public class ArrListLen {
    public static void main(String[] args) {

        int[] arr = {1, 4, -1, 3, 2};

        ArrListLenSolution sol = new ArrListLenSolution();

        int result = sol.solution(arr);
        System.out.println(result);
    }
}

