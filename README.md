Kursinio darbo metu buvo kūriamas 2d formato žaidimas su Sonic veikejo skinu, kurio užduotis peršokti artėjančią kliutį. Tačiau jeigu nepavyksta, žaidimas baigiasi ir išduoda užraša "Game over". Programa paleidžiama su dešiniame kampe esančia strelite Visual studio code programoje. Žaidėjo pagrindinis valdymo migtukas yra SPACE, kuris leidžia peršokinėti kliutis.

Kodo metu buvo panaudotos klases, funkcijos, enkapsuliacija ir paveldejimas. 

Buvo bandyta pritaikyti unit testa, kuris tikritu ar Sonic ir kliučių objektas yra sukurtas ir yra priskirtas prie savo klasės egzemplioriaus. Taip pat sukurtas txt failas į kuri inputinasi zaidimo veikimo laikas, kas kart kai jus baigiate žaisti.

„GameObject“ klasė: ši klasė yra bendras žaidimo objektas, suteikiantis ypatybes pasiekti jo vaizdo ir stačiakampio atributus. Tai apima bendras funkcijas, reikalingas visiems žaidimo objektams, pavyzdžiui, vaizdų įkėlimą ir jų padėties nustatymą.

Player klase kilusi iš GameObject klasės, žaidėjų klasė atstovauja pagrindiniam žaidimo veikėjui. Jame yra metodas jump_action(), skirtas valdyti žaidėjo šokinėjimo mechaniką, kuris reaguoja į tarpo klavišo paspaudimą. Ši klasė užtikrina inkapsuliavimą ir paveldėjimą paveldėdama iš GameObject .
Priešo klasė: Panašiai kaip žaidėjų klasė, priešų klasė paveldima iš GameObject, kad atstovautų priešiškiems subjektams žaidime. Jis inicijuojamas naudojant skirtingą vaizdą ir padėtį, todėl pateikiamas įvairus žaidimo elementų rinkinys.

Super raktažodis naudojamas bazinės (parent) klasės metodams ir konstruktoriams iškviesti poklasiuose (antrinėse klasėse). Tai leido išvengti kodo dubliavimo ir suteikia lankstumo plečiant klasių funkcionalumą.
Pagrindinė funkcija: funkcija main() inicijuoja Pygame modulį, nustato žaidimo langą, įkelia išteklius ir valdo žaidimo ciklą. Jis tvarko žaidėjo įvestį, atnaujina žaidimo būseną ir atitinkamai atvaizduoja grafiką. Be to, jis įrašo programos vykdymo laiką ir įrašo jį į failą, pavadintą execution_time.txt.

{if name == "main":
 main()} 
Šis kodo blokas paleidžia funkciją game() tik tuo atveju, jei scenarijus vykdomas tiesiogiai. Jei scenarijus importuojamas į kitą failą, funkcija game() nebus iškviesta automatiškai. Tai leidžia kontroliuoti kodo vykdymą ir užkirsti kelią nereikalingam vykdymui importuojant.

Žaidimo pratesimas atrodytu jau su labiau pasunkintais artejančių kliučių atsiradimais už ribų su skirtingais generavimosi intervalais.

Apibendrinat galiu paskyti, kad rašyti kursini darba buvo sunku. Reikejo pasitelti interneto ir Youtube pagalba. Taip pat kursinis ne visiškai pilnai buvo atliktas, nes nebuvo panaudotas polymorfizmas, singletone, decorator, kaip buvau suplanaves, unit testas neveikia ir yra nuojauta, kad nevisiškai gerai pritaikiau išmokta teorija kursinio rašymui. Bet džiugu, kad kodas veikia.

