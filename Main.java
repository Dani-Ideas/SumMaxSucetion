package org.example;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);        //TIP Press <shortcut actionId="ShowIntentionActions"/> with your caret at the highlighted text
        // to see how IntelliJ IDEA suggests fixing it.
        System.out.printf("Hello and welcome!");
        String entrada = scanner.nextLine();
        int n = Integer.parseInt(entrada), temp=0;
        List<Integer> list = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if ((Math.random() * 100)<50){
                temp=1;
            }else
                temp=-1;
            list.add(((int) (Math.random() * 100))*temp);
        }
        int matrix[][]= new int[n][n];
        setDiagonalMain(matrix,list);
        setAllSum(matrix);
        System.out.println(list);
        printMatrix(matrix);
        searchMaxValueSum(matrix);
    }

    private static void searchMaxValueSum(int[][] matrix) {
        
    }

    private static void printMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
    }

    private static void setAllSum(int[][] matrix) {
        // Sumar los valores de la primera columna
        for (int i = 1; i < matrix.length; i++) {
            matrix[i][0] = matrix[i - 1][0] + matrix[i][i]; // Sumar el valor de la diagonal actual
        }

        // Sumar los valores de la segunda columna
        for (int i = 2; i < matrix.length; i++) {
            matrix[i][1] = matrix[i - 1][1] + matrix[i][i]; // Sumar el valor de la diagonal actual
        }
    }



    private static void setDiagonalMain(int[][] matrix, List<Integer>list) {
        for (int i = 0; i < matrix.length; i++) {
            matrix[i][i]= list.get(i);
        }
    }
}