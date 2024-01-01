# Leveraging Gender bias in Brands

## 1. Introduction
In the ever-evolving landscape of advertising, the strategic use of gender bias has become a subject of considerable interest and scrutiny. As brands navigate the intricacies of audience engagement, the question arises: to what extent do brands leverage gender bias to enhance appeal and foster engagement? 

This project delves into this compelling inquiry, seeking to analyze the deliberate incorporation of gender bias in advertising and its impact on audience perception and interaction. This endeavor not only contributes to our understanding of advertising dynamics but also provides valuable insights for brands aiming to navigate the delicate balance between effective communication and societal expectations.

## 2. Problem Statement
To analyze if brands leverage gender bias for appeal and engagement.

## 3. Objectives
- Define metrics to measure gender bias in a sentence. 
- Extract YouTube transcripts of brands targeted at men and women along with other data and select brands with most bias. 
- Perform statistical analysis on these brands’ ads and formulate meaningful conclusions.

## 4. Methodology

1. Collected transcripts of 10 most viewed Ads from 10 brands targeted at men and 10 brands targeted at women. 
2. Calculated gender bias metrics of transcripts of each brand and selected 3 brands each with highest gender bias. 
3. Collected the transcripts, dates, views, likes, and comments of all the ads from these brands over the past two years. 
4. Calculated gender bias metrics of the transcripts collected. 
5. Performed Independent T-Test and Regression Analysis. 
6. Formulated inferences and derived conclusion from the obtained results.

## 5. Inferences

### 5.1 From average gender bias metrics 
I gave a ranking system where highest value is given 3 score, second highest is given 2 score and third highest is given 1 score. Based on the sum of these scores, 6 brands were selected.            
- Masculine Brands: Old Spice, The Man Company and Gillette                                       
- Feminine Brands: Chanel, Shein and Sephora

### 5.2 From Independent T-Test 
- It was observed that p-value of number of views, number of comments, GenBit score, average bias ratio, % female words and % male words is less than 0.05. 
- Hence, it can be concluded that there is statistically significant difference between the means of the two groups in terms of the above-mentioned metrics. 
- That is, there is not much similarity between the Ads targeted at male and female in terms of popularity and gender bias metrics. 
- Although, this cannot be said about the number of likes. 

### 5.3 From Regression Analysis 
Independent Variables: GenBit score, Avg. Bias ratio, Frequency of Male definition words, Frequency of Female definition words and all of these multiplied by binary variable (Binary Variable: 1-Male, 2-Female), Title GenBit score, Title avg bias ratio, Length and Days old. <br>

#### 5.3.1 Dependent Variable: Views <br>
- Title GenBit score has –3.3e6 regression co-efficient which says that titles with more gender bias are less likely to get views. 
- Title avg bias ratio has 1.4e6 regression co-efficient which says that use of female gender bias words is more likely to generate more views. 
- % Female words has 1e8 regression co-efficient whereas % Male words has –3.5e6 regression co-efficient which says that use of female definition words is more likely to generate more views and use of male definition words is more likely to generate less views. 
- GenBit score has –3.67e7 regression co-efficient whereas GenBit score*Binary Variable has 1.7e10 regression co-efficient. 
- Average bias ratio has 2.9e7 regression co-efficient whereas Average bias ratio* Binary Variable has –1.5e7 regression co-efficient. <br>

#### 5.3.2 Dependent Variable: Likes <br>
- % Female words has –4.2e-2 regression co-efficient whereas % Male words has –3.9e-2 regression co-efficient which says that use of female and male definition words is more likely to generate less likes. 
- GenBit score has –2.4e-2 regression co-efficient whereas GenBit score*Binary Variable has 4.55e-3 regression co-efficient. 
- Average bias ratio has 3.4e-2 regression co-efficient whereas Average bias ratio* Binary Variable has –1.6e-2 regression co-efficient.

## 6. Conclusion

In conclusion, the relationship between gender bias and advertising outcomes reveals a complex interplay of factors. While the presence of bias, particularly towards women, tends to amplify virality by sparking controversy and increasing views, the overall appeal of ads is nuanced. 

Ads featuring titles with gender bias, especially leaning towards women, often generate heightened interest and discussions, contributing to their virality. Notably, the use of female-centric language in ads appears to attract more viewership, reflecting a trend towards increased engagement. Additionally, the presence of gender bias in ads correlates with a reduced likelihood of garnering a higher number of likes.

Conversely, a noteworthy observation arises when exploring the use of both male and female definition words. Such balanced approaches seem to correlate with a decrease in the likelihood of accumulating higher likes. This suggests that attempts at inclusivity may not always translate into stronger positive reactions from the audience.

In essence, the advertising landscape showcases a delicate balance between attracting attention, sparking controversy, and securing positive engagement. Navigating this intricacy requires advertisers to carefully consider the implications of gender bias, recognizing that the dynamics of virality and appeal may vary significantly across different strategies and audiences.
