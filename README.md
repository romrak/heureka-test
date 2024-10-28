# heureka-test
Implementation of Test for Product Catalogue Team @ Heureka

# Assignment
Available at https://docs.google.com/document/d/18tnyphLEdKTGn2r__7gGhGOgk7_iZq-gdlcptkfNIYA/edit?tab=t.0

# Analysis
It's not exactly specified what are data, if they change over time etc.
So I made some assumptions and decisions.

## Producer data
They are coming in infinite loop. They don't change over time. 

There are 7 offers.

There are also categories. However, I don't think we need them to fulfill the assignment. 

## API matches
It returns either a list of matches or nothing with code 404.

## Matched Offers
Looking at matched offers we can see that there are only language mutations.

Assignment description says that we must save merged parameters. 
So I assume we are making the merging system of parameters, we don't have to store name or description (which are probably stored elsewhere).

We will store parameter values as a list (set), since they can differ.

Here are all the matched offers.
### Harry Potter 1
```json
{
    "id": "29e0b669-a670-476b-808a-e21a449d1c0f",
    "category": "Books",
    "name": "Harry Potter a Kámen mudrců - J. K. Rowlingová",
    "description": "Harryho Pottera Vám zajisté nemusím představovat, neboť je to taková knižní legenda a téměř už i klasika. Pro mnoho z Vás je to dokonce kniha, na které jste vyrostli.\n\nKdyž byl Harrymu jeden rok, tak přišel o své rodiče. Ten - o kom se nemluví - zavraždil Harryho rodiče a chtěl zabít i jeho samotného, jenže nějakým zázrakem chlapec přežil a na čele mu zůstala jizva v podobě blesku. Chlapec deset let vyrůstal u strýce a tety Dursleyových a jejich syna Dudleyho. Bylo by pravdě podobné, že když se jedná o přímé příbuzné, že bude o chlapce postaráno dobře, ale Harry doslova trpěl a je div, že z něho vyrostl bystrý a hodný chlapec.\n\nNezná svou minulost, nezná své rodiče, bylo mu jen řečeno, že zemřeli při nehodě. Neví z jaké rodiny pochází a ani neví, co mu bylo dáno do vínku. Ví, že je jiný, že se občas stanou zvláštní věci, ale ani ve snu by ho nenapadlo, že v den svých jedenáctých narozenin zjistí pravdu, která mu navždy změní život. A i přesto, že se teta se strýcem snaží všemožně zabránit tomu, aby se Harry dozvěděl skutečnost o sobě i svých rodičích, se jednoho dne objeví sova se zvláštním dopisem z Bradavic - ze školy čar a kouzel, jejímž ředitelem je Albus Brumbál.\n\nK příběhu asi netřeba více dodávat, kdo by jej neznal? Věřím, že není nikdo, i třeba těch, kteří knihy nečetli a kdo by nevěděl kdo je Harry Potter. Víte, že letos je to dvacet let od vydání první knihy od skvělé autorky J.K. Rowling?",
    "parameters": {
      "author": "J.K. Rowling",
      "genre": "for children",
      "publisher": "Albatros",
      "number of pages": "336",
      "year": "2017",
      "language": "czech"
    }
  }
```
```json
{
    "id": "ed87340d-3703-45b1-a7f8-5fa7d22fc9e9",
    "category": "Books",
    "name": "Harry Potter és a bölcsek köve (2016)",
    "description": "A \"Harry Potter és a bölcsek köve\" c. könyvről részletesen:\nHarry Potter tizenegy éves, amikor megtudja, hogy ő bizony varázslónak született, és felvételt nyert a Roxfort Boszorkány- és Varázslóképző Szakiskolába.",
    "parameters": {
      "number of pages": "336",
      "weight": "380",
      "publisher": "Fizika"
    }
  }
```

### Lego Hogwarts
```json
{
    "id": "631aa5a8-9b5d-4ae2-945a-00a0a539b101",
    "category": "LEGO",
    "name": "LEGO Harry Potter Grad Bradavičarka (71043)",
    "description": "Dobrodošli na ikonski LEGO® Harry Potter™ 71043 Grad Bradavičarkš Sestavi in razstavi podrobno izdelani model LEGO® iz več kot 6000 koščkov. Odkrij podrobno okrašene sobane, stolpe in učilnice, pa tudi veliko skritih lastnosti in prizorov iz filmov o Harryju Potterju. Grad poseli s 27 mikrofigurami, med katerimi so tudi Harry, Hermiona in Ron. Tu je tudi veliko ikonskih pripomočkov in artefaktov. Čarovniško izkušnjo izpopolni s Hagridovo kočo in vrbo mesarico.",
    "parameters": {
      "manufacturer": "LEGO",
      "minimum age": 16,
      "set": "Harry Potter"
    }
  }
```
```json
{
    "id": "38495bd1-afe9-4cd0-bf9d-eca162e75542",
    "category": "LEGO",
    "name": "LEGO Harry Potter 71043 Bradavický hrad",
    "description": "Ponořte se do tajemného světa čar a kouzel a podívejte se do kouzelnické školy v Bradavicích. Oblíbené postavy Harryho, Rona a Hermiony zde potkají spoustu přátel a členů profesorského sboru, ale i nepřátel, kteří se přiklonili na stranu zlého kouzelníka Lorda Voldemorta. Pokud mají bitvu vyhrát, musí se naučit ještě hodně kouzel, lektvarů a dalších čarodějnických dovedností. Na své cestě se potkají s mnoha zajímavými tvory. Celá škola i její okolí jsou do detailu propracovány, a tak jistě poznáte spoustu známých míst. Pohyblivé schodiště, hostina ve velkém sále, Nebelvírská kolej i učebny - vše je tak, jak to znáte z filmů kouzelnické ságy. Stavebnice je kompatibilní s dalšími z řady, takže můžete svůj svět stále rozšiřovat.",
    "parameters": {
      "minimum age": 16,
      "set": "Harry Potter",
      "number of pieces": 6020
    }
  }
```
```json
{
    "id": "feaa400a-d304-4f55-b045-51b1daec8e0c",
    "category": "LEGO",
    "name": "LEGO Harry Potter - Roxfort (71043)",
    "description": "Üdvözlünk az egyedülálló LEGO® Harry Potter™ 71043 Roxfort kastélyban! Építsd meg és állítsd ki ezt a részletesen kidolgozott mini LEGO® Harry Potter TM Roxfort kastély modellt, mely több mint 6000 elemből áll! Fedezd fel a rendkívül részletesen kidolgozott kamrákat, tornyokat és tantermeket, valamint számos rejtett funkciót és a Harry Potter filmek jeleneteit is! Népesítsd be a kastélyt 27 mikrofigurával, melyek között Harry, Hermione és Ron figurája is szerepel, továbbá rengeteg jellegzetes kiegészítő és tárgy lenyűgöző választéka is vár rád! A varázslatos építési élményt pedig kiegészítheted Hagrid kunyhójával és a Fúriafűzzel.\n\n\n\nÍgy is ismerheti: Harry Potter Roxfort 71043, HarryPotterRoxfort71043, Harry Potter Roxfort (71043), HarryPotter-Roxfort71043, Harry Potter - Roxfort ( 71043)",
    "parameters": {
      "minimum age": 16,
      "set": "Harry Potter",
      "number of pieces": 6020
    }
  }
```

### Minecraft
```json
{
    "id": "0a10d511-6a65-444d-9628-3c6993ba7dbd",
    "category": "Tabletop games",
    "name": "Ravensburger Minecraft",
    "description": "Tuto strategickou stolní hru určenou nejen pro všechny fanoušky Minecraftu mohou hrát dva až čtyři hráči ve věku od 10 let. Balení hry obsahuje 64 dřevěných bloků, 64 stavebních karet a karet s příšerami, 36 kartiček se zbraněmi, 4 herní plány, 4 herní žetony, 4 hráčské skiny, 4 stojánky na figurky, 12 přehledových karet, 1 podložku pod bloky, 1 konstrukční oporu a návod.",
    "parameters": {
      "genre": "strategic",
      "publisher": "Ravensburger",
      "age_from": "10",
      "number_of_players": "2-4",
      "year": "2019",
      "game_length": "30m"
    }
  }
```

### Harry Potter 5
API returns 404 code
```json
{
    "id": "94fe7882-dd86-424f-b487-706b174d8d4e",
    "category": "Books",
    "name": "Harry Potter a Fénixův řád - Rowlingová Joanne Kathleen",
    "description": "Albatros Harry Potter a Fénixův řád (2017)\n\nČeká na tebe napínavé čtení o kouzelníkovi Harry Potterovi, který bojuje se zlem a proti tomu o kom se nesmí mluvit. Po jeho boku, ale stojí přátelé Ron Weasley a Hermiona Grangerová, kteří mu zásadně pomáhají.\n\nDo Bradavic přišly temné časy. Po útoku mozkomorů na bratrance Dudleyho Harry ví, že Voldemort udělá cokoli, jen aby ho našel. Mnozí jeho návrat popírají, ale Harry přesto není sám: na Grimmauldově náměstí se schází tajný řád, který chce bojovat proti temným silám. Harry se musí od profesora Snapea naučit, jak se chránit před Voldemortovými útoky na jeho duši. Jenže Pán zla je den ode dne silnější a Harrymu dochází čas…\nAutor: J. K. Rowlingová\nPřeklad: Vladimír Medek\nVěk: 9+\nPočet stran: 800\nJazyk: čeština\nRozměry: 14 x 20,5 cm\nZemě původu: ČR",
    "parameters": {
      "author": "J.K. Rowling",
      "genre": "for children",
      "publisher": "Albatros",
      "number of pages": "800",
      "year": "2018",
      "language": "czech"
    }
  }
```

# Solution

## Assumptions
Solution is based on various assumptions:

- Offers can change over time
- There might be many offers (up to a million)
- Matching doesn't change (that would complicate things a lot)
- There are not many different offers for one product

## Procedure

The heart of the service is in making the merged parameters. 

It can receive offer. It will load current Product from repository, once the offer is received. It will call matching API simultaneously.

Products are specified by a set of ids.

### Key concepts
Always save merged parameters and offer parameters. So we can update the Product when there is a new offer coming.

Parameters difference is calculated from merged parameters.

In order to support update of Product by changed offer, we must save all the parameters of all matched offers.

### New product scenario
It will create new Product, when there is no Product yet (it is very first offer for example).

It saves all matching ids, all parameters and offer parameters. Diffs for offer will be empty.

### Update product with new offer scenario
It will update a Product, when there is already a Product.

Matching ids stay the same. Parameters of offers are merged. Difference for each offer is recalculated. Everything is saved to the same Product.

### Update product with updated offer scenario
It will update a Product, when there is already a Product.

Basically it's the same as previous scenario. There will be just different parameters for given offer.

## Technologies

For saving the Products I choose MongoDB. We don't need many relations, but we need to save many objects (documents).
MongoDB is very good for that. However, it has a limitation in document size. I assume that all offers can fit into one document.

I also considered ElasticSearch. That would be better in the case of searching, however that is probably not a case.

# Further improvements

It might happen that matching IDs will change over time. 
In that case we would need to handle various situations.
It would be probably just enough to recalculate all affected Products.
I'm not going to investigate this scenario further, it would require deeper investigation.

It might happen that there will be many offers in one Product and MongoDB cannot save it into one document.
In that case we can save each offer in different document and Products wouldn't contain offers.

It might happen that matching API is not available.
In that case we have various options. Stop processing offers until matching API is available, or save offers and process them later.
It would depend on many details. Understanding the data is very important.