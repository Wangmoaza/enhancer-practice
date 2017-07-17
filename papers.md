# Enhancer 관련 논문들

## Master Transcrpition Factors and mediator Establish Super-Enhancers at Key Cell Identity Genes

Link: [논문 링크](https://doi.org/10.1016/j.cell.2013.03.035)

### Introduction

기본 정보:
* Transcription factor는 enhancer에 결합해서 coactivator와 RNA Pol II를 target gene에 recruiting함으로써 유전자 발현을 조절
* Enhancer는 few hundred base pair로 이루어지고 여러 TF와 binding하는 DNA segment
* Enhancer activity is largely cell-type specific
* Embryonic Stem Cell (ESC)에서
	* establishment/maintanence 는 몇 개의 master transcription factor에 의존
	* Oct4, Sox2, Nanog (OSN) 는 Medator coactivator complex와 함께 enhancer에 결합

얘네가 알아 낸 거:
 * Enhancer와 관련된 Mediator들은 굉장히 큰 enhancer domain을 차지한다.
 * 우리는 이것을 super-enhancer라 칭하겠다!
 * super-ehancer에는 key ESC TF인 Oct4, Sox2, Nanog, Klf4, Esrrb가 많다
 * 또 super-enhancer는 다양한 cell type에서 발견되었고 
 gene expression program에 중요한 역할을 하는 cell-type-specific gene과 연관되어있었다.
 * **고로!** super-enhancer는 cell identity에 중요한 gene들을 drive한다.
---
### Results
#### Large genomic domains occupied by master TF and mediators in ESCs

super-enhancer의 정의
	1. span DNA regions whose median length is an order of magnitude larger than the typical enhancer
	2. have levels of mediator that are at least an order of magnitude greater than those at the typical enhancer

그 이외의 characteristics:
* typical enhancer와 비슷하지만 larger scale로 특징들을 가지고 있다

그럼 typical enhancer와 super enhancer를 구분하는 특징은?
* particularily enriched in Klf4 and Esrrb

> Klf4, Esrrb는 ESC gene expression program과 somatic cell을 iPS로 바꾸는 데 중요한 역할을 하는 TF

결론적으로 ESC super-enahncer는 다음과 같이 생각할 수 있다.
	* large clusters of enhancers thatn can be dstinguished from typical enhancers
    by the presence of TF Klf4 and Esrrb and exceptional levels of Mediator
    * formed as a consequence of binding of specific master TF to dense clusters of their binding site sequences

![Alt text](http://www.sciencedirect.com/science?_ob=MiamiCaptionURL&_method=retrieve&_eid=1-s2.0-S0092867413003929&_image=1-s2.0-S0092867413003929-gr1_lrg.jpg&_cid=272196&_explode=defaultEXP_LIST&_idxType=defaultREF_WORK_INDEX_TYPE&_alpha=defaultALPHA&_ba=&_rdoc=1&_fmt=FULL&_isHiQual=Y&_issn=00928674&_pii=S0092867413003929&md5=8c64df20db591398f7755e9ecf29ded1)

#### Super-enhancers are associated with key ESC identity genes

> * enhancer는 보통 target gene과 ~50 kb 안에서 interaction함. 물론 더 멀 때도 있음.
> * enhancer를 target gene에 assign하는 여러 방법들이 있음
>	* proximity, enhancer-promotor unit assignment (EPU), 3C-based

* 얘네는 우선 proximity를 이용해서 231개 super-enhancer를 210개의 유전자에 assign함
* 이 결과는 EPU와 Hi-C 결과와도 constistent함
* super-enhancher-associated gene에는 ESC identity를 조절하는 유전자가 대부분 포함됨
* 더 알아보기 위해 super-enhancer-associated gene 집합과 2000개의 regulator를 포함한 short hairpin RNA (shRNA) knockdown screen에 있는 gene을 비교해봄
* TF encoding gene이 super-enhancer-associated gene의 대부분을 차지함.
* 반대로 super-enhancer는 house keeping gene과는 연관이 없었음.

#### Functional attributes of super-enhancers


* 우리가 보니까 super-enhancer-associated gene들은 typical enhancer와 관련되있는 유전자보다 더 높은 발현 수준을 보였음.
* super-enhancer가 target gene에 high-level expression을 주도 하는 것이 아닐까 생각됨.
* 이걸 테스트 하기 위해 super enhancer들을 luciferase reportur cunstruct에 끼워 넣고 ESC에 trasfection 시킴
* super-enhancer 안에 있는 enhancer가 높은 luciferase activity를 나타냄! ~~거봐 내말이 맞았지!~~


* 어떤 요소가 이런 결과를 야기하는 것일까를 또 테스트 해보기로 함
* ChIP-seq 결과를 보니까 enhancer element에서 특정 TF의 level이 luciverase activity와 상관 관계를 맺음


* Oct4나 Mediator 중 어느거나 level이 떨어지면 ESC gene expression system에 비슷한 영향을 주고 ESC state를 빠르게 잃어감.
* 이게 super-enhancer와 연관이 있는지 알아봄.

Hypotheseis:

	 super-enahcner-associated genes 는 enhancer-binding factor의 level 변화에 더 민감하다.

* 이를 확인하기 위해 두가지 실험을 수행함.

1. super-enhancer-associated gene이 다른 유전자보다 master TF의 loss에 더 민감하다면 Oct4의 감소가 super-enhancer-associated gene expression의 preferential loss를 야기시킬 것이다.
	* shRNA를 이용해 Oct4 transcrption level을 떨어뜨림
	* super-enhancer-associated gene에서 transcript level이 상당하게 그리고 일찍 줄어듦

2. Mediator subunit의 감소는 super-enhancer-associated gene의 발현에 영향을 줄 것이다.

결과적으로
Oct4와 Mediator의 감소는 super-enhancer-associated gene에 큰 영향을 줌

#### Super-enhancers in B Cell

뭐 ESC랑 거의 비슷한 양상의 결과들이 나옴 ~~귀찮아서 적지 않겠노라~~

#### Super-enhancers are cell-type specific and mark ke cell identity genes

super-enhancer가 mammalia cell에서 보편적인 특징인지 알아보기 위해 3가지 cell type에서 더 실험해봄.
* mouse myotubes (MyoD), T helper cells (Th), macrophages
* 여기서도 비슷한 결과가 나왔음.

* 즉, cell state를 조절하는 key TF들은 cell identity를 결정하는 데 중요한 역할을 하는 특정 유전자들과 관계를 맺는 enhancer의 cluster에 
결합한다는 우리의 주장을 뒷받침해준다! 

* 또 super-enhancer와 그와 연관된 유전자들은 typical ehnahcer-associated gene들에 비해 cell-type specific했다.
* 이것은 super-enhancer가 key TF들이 cellular identity를 조절하는 유전자와 연관되어있는 binding site cluster에 결합하면서 만들어졌다는
우리의 가설과 consistent 하다!

---
### Discussion

super-enhancer에 대해 정리하자면
* ESC에서 super-enhancer는 typical enhancer와 크기, TF density & content, ability to activate trasncription, sensitivity to perturbation이라는 측면에서 차이가 있음.
* super-enhancer가 다양한 cell type 그리고 암에서도 발견되는 걸 보아 super-enhancer는 mammalian cell identity와 disease를 조절하는 거 같음.
* super-enhancer의 formation은 많은 master TF가 DNA sequence cluster에 결합하면서
* genes encodeing ESC master TF are themselves driven by super-enhancers => feedback looop


* * *

## Super-Enhancers in the Control of Cell Identity and Disease

Link: [논문 링크](http://dx.doi.org/10.1016/j.cell.2013.09.053)

![Alt text](http://ars.els-cdn.com/content/image/1-s2.0-S0092867413012270-fx1.jpg)

위에 논문 후속작으로 같은 연도 같은 랩에서 나온 논문
위 논문과 똑같은 소리 하는 것은 다 제외
### Introduction

* dnflsms 86 human cell과 tissue type에 대해 super-enhancer catalog을 만들었다
* 이 super-enhancer들은 cell-type-specific TF를 암호화하는 유전자들과 관련되어있다
* 이 catalog을 이용해서 우리는 특정 질병과 관련되어있는 DNA sequence variation이 super-enhancer에서 enrich되어 있음을 알아냈다!
* 또 tumor cell은 key oncogene 위치에 super-enhancer가 생긴다!

---

### Results

#### Transcription factors in ESCs

* Whyte et al., 2013 에서 밝혀낸 5개 ESC TF (Oct4, Sox2, Nanog, Klf4, Esrrb) 외에 추가로 15개 TF에 대해 ChIP-seq 해봄
* 이 중 6개 (Nr5a2, Prdm14, Tcfcp2l1, Smad3, Stat3, Tcf3)는 앞에 5개랑 비슷한 양상을 보였고 나머지는 안 그럼
* 특히 Smad3 -> TGF-b, Stat3 -> LIF-, Tcf3 -> Wnt signaling pathway를 targeting하기 때문에 좀 interesting
	* 얘네는 master TF에 의해 enhancer로 recruit 되는 애들이기 때문에
* 아무튼 이런 TF들이 super-enhancer에 enrich 되어있는 건 signaling pathway들이 ESC identity를 조절하는 
key gene에 모여든다는걸 보여주는 증거임!


* super-enhancer 지역의 binding motif이 빈도를 분석해봄
* super-enhancer에 motif들이 완전 enrichment 되어있는거임!
=> TF들이 그들의 known DNA sequence motif에 결합하므로써 super-enhancer에 기여


* 옛날 사람이 ESC의 core transcriptional regulatory circuitry를 제안한 게 있는 데 이거 개정한 모델이 필요함


#### RNA Pol II, cofactors, and chromatin regulators

* 이번에는 TF 말고 RNA Pol II, cofactor, chromatin regulator에 대해서도 살펴봄
* publish된 데이터랑 새로 우리가 만든 RNA-seq, ChIP-seq 데이터를 분석함
* 결과를 보니까 RNA Pol II, Mediator, cohesin, p300, CBP 등등 겁나 많은 것들이 super-enhancer에 enrich되어 있었음
* RNA pol II는 enhancer를 전사해서 noncoding RNA (eRNA)를 만들고 어떨 때는 enhancer activity에 기여한다고 알려져 있음
* ESC 분화는 super-enhancer-associated gene의 발현이 엄청 줄게 함.
* super-enhancer의 이러한 dual feature가 발생 과정에서 cell state transition을 야기할 것이라고 추측함.
	1. drive high-level expression of key regulators of cell identity
	2. vulnerability to perturbation of their components


#### Super-enhancers in many cell types

* H3K27ac ChIP-seq data를 이용해서 86 human cell & tissue sample에서 super-enhancer catalog를 만듦 ~~연구원의 노고가...~~
* 관련된 많은 유전자들은 cell type specific
* super-enhancer-associated gene에 master TF가 많았다는 사실을 이용, 반대로
super-enhancer-associated gene들을 candidate master TF로 생각해서 분석해봄


> 여기까지는 앞에 논문과 거의 같은 내용
> 다음부터는 질병과 관련된 이야기

#### Disease-associate DNA sequence variation in super-enhancers

* 1675개의 GWAS와 연관된 5303개 SNP를 이용, super-enhancer / enhancer 에 어떻게 분포되어있는지 살펴봄
* trait-associtated SNP의 대부분이 noncoding region에 있었음. 이중 64%가 enhancer에 있었음.
* 그리고 super-enhancer에 더 enrich 되어있었음 ~~역시!~~
* 우리의 에상대로라 특정 질병과 연관되어있는 SNP는 disease-relevent cell에서만 super-enhaner에서 나타야됨.
  그리고 역시 결과도 그러하였노라.
* **결론**: super-enhancer는 cell identity를 결정하는 유전자들의 발현은 조절하니까 변화된 cell identity gene들의 발현이 질병에 기여

#### Examples of disease-associtate SNPs in super-enhancers

여러가지 질병에서 더 자세히 살펴봄

Alzheimer's disease
* brain cell
* amyloid precursor protein, transmembrane protein, apolipoprotein E4
* 19%의 SNP가 genome의 1.4% 밖에 안 차지하는 super-enhancer에서 발견됨

Type 1 diabetes
* SNP enrichied in super-enhancers of primary Th cells

Systemic lupus erythematosus (SLE) 루푸스
* 몸의 여러 곳에 염증을 일으키는 만성 자가면역질환
* noncoding SNP가 B cell의 super-enhancer에서 가장 빈번하게 있음

#### Super-enhancers in cancer

~~암, 암세포를 빼먹을 수는 없지~~
* H3K27ac ChIP-seq data를 이용해서 18 human cancer cell에서 super-enhancer를 찾고 associated gene도 찾고
* cancer cell은 tumor pathogenesis 과정에서 oncogene driver에 super-enhancer를 얻음
* Hanahan and Weinberg (2011)이 제시한 tumor pathogenesis 과정에서 얻는 hallmark biological capabilities가 있음
* colorectal cancer (대장암) 에서 보니까 1/3의 super-enhancer gene이 cancer hallmark와 관련이 있었음

---
### Discussion

우리가 알아낸 것을 정리해 보면

	1. ESC에서 TF, cofactor, chromatin regulators, RNA Pol II 등이 super-enhancer 지역에 enrich 되있음.
	그리고 enhancer는 eRNA로 전사도 많이 됨.
		* ESC에서 밝혀낸게 다른 cell type 보다 훨 많음. ESC는 super-enhancer 연구하는 데 좋은 모델
	
	2. 많은 human cell, tissue에서 super-enhancer와 그와 관련된 유전자 catalog를 만듦
		* super-enhancers are cell type specific

	3. disease-associated SNP는 질병과 관련있는 cell의 super-enhancer에서 많이 나타남.
	4. 암세포는 tumor pathogenesis 과정에서 oncogene driver, cancer hallmark와 관련된 유전자들에서 super-enhancer를 얻음
		* super-enhancer가 cancer의 biomarker가 될 수 있을듯?

* * *
## Convergence of Developmental and Oncogenic Signaling Pathways at Transcriptional Super-Enhancers

Link: [논문 링크](http://dx.doi.org/10.1016/j.molcel.2015.02.014)
![Alt text](http://www.cell.com/cms/attachment/2028846145/2046897833/fx1.jpg)
### Introduction

이전 연구를 통해 밝혀진 것들
* super-enhancer(SE)는 cell-type-specific process에 특히 중요한 역할을 한다
* 암세포는 oncogene의 높은 발현을 이끄는 SE를 얻는다
* 여러 질병과 관련되어있는 sequence variation은 SE에 많이 enrich 되어있다

이번 연구에서 밝힌 것들
* SE의 구성성분들은 보통 cell-type-specific, OCT4-dependent function을 가지고 있는 active enhancer로 작동한다
* SE는 Wnt, TGF-b, LIF signaling pathway의 terminal TF와 결합한다.

> Wnt signaling pathway: carcinogenesis, embryonic development에 관여한다고 알려져 있음. gene transcription 조절
> TGF-b signaling pathway: cell growth, cell differentiation, apoptosis 등 여러 cellular process에 관여
> LIF signaling pathway: affects cell growth by inhibiting differentiation

* oncogenic Wnt signaling에 의존적인 tumor cell은 tumorigenesis에 관련된 key gene에 SE를 얻는다
* Wnt pathway에서의 perturbation은 이러한 유전자들에 큰 영항을 미친다.

### Results

소문단의 구성
1. 이전 연구에서 이런 이런 결과들이 있었습니다. (배경)
2. 이걸 바탕으로 우린 이것을 살펴보기로 하였습니다. (목적)
3. 실험 방법으로는 이러 이러한 것을 사용했습니다. (방법)
4. 실험 결과는 무엇 무엇 이었습니다. (결과)
5. 그래서 이것은 저러 저러 하다고 볼 수 있습니다. (결론)

만약에 추가로 알아 본것이 있으면
1. 결과 중에 이러 이러한 게 나왔습니다.
2. 더 살펴보기 위해 추가로 요런 실험을 하였습니다.
3. 결과는 요로코롬 나왔습니다.
4. 그래서 이 현상은 이렇게 설명할 수 있습니다.

#### Enhancer activity of SE constituents

* murine ESC에서 살펴봄
* 이전 연구에서 ESC SE는 OCT4, SOX2, NANOG (pluripotency TFs) 와 binding하고 transcription apparatus의 구성 성분들, Mediator가 짱짱 많은 지역
* ESC SE중 5개 골라서 각각의 구성성분들이 enhancer activity가 있는지 살펴봄
	* 어떻게? 각각 구성성분들을 enhancer-reporter vector에 cloning함
	* luciferase assay 해봤는데 거의 다 enhancer activity가 있었고 ESC specific activity였음.
	* OCT4를 없애니까 대부분 enhancer activity가 감소
	* 즉, ESC는 ESC-specific function을 가지고 있고 OCT4-dependent한 anctive enhancer의 뭉텅이
	
* 한 SE의 구성성분끼리 서로 영향을 줄까?
	* 여러 조합으로 reporter system에 넣어봄
	* Pou5f1 super-enhancer에서 여러 enhancer 구성성분들은 additive / synergistic affect가 없었음

#### Perturbations super-enhancer constituents

* individual constituent가 in vivo에서 redundant한 function이 있는지 CRISPR/Cas9을 이용해서 알아봄
* 대부분의 경우 SE 성분을 없애면 관련된 유전자 발현이 떨어졌음
* **결론**:대부분 SE 구성성분은 transcription activity에 + 영향을 주지만 어떤 경우에는 반대의 영향을 끼치기도 함


* 어떤 SE-associated gene들은 특정 SE 구성성분에 특별히 의존적이었음
* 실험을 좀 더 해보니까 Prdm14 super-enhancer의 구성성분들은 interdependent functionality를 보였음

#### Signaling modules at super-enhancers

왜 key cell identity gene들은 clustered enhancer structure를 갖게 되었을까?
* house keeping gene들도 발현은 높은데 딱히 super-enhacer 구조를 안보이거든


* ** 가설**: key cell identity gene들은 developmental signaling pathway에 직접적으로 반응을 잘 하기 위해 SE 구조를 갖도록 진화했다.
* stem cell state 조절에 중요한 역할을 하는 Wnt (TCF3), TGF-beta (SMAD3), LIF (STAT3) signaling pathway의 terminal TF들이 SE에 결합하는 패턴이 OCT4, SOX2, NANOG와 유사함.
* 그리고 얘네가 함께 super-enhancer에 결합하는 비율이 random typical enhancer들의 cluster보다 높음
* 만약 얘네가 developmental signaling pathway에 잘 반응하도록 진화했으면 진화적으로 보존되있지 않겐?
	* signaling TFs are enriched in ESC super-enhancers
* 이 가설이 맞다면 SE-associated gene들이 typical enhancer-associated gene들 보다 signaling pathway 변화에 잘 반응해야하지 않겠니?
	* pathway에 변화를 주었을 때 가장 많은 변화를 보인 유전자들 중에 SE-associated gene들이 있었음
	
#### Signaling to super-enhancers acquired in tumor cells

* 이미 알려져 있는 사실: 
	1. cancer cell은 oncogene에서 super-enhancer를 잘 얻는다.
	2. signaling pathway의 dysregulation은 cancer hallmark다.
* 이 두개가 연관되어있지 않을까?
* CRC (대장암)에서 tumorogenesis 과정에서 얻는 oncogene-associated SE가 TCF4 (Wnt pathway의 terminal TF)와 결합한다!
* 그리고 이 SE는 c-MYC locus (well-established target of Wnt signaling)에 있다!


* 우리는 또 TCF4가 다른 CRC SE에 결합하는지, 그리고 acuired-SE에 관련된 유전자들이 Wnt pathway의 변화에 반응하는지를 알아봄.
* 결합함. 그리고 전부는 아니지만 일부는 Wnt pathway 변화에도 반응함.


* 다른 cancer에서도 이러한 현상이 일어나는지 알아보기 위해 breast cancer에서도 실험해봄


* **결론** turmor cells evolve SEs at key oncogenes, at least in part, to enhance the connection to oncogenic signaling pathways.


#### Discussion

intro에서 밝힌 결과들이랑 거의 똑같음. 위에 참고.


***
## Genome-wide characterization of mammalian promoters with distal enhancer functions

Link: [논문링크](https://www.nature.com/ng/journal/v49/n7/abs/ng.3884.html)

### Introduction

* promoter와 enhancer은 비슷한 게 많음
* 이전 연구들에서 promoter가 enhancer역할도 할 수 있음을 시사하기도 했음.
* 우리는 여기서 더 나아가 promoter 중 어느 것들이 enhancer 역할을 하는지, 
  이러한 enhancer 역할이 distal gene regulation에 관여하는지 알아봄.
* CapStarr-seq: Starr-seq에다가 capture도 같이한 거
* CRISPR-Cas9 이용해서 natural context에서 Epromoter들이 멀리 떨어진 유전자의 조절에 관여한다는 것을 보여줌.

> Epromotor: TSS-overlapping enhancers

---
### Results

#### Mouse TSS-proximal DHSs display enhancer activity

* proximal enhancers are specific to tissue type
* P5424 cell line에서 proximal enhancer와 distal enhancer 비율이 비슷했음


![Alt text](https://www.nature.com/ng/journal/v49/n7/images/ng.3884-F1.jpg)



#### Assessment of the enhancer activity of coding-gene promotor

* refseq의 모든 coding gene promoter에 대해 CapStarr-seq 수행
* K562랑 heLa cell에서 Epromoter 겹치는게 꽤 있었음

#### Epromoters display specific genomic and epigenomic features

> p300: coactivator protein

... 그만 할래

***
