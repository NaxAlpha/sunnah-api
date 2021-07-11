# sunnah-api
Lightweight Python wrapper for APIs of https://sunnah.com with full type annotations. 

## Get Started

Install the package as following:

```bash
pip install sunnah-api
```

Or you can get it directly from github

```bash
pip install git+https://github.com/NaxAlpha/sunnah-api
```

## Examples

Following is the list of examples for what you can do with this library:

### Initialize API Adaptor

The main component of this library is `ApiAdaptor` which you can use to call the APIs. Here is how to setup/initialize the adaptor:

```python
from sunnah_api import ApiAdaptor

api = ApiAdaptor(
    api_key="<your-api-key>", 
    wait_between_all_requests=0.5,
)
```

In order to run this example, you will need to [get an API key](https://sunnah.com/developers) from the sunnah.com team. 

Here the parameter `wait_between_all_requests` is for all the functions which send multiple requests to the API endpoint. It waits this many seconds between two requests. It is only applicable to `get_all_*` APIs as those APIs send repeated requests, other APIs only send one request when called.

### Get All collections

You can get list of all the available collections as following:

```python
cols = api.get_all_collections()
print(cols[0])
```

**Output:**

```python
Collection(
    name="bukhari",
    hasBooks=True,
    hasChapters=True,
    collection=[
        CollectionInfo(
            lang=<LangInfo.en: 'en'>,
            title="Sahih al-Bukhari",
            shortIntro="Sahih al-Bukhari is a collection of hadith compiled by Imam Muhammad al-Bukhari (d. 256 AH/870 AD) (rahimahullah).\r\n\r\nHis collection is recognized by the overwhelming majority of the Muslim world to be the most authentic collection of reports of the <i>Sunnah</i> of the Prophet Muhammad (ﷺ). It contains over 7500 hadith (with repetitions) in 97 books.\r\n\r\nThe translation provided here is by Dr. M. Muhsin Khan.",
        ),
        CollectionInfo(
            lang=<LangInfo.ar: 'ar'>,
            title="صحيح البخاري",
            shortIntro="Sahih al-Bukhari is a collection of hadith compiled by Imam Muhammad al-Bukhari (d. 256 AH/870 AD) (rahimahullah).\r\n\r\nHis collection is recognized by the overwhelming majority of the Muslim world to be the most authentic collection of reports of the <i>Sunnah</i> of the Prophet Muhammad (ﷺ). It contains over 7500 hadith (with repetitions) in 97 books.\r\n\r\nThe translation provided here is by Dr. M. Muhsin Khan.",
        ),
    ],
    totalHadith=7291,
    totalAvailableHadith=7277,
)

```

All the returned responses are *dataclasses*. You can access their elements as they are objects like for above example, you can get total number of hadith as `cols[0].totalHadith`. 

### Get Books of a collection

You can get the list of books of a collection as following:

```python
# Get all collections
cols = api.get_all_collections()
bukhari = cols[0]

# Get books of Sahih-al-Bukhari
books = api.get_all_books(
    collection_name=bukhari.name
)
print(books[0])
```

**Output:**

```python
Book(
    bookNumber=1,
    book=[
        BookInfo(lang=<LangInfo.en: 'en'>, name="Revelation"),
        BookInfo(lang=<LangInfo.ar: 'ar'>, name="كتاب بدء الوحى "),
    ],
    hadithStartNumber=1,
    hadithEndNumber=7,
    numberOfHadith=7,
)
```

You can get arabic info of the book as following:

```python
book_info = books[0].ar_book
print(ar_book.name)  

# Output: كتاب بدء الوحى
```

### Get All Hadith of a book

You can get all the hadith of a book as following:

```python
# Get all collections
cols = api.get_all_collections()
bukhari = cols[0]

# Get books of Sahih-al-Bukhari
books = api.get_all_books(
    collection_name=bukhari.name
)
book_of_revelation = books[0]

# Get all hadith of the book
ahadith = api.get_all_hadith(
    collection_name=bukhari.name,
    book_number=book_of_revelation.bookNumber,
)
print(ahadith[0])
```

**Output:**

```python

Hadith(
    collection="bukhari",
    bookNumber=1,
    chapterId=1.0,
    hadithNumber=1,
    hadith=[
        HadithInfo(
            lang=<LangInfo.en: 'en'>,
            chapterNumber=1,
            chapterTitle="How the Divine Revelation started being revealed to Allah's Messenger",
            urn=10,
            body="<p>Narrated 'Umar bin Al-Khattab:\n</p>\n<p>\n I heard Allah's Messenger (ﷺ) saying, \"The reward of deeds depends upon the \n intentions and every person will get the reward according to what he \n has intended. So whoever emigrated for worldly benefits or for a woman\n to marry, his emigration was for what he emigrated for.\"\n</p>",
            grades=[HadithGrade(graded_by=None, grade="Sahih")],
        ),
        HadithInfo(
            lang=<LangInfo.ar: 'ar'>,
            chapterNumber=1,
            chapterTitle="باب كَيْفَ كَانَ بَدْءُ الْوَحْىِ إِلَى رَسُولِ اللَّهِ صلى الله عليه وسلم",
            urn=100010,
            body='<p>[prematn]حَدَّثَنَا[narrator id="4698" tooltip="عبد الله بن الزبير بن عيسى بن عبيد الله بن أسامة بن عبد الله بن حميد بن زهير بن الحارث بن أسد بن عبد العزى"] الْحُمَيْدِيُّ عَبْدُ اللَّهِ بْنُ الزُّبَيْرِ [/narrator]، قَالَ : حَدَّثَنَا[narrator id="3443" tooltip="سفيان بن عيينة بن ميمون"] سُفْيَانُ [/narrator]، قَالَ : حَدَّثَنَا[narrator id="8272" tooltip="يحيى بن سعيد بن قيس بن عمرو بن سهل بن ثعلبة بن الحارث بن زيد بن ثعلبة بن غنم بن مالك بن النجار"] يَحْيَى بْنُ سَعِيدٍ الْأَنْصَارِيُّ [/narrator]، قَالَ : أَخْبَرَنِي[narrator id="6796" tooltip="محمد بن إبراهيم بن الحارث بن خالد بن صخر بن عامر بن كعب بن سعد بن تيم بن مرة"] مُحَمَّدُ بْنُ إِبْرَاهِيمَ التَّيْمِيُّ [/narrator]، أَنَّهُ سَمِعَ[narrator id="5719" tooltip="علقمة بن وقاص بن محصن بن كلدة بن عبد ياليل"] عَلْقَمَةَ بْنَ وَقَّاصٍ اللَّيْثِيَّ [/narrator]، يَقُولُ : سَمِعْتُ[narrator id="5913" tooltip="عمر بن الخطاب بن نفيل بن عبد العزى بن رياح بن عبد الله بن قرط بن رزاح بن عدي بن كعب"] عُمَرَ بْنَ الْخَطَّابِ [/narrator] رَضِيَ اللَّهُ عَنْهُ عَلَى الْمِنْبَرِ، قَالَ : سَمِعْتُ رَسُولَ اللَّهِ صَلَّى اللَّهُ عَلَيْهِ وَسَلَّمَ، يَقُولُ : "[/prematn]\n[matn]إِنَّمَا الْأَعْمَالُ بِالنِّيَّاتِ، وَإِنَّمَا لِكُلِّ امْرِئٍ مَا نَوَى، فَمَنْ كَانَتْ هِجْرَتُهُ إِلَى دُنْيَا يُصِيبُهَا أَوْ إِلَى امْرَأَةٍ يَنْكِحُهَا، فَهِجْرَتُهُ إِلَى مَا هَاجَرَ إِلَيْهِ "[/matn]</p>',
            grades=[HadithGrade(graded_by="", grade="صحيح")],
        ),
    ],
)
```

You can get the english text of hadith as following:

```python
first_hadith = ahadith[0].en_hadith
print(first_hadith.body)
```

**Output:**

```html
<p>Narrated 'Umar bin Al-Khattab:
</p>
<p>
 I heard Allah's Messenger (ﷺ) saying, "The reward of deeds depends upon the 
 intentions and every person will get the reward according to what he 
 has intended. So whoever emigrated for worldly benefits or for a woman
 to marry, his emigration was for what he emigrated for."
</p>
```
