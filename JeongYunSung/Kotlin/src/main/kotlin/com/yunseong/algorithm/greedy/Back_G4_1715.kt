package com.yunseong.algorithm.greedy

import java.util.PriorityQueue

fun main() {
    val br = System.`in`.bufferedReader()

    val queue = PriorityQueue<Int>()

    val n = br.readLine().toInt()

    repeat(n) {
        queue.add(br.readLine().toInt())
    }

    if (n == 1) {
        println(0)
        return
    }

    var answer = 0

    while (queue.isNotEmpty()) {
        var num = queue.poll()

        if (queue.isNotEmpty()) {
            num += queue.poll()
        }
        if (queue.isNotEmpty()) {
            queue.add(num)
        }

        answer += num
    }

    println(answer)
}