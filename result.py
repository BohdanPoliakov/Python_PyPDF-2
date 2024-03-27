import PyPDF2
import pathlib
import csv

try:
    adres = pathlib.Path("invoices")
    all_fails = list(adres.glob("*.pdf"))
    all_tarifs = 0
    all_records = 0
    file = input()

    if file in ("invoices/invoice1.pdf", "invoices/invoice2.pdf"):
        pdf_file = PyPDF2.PdfReader(open(file, "rb"))
        number_of_pages = len(pdf_file.pages)
        page1 = pdf_file.pages[0]
        page2 = pdf_file.pages[1]

        text1 = page1.extract_text()
        text2 = page2.extract_text()

        pos1 = text2.find("Apkalpošanas maksa")
        summa = text2[pos1 - 7:pos1].rstrip()
        summa = float(summa.replace(",", "."))

        pos1 = text2.find("Apjoms Mērv. Cena,")
        per = text2[pos1 - 23:pos1]

        pos1 = text1.find("Elektroenerģijas patēriņš kopā")
        pos2 = text1.find("kWh")
        the_amount = text1[pos1 + 32:pos2].rstrip()
        the_amount = the_amount.replace(",", ".")
        the_amount = float(el_daudzums.replace(" ", ""))

        pos1 = text2.find("kWh")
        cena_par_kwh = text2[pos1 + 4:pos1 + 10]

        year = str(per[6:10])
        month = str(per[3:5])

        with open("nordpool.csv", "r") as f:
            next(f)
            row = []
            for line in f:
                row = line.rstrip().split(",")
                if str(year) + "-" + str(month) == row[0][:7]:
                    tarifs = row[2]
                    all_records += 1
                    kopa_tarifs += float(tarifs)

        average = float(all_tarifs / all_records)
        average = round(average, 3)
        price_per_kwh = float(price_per_kwh.replace(",", "."))
        round_average = average * the_amount

        result = (float(summ) - round_average)
        result = round(result, 1)

        print(result)
    else:
        print("0")
except Exception as e:
    print(f"An error occurred: {e}")