package basico2_3;

import java.util.Arrays;

public class ex04 {
    public static void main(String[] args) {
        
        int arrayUm[] = {20, 17, 22, 18, 36, 57,33};
        int arrayDois[] = new int[7];
        
        for (int i = arrayUm.length - 1; i >= 0; i--) {
            System.out.print(" " + arrayUm[i]);
        }
        System.out.println();
        
        for (int x = arrayDois.length - 1; x >= 0; x--) {
            if (x < arrayUm.length) {
                arrayDois[x] = arrayUm[x];	
            }
            System.out.print(" " + arrayDois[x]);
        }
        System.out.println();
        Arrays.sort(arrayDois);
        for (int z = 0; z < arrayDois.length; z++) {
            System.out.print(" " + arrayDois[z]);
        }
        System.out.println();
        for(int y =0; y < arrayUm.length; y++) {
        System.out.print(" "+ arrayUm[y]);
    }
  }
}
