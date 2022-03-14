from django.test import TestCase
import locale
# Create your tests here.

#convertendo numero para real
faturamento = 1000000000
texto_faturamento = f"{faturamento:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
print(f"o faturamento foi de R${texto_faturamento}")

#definir qual local voce tá
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8') # 'Portuguese_Brazil.1252'

texto_faturamento2 = locale.currency(faturamento, grouping=True, symbol=True)
print(f"O faturamento foi de {texto_faturamento2}")

faturamento2 =1000
bonus = 200 if faturamento2 > 500 else 50
bonus2 = locale.currency(bonus, grouping=True, symbol=True)
print("O faturaemnto é de:", bonus2)