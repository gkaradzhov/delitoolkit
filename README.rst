delitoolkit
===========

A toolkit for evaluating deliberative discussions and building DEliBots.
For more details see https://delibot.xyz



Install
-------

Please install the latest version from PyPi, preferably in a virtual environment of choice.

::

    pip install delitoolkit

Usage
-----

DeliAnnotation
--------------

This module gives access to classifiers trained to annotate deliberative
discussions. The classifier predicts the first 2 levels from the
DeliAnnotate annotation scheme. Please refer to the original paper for
usage, annotation description, guidelines, classification architecture
and performance: `link <#deliannotation-module>`__.

::

   from delitoolkit import deliannotate

   deli_predictor = deliannotate.DeliAnnotationPredictor()

   type, role = deli_predictor.predict("What about A")

Cause of change of mind predictor (aka conversational turning points or inflection points)
------------------------------------------------------------------------------------------

This module gives access to classifiers trained to predict which
utterances in a collaborative conversation can cause someone to change
their mind. Please refer to the original paper for usage, classification
architecture and performance `link <#inflection-point-module>`__.
Currently delitoolkit provides API to an enhanced Bag-of-words model,
with slightly better performance than the one in the original paper. The
classifier relies only on linguistic data, without incorporating any
other datastreams (and thus is applicable to wider-range of tasks).
Please provide conversation context of at least 2 utterances for best
performance.

::

   from delitoolkit.inflection_point import bow

   predictor = bow.BoWSimple()

   print(predictor.predict_proba(["Hi", "I think 3"]))

DeliData
--------

Easy way to access the contents of
`DeliData <#deliannotation-module>`__. Contains 500 deliberative
discussions of groups solving the Wason card selection task. Each
utterance is augmented with additional data, such as annotation,
solutions, and approximation of team performance. For full information,
please refer to the DeliData paper and DELIDATA_README.md

::

   from delitoolkit.delidata import DeliData


   delidata_corpus = DeliData()
   groups = list(delidata_corpus.corpus.keys())
   for m in delidata_corpus.corpus[groups[0]]:
       print(m['message_type'], m['original_text'])

Relevant papers and BibTeX citations
------------------------------------

DeliAnnotation module
~~~~~~~~~~~~~~~~~~~~~

**DeliData A dataset for deliberation in multi-party problem solving
(https://delibot.xyz/delidata)**

::

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

Inflection point module
~~~~~~~~~~~~~~~~~~~~~~~

**What makes you change your mind? An empirical investigation in online
group decision-making conversations**

::

     @inproceedings{karadzhov2022makes,
       title={What makes you change your mind? An empirical investigation in online group decision-making conversations},
       author={Karadzhov, Georgi and Stafford, Tom and Vlachos, Andreas},
       booktitle={Proceedings of the 23rd Annual Meeting of the Special Interest Group on Discourse and Dialogue},
       pages={552--563},
       year={2022}
     }
