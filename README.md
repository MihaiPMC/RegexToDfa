# RegexToDfa

## 📝 Descriere

Un instrument eficient pentru conversia expresiilor regulate în automate finite deterministe (DFA). Acest proiect are atât valoare educațională cât și practică, fiind util pentru înțelegerea teoriei automatelor și a expresiilor regulate.

## 🔄 Procesul de conversie

Conversia de la expresie regulată la DFA se realizează în trei etape principale:

1. **Regex → Expresie Postfix**: Transformă expresia regulată într-o notație postfix pentru procesare mai ușoară.
2. **Expresie Postfix → NFA**: Construiește un automat finit nedeterminist (NFA) folosind algoritmul Thompson.
3. **NFA → DFA**: Transformă NFA-ul în DFA utilizând algoritmul de construcție a subseturilor.

## 🗂️ Structura proiectului

- **src/regex_parser.py**  
  Analizează expresiile regulate, adaugă concatenări explicite și convertește în notație postfix. Implementează algoritmi de parsare și preprocesare a expresiilor.

- **src/postfix_to_nfa.py**  
  Convertește expresia postfix într-un NFA folosind algoritmi bazați pe stive pentru gestionarea operațiilor.

- **src/nfa_to_dfa.py**  
  Implementează algoritmul de construcție a subseturilor pentru transformarea NFA în DFA, optimizând tranziții și stări.

- **src/main.py**  
  Coordonează întregul proces de conversie și validare a rezultatelor cu cazurile de test.

- **tests/testcase.json**  
  Conține expresii regulate de test și șiruri corespunzătoare de validare pentru verificarea corectitudinii implementării.

## 🚀 Instalare și utilizare

### Cerințe

- Python 3.6 sau mai nou

### Pași de rulare

1. Clonați repository-ul:
   ```bash
   git clone https://github.com/MihaiPMC/RegexToDfa.git
   cd RegexToDfa
   ```

2. Rulați aplicația:
   ```bash
   python src/main.py
   ```

### Ce se întâmplă atunci când rulați aplicația

- Se parsează cazurile de test din `tests/testcase.json`
- Fiecare expresie regulată este convertită în postfix
- Se construiește un NFA pentru fiecare expresie
- NFA-ul este transformat în DFA
- Se afișează stările și tranzițiile NFA și DFA
- Se rulează teste pe DFA și se afișează rezultatele

## 📋 Exemple

Iată un exemplu simplu de conversie a expresiei regulate `a(b|c)*` în DFA:

1. Expresia cu concatenare explicită: `a·(b|c)*`
2. Notația postfix: `abc|·*·`
3. DFA rezultat va recunoaște toate șirurile care încep cu 'a' și sunt urmate de orice număr de 'b' sau 'c'

## 🔧 Contribuții

Contribuțiile sunt binevenite! Iată câteva modalități prin care puteți contribui:

- Îmbunătățirea algoritmilor existenți
- Adăugarea de noi caracteristici (cum ar fi vizualizarea DFA)
- Extinderea suportului pentru mai multe operații regex
- Raportarea problemelor sau contribuirea la documentație

## 📝 Note

- Proiectul acceptă operatorii de bază: concatenare, alternare (`|`), repetare (`*`), una sau mai multe repetiții (`+`), și opțional (`?`)
- DFA-ul generat poate fi utilizat pentru a verifica dacă un șir de caractere se potrivește cu expresia regulată

## 📄 Licență

Acest proiect este furnizat "așa cum este" fără nicio garanție.
