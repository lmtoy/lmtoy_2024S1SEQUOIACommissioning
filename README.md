# 2024S1SEQUOIACommissioning 


Commissioning work for SEQ.  Started 1-dec-2023 on the generator. Some 1MM is also mentioned here,
as the Ps mode in SEQ and 1MM are similar. No testing of 1MM/Bs mode done yet.

Summary:

1. Map fine (110407) but bank=1 has bad beams 0,4, and script generator needs to run 3 times
2. Bs fine (110401)
3. Ps fine (110362, 110354, 110416 science)
4. 1MM/Ps ok (110433)


#  SEQ Map

So far only one map of the first night was good.

- 110407 - long 45 min 2IF integration on MonR2 in narrow band 200MHz mode . Lots of beam issues, especially in bank 1
           bank1 has beams 0,4 that need to be removed in order for pipeline not to crash, and later bank0 needs to be
	   re-inspected since beams 0,4 are ok for it.


     SLpipeline.sh obsnum=110407 dv=10 dw=40 vlsr=10  pix_list=-0,4 restart=1  
     SLpipeline.sh obsnum=110407 b_order=1 bank=0 pix_list=-2,4,6,11,13             
     SLpipeline.sh obsnum=110407 b_order=5 bank=1 pix_list=-0,1,2,3,4,6,11,13

     SLpipeline.sh obsnum=110407 dv=100 dw=100 vlsr=-100  pix_list=-0,4 restart=1

- 111259 (march 2024) - 20 min integration on IRC+10216 , both IF.  Much improved, still beam 13 bad.

      SLpipeline.sh obsnum=111259 meta=0 restart=1 otf_cal=1
      SLpipeline.sh obsnum=111259 bank=0 pix_list=-3,13         # 12CO
      SLpipeline.sh obsnum=111259 bank=1 pix_list=-1,13,14,15   # 13CO


# SEQ Ps


- 110362 - IRC+10123 

       SLpipeline.sh obsnum=110362    # IRC+10123    restfreq=86.243442,86.243442 (SiO twice accidentally)
       # uses seqps_pipeline.sh
       
       QAC_STATS: IRC+10123_110362__0.txt 78.0381 77.5216 -204.884 1040.29 153499 0.85978 1903
       QAC_STATS: IRC+10123_110362__1.txt 60.2893 79.1958 -196.641 1030.59 120230 0.744827 1893

- 110354 - Ori-KL 

       SLpipeline.sh obsnum=110354    # Ori-KL       restfreq=86.243442,88.631847 (SiO and HCN)

       QAC_STATS: Ori-KL_110354__0.txt 850.178 540.842 -1102.7 172398 2.7311e+07 0.993566 7275
       QAC_STATS: Ori-KL_110354__1.txt 650.052 588.132 -12798.8 29476.1 1.34744e+07 0.950286 7330

     The 86GHz data also has a line at -300

- 110416 (MonR2) - 120sec

       SLpipeline.sh obsnum=110416    # MonR2        restfreq=115.271202,109.782173  (co and c18o)
     
       QAC_STATS: MonR2_110416__0.txt 2226.26 611.437 -104.812 25167.1 2.00972e+07 0.99999 7799
       QAC_STATS: MonR2_110416__1.txt 2157.52 399.925 -29264.5 9503.88 1.73313e+07 0.996634 7976
       


# SEQ Bs/Map(Az/C)

- 110401    Bs 

       SLpipeline.sh obsnum=110401      # O-Cet: SiO detected, but nothing in HCN (20 sec)
       # uses seqbs_pipeline.sh
       
       QAC_STATS: O-Cet_110401__0.txt -320.207 58.6562 -540.327 1916.58 -609989 -0.987809 1903
       QAC_STATS: O-Cet_110401__1.txt -330.151 58.1615 -542.487 -121.705 -633853 -1 1910

- 110399    Pointing

       SLpipeline.sh obsnum=110399 extent=120    # 27.2 sec (SiO and HCN)


       QAC_STATS: O-Cet_110399__0-full -3.39204e-05 0.128163 -10.0138 22.3949 547.027 0.0178856 190765
       QAC_STATS: O-Cet_110399__0-cent -5.29817e-05 0.118217 -10.0138 22.3949 551.334 0.0267519 146051
       QAC_STATS: RMS/radiometer 3.48704 0.977724 1.91441 56.3804 1280.8 1 278

     
       QAC_STATS: O-Cet_110399__1-full 4.04388e-05 0.130061 -75.3374 73.9275 580.194 0.0133532 195702
       QAC_STATS: O-Cet_110399__1-cent 0.000324535 0.119864 -75.3374 73.9275 580.748 0.017859 150513
       QAC_STATS: RMS/radiometer 3.46054 0.930884 1.81967 401.25 1703.01 1 277




# matching 1MM Ps

With the caveat that the 1MM receiver was out of focus, we did get some data to play with.

110421 110423 110425 110429 110431 110433 on MonR2

110436 110438 on IRC+10216

- 110438

       SLpipeline.sh obsnum=110438    # IRC+10216    restfreq=230.538,220.3986 (12co and 13co in 2-1)
       # seqps_pipeline.sh
       
       QAC_STATS: IRC+10216_110438__0.txt -4448.46 88.1506 -4785.95 -399.533 -8.37652e+06 -1 1850
       QAC_STATS: IRC+10216_110438__1.txt -4201.63 93.8925 -4535.21 -3638.3 -8.04902e+06 -1 1853

- 110433

       SLpipeline.sh obsnum=110433    # MonR2        restfreq=230.538,220.3986 (co and c18o)
       # use seqps_pipeline.sh
       
       QAC_STATS: MonR2_110433__0.txt 10962.6 193.585 10377.2 25265.6 2.1294e+07 1 1875
       QAC_STATS: MonR2_110433__1.txt 12703.9 405.527 11565.1 15572.4 2.44094e+07 1 19100
       
Note for 1MM only roach0 is written

# Handling Ps and Bs modes in SLpipeline

The **Bs** mode requires two beams, an "ON" beam (typically 10) and an
"OFF" beam (typically 8). Thus **pix_list=10,8** is the default.

The **Ps** mode can in theory average multiple beams. If used, they
are averaged on output. For example the 1MM receiver uses beams 0 and
2 for the two polarizations, and they are averaged to increase the
signal by sqrt(2), thus **pix_list=0,2**.  The 2nd IF is under
**pix_list=1,3**. Note only roach0 is used for 1MM.  For SEQ for a
point source one probably needs to use **pix_list=10**, assuming the
array is centered on 10, but nobody will stop you from averaging any
of the 16 beams.
