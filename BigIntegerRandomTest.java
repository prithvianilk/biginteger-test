package org.example;

import java.math.BigInteger;
import java.util.Random;

public class BigIntegerRandomTest {
    public static void main(String[] args) {
        for (int i = 0; i < 1_00_000; ++i) {
            var x = new BigInteger(126, new Random());
            System.out.println(x);
        }
    }
}

