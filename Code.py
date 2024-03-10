import numpy as np
import matplotlib.pyplot as plt
import csv
import os


#Definin the file paths
Audio_file              = "Måling\Måling_av_lydfil.csv"
frequency_response_file = "Måling\Måling_av_frekvensrespons.csv"
Spectrum_narrow         = "Måling\Måling_i_spectrum_(liten_område).csv"
Spectrum_wide           = "Måling\Måling_i_spectrum_(stort_område).csv"

#Defining function to convert csv file to lists.
def file_to_lists(file, freq_column, magnetude_column):
    freq_list=[]
    magnetude_list=[]
    n=0
    with open(file, 'r') as file:
        data=csv.reader(file)
        for row in data:
            
            if len(row)==0:
                continue
            elif not (row[0][0].isdigit()):

                continue
                
            
            freq_list.append(float(row[freq_column]))
            magnetude_list.append(float(row[magnetude_column]))
    return freq_list, magnetude_list

#Applying the function file_to_lists to the csv files
freq_audio, magnetude_audio = file_to_lists(Audio_file, 0,1)
freq_freq_response, magnetude_freq_response = file_to_lists(frequency_response_file,0,2)
freq_freq_spectnarrow1, magnetude_freq_spectnarrow1 = file_to_lists(Spectrum_narrow ,0,1)
freq_freq_spectnarrow2, magnetude_freq_spectnarrow2 = file_to_lists(Spectrum_narrow ,0,3)
freq_freq_spectwide1, magnetude_freq_spectwide1 = file_to_lists(Spectrum_wide ,0,1)
freq_freq_spectwide2, magnetude_freq_spectwide2 = file_to_lists(Spectrum_wide ,0,3)

#Creating a folder
folder_path = 'Graphs'
os.makedirs(folder_path, exist_ok=True)

#plotting and saving the graphs
plt.figure()
plt.plot(freq_audio, magnetude_audio)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude [dB]')
plt.savefig('Graphs\Audio.png')
print("Frequency of the top in the audio file:", round(freq_audio[magnetude_audio.index(max(magnetude_audio))],1))

plt.figure()
plt.semilogx(freq_freq_response, magnetude_freq_response)
plt.title('Amplitude response')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude [dB]')
plt.savefig('Graphs\Frequency_response.png')
print("Resonance frequency:", round(freq_freq_response[magnetude_freq_response.index(min(magnetude_freq_response))],1))

plt.figure()
plt.plot(freq_freq_spectnarrow1[2000:], magnetude_freq_spectnarrow1[2000:])
plt.plot(freq_freq_spectnarrow2[2000:], magnetude_freq_spectnarrow2[2000:])
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude [dB]')
plt.title('Narrow Spectrum')
plt.legend(['Unfiltered', 'Filtered'])
plt.savefig('Graphs\Spectrum_narrow.png')

plt.figure()
plt.plot(freq_freq_spectwide1, magnetude_freq_spectwide1)
plt.plot(freq_freq_spectwide2, magnetude_freq_spectwide2)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude [dB]')
plt.title('Wide Spectrum')
plt.legend(['Unfiltered', 'Filtered'])
plt.savefig('Graphs\Spectrum_wide.png')

# plt.show()