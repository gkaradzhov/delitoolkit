# DeliData

This is a README that outlines key fields and characteristics of the DeliData corpus.
For full description of how we collected DeliData, as well as possible applications, please refer to the original
paper  [link](#citation).

# Data Fields

###### group_id

Unique identifier of the group chat

###### message_id

Message identifier. System messages will have an id of -1, however all participant messages' ids are unique.

###### message_type

INITIAL - indicating the cards presented and aliases of participants;

SUBMIT - indicating that a participant has pressed the Submit Solution button

MESSAGE - noting a chat entry

###### origin

The alias of the participant who submitted a message/solution

###### original_text

Original text as said in the collected conversation;

For INITIAL type, contains the list of participants and cards presented.

For SUBMIT type, contains the cards submitted

###### clean_text

Normalised message, with applied tokenisation, and masking of special tokens. Special tokens are considered solution
mentions, which are masked with < CARD > and participant mentions which are masked with < MENTION >

###### annotation_type

A record from the first level of DeliAnnotation. Can be Probing, Non-probing deliberation, or None. For more details,
please refer to the DeliData paper.

###### annotation_target

A record from the second level of DeliAnnotation. Can be Moderation, Reasoning, Solution, Agree, or Disagree. For more
details, please refer to the DeliData paper.

###### annotation_additional

A record from the third level of DeliAnnotation. Can be partial_solution, complete_solution, specific_referee,
solution_summary, or consider_opposite. For more details, please refer to the DeliData paper.

###### team_performance

An approximation of team performance, based on user submissions, and solution mentions. Range [0-1], where 1 indicates
each participant selecting the correct solution.

###### performance_change

Change of performance based compared to the previous utterance

###### sol_tracker_message

Extracted solution from the current message

###### sol_tracker_all

Up-to-date "state-of-mind" for each of the participants, i.e. an approximation of what each participant think the
correct solution is at given timestep. This is based on initial solutions, submitted solutions, and solution mentions.
team_performance value is calculated based on this column

### Citation

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

