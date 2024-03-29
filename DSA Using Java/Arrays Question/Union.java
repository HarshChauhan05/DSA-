package com.Array;

import java.util.ArrayList;
import java.util.List;

public class UnionOfSortedArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int arr1[] = { 1, 2, 3, 3, 4, 5, 5 };
		int arr2[] = { 1, 1, 2, 2, 2, 8, 9 };
		int i = 0, j = 0;
		List<Integer> res = new ArrayList<>();
		while (i<arr1.length || j<arr2.length) {

			// Skip Duplicate
			while (i>0 && i<arr1.length && arr1[i]==arr1[i - 1])
				i++;
			while (j>0 && j<arr2.length && arr2[j] == arr2[j - 1])
				j++;

			// one array Exhausted
			if (i>=arr1.length) {
				res.add(arr2[j]);
				j++;
				continue;
			}
			if (j>=arr2.length) {
				res.add(arr1[i]);
				i++;
				continue;
			}

			// Comparsion
			if (arr1[i] < arr2[j]) {
				res.add(arr1[i]);
				i++;
			} else if (arr1[i] > arr2[j]) {
				res.add(arr2[j]);
				j++;
			} else {
				res.add(arr1[i]);
				i++;
				j++;
			}
		}
		System.out.println(res);
	}

}
