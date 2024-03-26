package com.yunseong.algorithm.greedy

import java.util.LinkedList

fun main() {
    val br = System.`in`.bufferedReader()

    val (a, b) = br.readLine().split(" ").map { it.toLong() }

    val list = LinkedList<Pair<Long, Long>>()
    list.add(a to 1)

    while (list.isNotEmpty()) {
        val (v, i) = list.pop()

        if (v > b) {
            continue
        }

        if (v == b) {
            println(i)
            return
        }

        list.add(v * 2 to i + 1)
        list.add("${v}1".toLong() to i + 1)
    }
    println(-1)
}