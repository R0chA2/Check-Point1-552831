import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/R0chA2/Check-Point1-552831/main/urls_phishing_checkpoint1.csv')
amostra_df = df.sample(4000, random_state = 123456)

df1 = df[df['phishing'] == 1] # phishing
df0 = df[df['phishing'] == 0] # legítima

mean_value = round(df['length_url'].mean(),2)
print(f"A média da coluna 'UrlLength' é: {mean_value} (Todas URLs)")


mean_value1 = round(df1['length_url'].mean(),2)
print(f"A média da coluna 'UrlLength' é: {mean_value1} (URLs Phishing)")


mean_value0 = round(df0['length_url'].mean(),2)
print(f"A média da coluna 'UrlLength' é: {mean_value0} (URLs Legítima)")


median_value = df['length_url'].median()
print(f"A mediana da coluna 'UrlLength' é: {median_value} (Todas URLs)")


median_value1 = df1['length_url'].median()
print(f"A mediana da coluna 'UrlLength' é: {median_value1} (URLs Phishing)")


median_value0 = df0['length_url'].median()
print(f"A mediana da coluna 'UrlLength' é: {median_value0} (URLs Legítima)")


std_value = round(df['length_url'].std(),2)
print(f"O desvio padrão da coluna 'length_url' é: {std_value} (Todas URLs)")

std_value1 = round(df1['length_url'].std(),2)
print(f"O desvio padrão da coluna 'length_url' é:{std_value1}(URLs Phishing)")

std_value0 = round(df0['length_url'].std(),2)
print(f"O desvio padrão da coluna 'length_url' é:{std_value0} (URLs Legítima)")