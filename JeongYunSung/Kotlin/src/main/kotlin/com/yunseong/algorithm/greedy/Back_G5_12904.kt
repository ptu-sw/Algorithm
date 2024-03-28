package com.yunseong.algorithm.greedy

/**
 * 1. 문제에서 정답으로 가는 것 보다, 정답에서 문제로 가는것이 더 편하다.
 *
 *    가령 이 문제에서 1 -> 1122보다 1122 -> 1로 가는것이 편하다.
 */
fun main() {
    val br = System.`in`.bufferedReader()

    val s = br.readLine()
    var t = br.readLine()

    while (s != t) {
        if (t.isEmpty()) {
            println("0")
            return
        }

        val last = t.last()
        if (last == 'A') {
            t = t.substring(0, t.length - 1)
        } else if (last == 'B') {
            t = t.substring(0, t.length - 1).reversed()
        }
    }
    println("1")
}