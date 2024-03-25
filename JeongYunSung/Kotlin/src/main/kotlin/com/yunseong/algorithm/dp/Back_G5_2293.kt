package com.yunseong.algorithm.dp

fun main() {
    val br = System.`in`.bufferedReader()
    val (n, k) = br.readLine().split(" ").map { it.toInt() }

    val coins = IntArray(n) {
        br.readLine().toInt()
    }

    val dp = IntArray(k + 1)

    dp[0] = 1
    for (coin in coins) {
        for (i in coin..k) {
            dp[i] += dp[i - coin]
        }
    }

    println(dp[k])
}