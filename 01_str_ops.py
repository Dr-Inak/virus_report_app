#Virus Tracking Report | 2016

report_title = "The Umbra Magna"
report_writer = "JACK KLEIN"

virus_name = "Umbra Magna"
virus_detector = "Dr Mustapha INAK"
virus_detection_year = 2000
virus_origin = "Morocco"

virus_date_i = 2002
virus_date_f = 2026

vaccine_invention_date = 2025
vaccine_inventor = "Dr Mustapha INAK"

virus_status = f"The virus {virus_name} appeared first in {virus_origin} in {virus_date_i}, it was detected by {virus_detector} in {virus_detection_year}, a vaccine was invented by {vaccine_inventor} in {vaccine_invention_date}, the virus lasted {virus_date_f - virus_date_i} years." 

print(report_title.upper())
print(report_writer.lower())

replaced_report = virus_status.replace('Umbra', 'Tenebrae')

print(replaced_report)
