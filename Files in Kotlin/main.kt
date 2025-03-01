
import kotlin.random.Random

fun main(args: Array<String>) {
    var continuaIlGioco = true

    while (continuaIlGioco) {
        var continuaIlProgramma = true
        // Imposto il colore giallo per il menu:
        println("\u001B[31m")
        println()
        println("SCEGLI IL LIVELLO DI DIFFICOLTÀ DEL GIOCO:")
        println("-------------------------------------")
        println("0: ESCI DAL PROGRAMMA")
        println("1: UNITA'      (NUMERI DA 1 A 9)")
        println("2: DECINE      (NUMERI DA 10 a 99)")
        println("3: CENTINAIA   (NUMERI DA 100 a 999)")
        println("4: MIGLIAIA    (NUMERI DA 1000 a 3999)")
        println("-------------------------------------")
        print(">>> ")

        var input1 = readLine()!!
        var livello = input1.toInt()

        if (livello == 0) {
            println()
            println("GRAZIE AVER GIOCATO A QUESTO FANTASTICO GIOCO!")
            println()
            continuaIlGioco = false
            continuaIlProgramma = false
        }

        while (continuaIlProgramma) {
            var numeroSorteggiato = when (livello) {
                1 -> Random.nextInt(1, 10)
                2 -> Random.nextInt(10, 100)
                3 -> Random.nextInt(100, 1000)
                4 -> Random.nextInt(1000, 4000)
                else -> 10
            }

            // imposto il colore ciano per il quiz
            println("\u001B[36m")
            println()
            println("==================================================")
            println("TRASCRIVI IN NUMERI ROMANI IL SEGUENTE NUMERO: $numeroSorteggiato          [SCRIVI \u001B[31m0\u001B[36m PER TORNARE AL MENU]")
            var input2 = readLine()!!
            var numeroTrascritto = input2.toString().uppercase()

            if (numeroTrascritto == "0")
                continuaIlProgramma = false

            //var numeroSorteggiato = input.toInt()
            if ((numeroSorteggiato > 0) && (numeroSorteggiato <= 3999)) {
                var numeroRomano = trasformaNumero(numeroSorteggiato)
                if (numeroTrascritto == numeroRomano.toString()) {
                    println("COMPLIMENTI, HAI TRASCRITTO MOLTO BENE IL NUMERO!")
                    println("==================================================")
                    println()
                } else if (numeroTrascritto == "0") {
                    println("\n\n")
                    continuaIlProgramma = false
                }
                else {
                    println("\u001B[31mATTENZIONE, IN NUMERI ROMANI $numeroSorteggiato SI SCRIVE COSI': $numeroRomano\u001B[36m")
                    println("==================================================")
                    println()
                }
            } else {
                println("IL NUMERO SORTEGGIATO DEVE ESSERE COMPRESO FRA 1 E 3999")
            }
        }
    }
}

fun trasformaNumero(num : Int) : String {
    var unit = 0
    var decine = 0
    var centinaia = 0
    var migliaia = 0

    var numeroRomano = NumeriRomani()

    var migliaiaRomane = ""
    var centinaiaRomane = ""
    var decineRomane = ""
    var unitRomane = ""



    if (num > 999) {
        migliaia = num / 1000
        // mi occupo delle centinaia
        centinaia = num - (migliaia * 1000)
        centinaia = centinaia / 100
        // mi occupo delle decine
        decine = num - (migliaia * 1000) - (centinaia * 100)
        decine = decine / 10
        // mi occupo delle unità
        unit = num - (migliaia * 1000) - (centinaia * 100) - (decine * 10)

        migliaiaRomane = numeroRomano.migliaia[migliaia - 1]
        if (centinaia != 0)
            centinaiaRomane = numeroRomano.centinaia[centinaia - 1]
        if (decine != 0)
            decineRomane = numeroRomano.decine[decine - 1]
        if (unit != 0)
            unitRomane = numeroRomano.unit[unit - 1]
    } else if ((num >= 100) && (num <= 999)) {
        centinaia = num / 100
        // mi occupo delle decine
        decine = num - (centinaia * 100)
        decine = decine / 10
        // mi occupo delle unità
        unit = num - (centinaia * 100) - (decine * 10)


        centinaiaRomane = numeroRomano.centinaia[centinaia - 1]
        if (decine != 0)
            decineRomane = numeroRomano.decine[decine - 1]
        if (unit != 0)
            unitRomane = numeroRomano.unit[unit - 1]
    } else if ((num >= 10) && (num <= 99)) {
        decine = num / 10
        // mi occupo delle unità
        unit = num - (decine * 10)

        decineRomane = numeroRomano.decine[decine - 1]
        if (unit != 0)
            unitRomane = numeroRomano.unit[unit - 1]
    } else {
        unit = num
        if (unit != 0)
            unitRomane = numeroRomano.unit[unit - 1]
        else
            unitRomane = "Il numero inserito non può essere 0"
    }



    var risultato = arrayOf("")

    when (num) {
        in 1..3999  -> risultato = arrayOf(migliaiaRomane, centinaiaRomane, decineRomane, unitRomane)
        in 1..999   -> risultato = arrayOf(centinaiaRomane, decineRomane, unitRomane)
        in 1..99    -> risultato = arrayOf(decineRomane, unitRomane)
        in 1..9     -> risultato = arrayOf(unitRomane)
    }

    // rendo leggibile il contenuto dell'array eliminando le virgole
    return risultato.joinToString("")
}