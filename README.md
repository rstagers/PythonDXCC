# PythonDXCC Files Area 13 Nov 2017

This app is being developed, new feature will be added as time allows!

A lot of logging programs have this capability, some far more, however these programs can be very large and do
things their way.  I wanted a simple application, portable across multiple platforms that can do this simple 
task for me.  If you find it useful by all means use it or modify it for you own use.  
This may morph into a complete simple logger with its operation geared for DX'ing and possible protable operations
with minimal logging, i.e. no callbook lookup, no radio querying.  Just a plain old simple logger, small and cross
platform, ideal for portable or a simpler way of operating.

So far the app integrates LoTW verified ADI file with Country Information from plist file (XML) (http://www.country-files.com)
Allows a Amateur Radio DXCC Awards operator to input a prefix and receive information based on the ARRL's
verification of contacts for DXCC awards.  In an instance you can see if you need the entity you hear for any
DXCC awards.  If you have ARRL DXCC awards for this entity it shows VERIFIED! and the awards you have.  So if you're on 
40m and hear XE2XE (a verified award entity) you can type in XE and it will return Mexico as the entity and show VERIFIED! 
and the awards you currently have verified.  If 40m is not checked... go get em, you need that one! Of course you can also 
have a chat with the other operator just for fun too! Say Mexico has never been verified.. you will see no awards and 
a red NEEDED!  Again go get em, you need this one!  This only applies to ARRL VERIFIED AWARDS not Worked or Confirmed!
Just because you worked the station doesn't mean you will get confirmation and just because you get confirmation (though
QSL card or LoTW) doesn't mean the ARRL will award that contact!  You must apply for the award for the Award file to 
include the contact entity.  To me this is simpler, work them if you NEED them, even if you have worked the entity
before.  You may not get the confirmation or the verification so don't miss the opportunity!

Enhancement in the future..

Currently the app hard codes the ARRL ADIF Verification File, DXCC Entity File and those files have to be 
manually downloaded.  Eventually there will be a section for downloading them automatically if the file is 
not present or after the file reaches a certain age (configurable).  An option to update these files manually
will also be added.


Root Directory Files:
File  PyQtDXCC.py              - (MAIN PROG) This is the main application for this section.  However it will be expanded 
                                 in future to do more things.  Hence the test programs that I have kept in the
                                 archive.                
File DXCCPrefixLookup.ui       - (DATA) QtCreator file for UI (Data Used)
File DXCC_QSLs_20171109_184150 - (DATA) This file is downloaded from the ARRL Log Book of the World (LoTW).
                                 It contains all verified and award connected contacts in ADIF format.
                                 (Data Used)
File  PrefixLookupClass.py     - (PROG TEST) Simple console version of GUI app.  Not completed but works.
File  python_adi.py            - (TEST) Simple parser for testing that I used to generate a text file of aggregate entities.
File  regexp.py                - (TEST) Testing out a regular expression for parsing DXCC Cluster telnet data.
File  TelnetCluster.py         - (TEST) Simple console telnet connection and output.  Lookup to be integrated in future app.
File DXCCPrefixLookup.py       - (TEST) Converted UI file to python code only for reference not used.
File Screenshot.png            - (INFO) A screenshot of the application.
File DXCC200.png               - (INFO) Not used just a screenshot of my DXCC finally reaching 200 entities.

Directory cty_plist Files:
  File  cty.plist         - (DATA) File that contains DXCC entity information.  
                            Thanks to Jim Reisert AD1C for keeping this information current! 
                            Location for download: http://www.country-files.com
                            (Data Used)
  File  history.txt       - What has changed, adds deletes and modifications to DXCC entities.
  File  readme.txt        - Self explanatory!
  
  




