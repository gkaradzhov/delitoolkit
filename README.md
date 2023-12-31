# delitoolkit

A toolkit for evaluating deliberative discussions and building DEliBots. For more details see https://delibot.xyz

## Usage

## DeliAnnotation

This module gives access to classifiers trained to annotate deliberative discussions. The classifier predicts the
first 2 levels from the DeliAnnotate annotation scheme. Please refer to the original paper for usage,
annotation description, guidelines, classification architecture and performance: [link](#deliannotation-module).

```
from delitoolkit import deliannotate

deli_predictor = deliannotate.DeliAnnotationPredictor()

type, role = deli_predictor.predict("What about A")
```

## Cause of change of mind predictor (aka conversational turning points or inflection points)

This module gives access to classifiers trained to predict which utterances in a collaborative conversation can cause
someone to change their mind. Please refer to the original paper for usage, classification architecture and
performance [link](#inflection-point-module). Currently delitoolkit provides API to an enhanced Bag-of-words model, with slightly better
performance than the one in the original paper.
The classifier relies only on linguistic data, without incorporating any other datastreams (and thus is applicable to
wider-range of tasks). Please provide conversation context of at least 2 utterances for best performance.

```
from delitoolkit.inflection_point import bow

predictor = bow.BoWSimple()

print(predictor.predict_proba(["Hi", "I think 3"]))
```


## Relevant papers and BibTeX citations

### DeliAnnotation module
**DeliData A dataset for deliberation in multi-party problem solving (https://delibot.xyz/delidata)**
  
    @article{karadzhov2023delidata,
        title={DeliData: A dataset for deliberation in multi-party problem solving},
        author={Karadzhov, Georgi and Stafford, Tom and Vlachos, Andreas},
        journal={Proceedings of the ACM on Human-Computer Interaction},
        volume={7},
        number={CSCW2},
        pages={1--25},
        year={2023},
        publisher={ACM New York, NY, USA}
      }

### Inflection point module 
**What makes you change your mind? An empirical investigation in online group decision-making conversations**
  
      @inproceedings{karadzhov2022makes,
        title={What makes you change your mind? An empirical investigation in online group decision-making conversations},
        author={Karadzhov, Georgi and Stafford, Tom and Vlachos, Andreas},
        booktitle={Proceedings of the 23rd Annual Meeting of the Special Interest Group on Discourse and Dialogue},
        pages={552--563},
        year={2022}
      }

