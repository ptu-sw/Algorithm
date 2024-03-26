package com.yunseong.algorithm.greedy

fun main() {
    val br = System.`in`.bufferedReader()
    val tc = br.readLine().toInt()
    val builder = StringBuilder()

    repeat(tc) {
        val n = br.readLine().toInt()
        val list = Array(n) {
            0 to 0
        }
        var index = 1

        repeat(n) {
            val (p, i) = br.readLine().split(" ").map { it.toInt() }
            list[it] = p to i
        }

        list.sortBy { it.first }

        var pivot = list[0].second

        for (i in 1 until list.size) {
            val compare = list[i].second

            if (pivot > compare) {
                index++
                pivot = compare
            }
        }
        builder.append(index).append("\n")
    }

    print(builder)
}