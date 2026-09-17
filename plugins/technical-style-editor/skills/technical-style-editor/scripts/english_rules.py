"""English phrase patterns: (stable rule name, regex, review guidance)."""

BASE_RULES = (
    (
        "rhetorical-negation",
        r"\b(?:not|[a-z]+n['’]t)\s+[^.!?\n]{1,80}?\s+but\s+",
        "Review the rhetorical contrast; state the subject directly unless the negation defines a necessary boundary.",
    ),
    (
        "not-just",
        r"\b(?:not|[a-z]+n['’]t)\s+(?:just|only|merely)\b|\bmore\s+than\s+just\b",
        "Review emphasis through contrast and name the relevant property directly.",
    ),
    (
        "negative-opening",
        r"^\s*(?:[-*]\s+|\d+[.)]\s+)?(?:not|never)\b",
        "Keep an opening negation when it expresses a prohibition, invariant, or necessary boundary.",
    ),
    (
        "author-intent",
        r"\b(?:I|we)\s+(?:want\s+to|would\s+like\s+to|will\s+try\s+to|am\s+going\s+to|are\s+going\s+to)\s+(?:discuss|explain|show|describe|share|present)\b",
        "Replace the announcement of intent with the subject itself.",
    ),
    (
        "document-announcement",
        r"\bin\s+this\s+(?:document|article|section|talk|report),?\s+(?:we\s+(?:will\s+)?|I\s+will\s+)(?:discuss|explain|show|describe|present|explore)\b",
        "Review the description of the document; state the section's subject directly.",
    ),
    (
        "importance-marker",
        r"\b(?:it\s+is\s+(?:important|worth)|it['’]s\s+(?:important|worth))\s+(?:to\s+(?:note|emphasize|understand)|noting|emphasizing)\b",
        "Remove the announcement of importance and state the fact.",
    ),
    (
        "stance-adverb",
        r"\b(?:obviously|undoubtedly|unquestionably|clearly|of\s+course)\b",
        "Check whether this expression of certainty adds evidence.",
    ),
    (
        "promotional-adjective",
        r"\b(?:unique|revolutionary|innovative|powerful|groundbreaking|cutting[- ]edge|game[- ]changing)\b",
        "Replace promotional evaluation with a supported distinguishing property.",
    ),
    (
        "inflated-claim",
        r"\b(?:radically|dramatically|fundamentally)\s+(?:improv\w*|accelerat\w*|reduc\w*|increas\w*|transform\w*|chang\w*)\b",
        "A strong claim needs a measure, conditions, and evidence.",
    ),
    (
        "unmeasured-improvement",
        r"\b(?:significantly|substantially|considerably|greatly|effectively)\s+(?:improv\w*|accelerat\w*|reduc\w*|increas\w*|enhanc\w*|speed\w*|shorten\w*)\b",
        "Provide a measurement or describe the documented mechanism without an unsupported intensifier.",
    ),
    (
        "bureaucratic-wrapper",
        r"\b(?:in\s+order\s+to|for\s+the\s+purpose\s+of|within\s+the\s+framework\s+of|by\s+means\s+of)\b|\b(?:perform\w*|conduct\w*)\s+(?:an?\s+|the\s+)?(?:analysis|evaluation|implementation)\b",
        "Simplify the wrapper and name the actor and action.",
    ),
    (
        "passive-result",
        r"\b(?:was|were|is|are|will\s+be|has\s+been|have\s+been)\s+(?:performed|conducted|implemented|carried\s+out)\b",
        "Review the passive construction; name the actor when it is known and relevant.",
    ),
    (
        "assistant-meta",
        r"\b(?:here\s+is\s+(?:the|an?|your)\s+(?:revised|improved|polished)\s+version|I\s+hope\s+this\s+helps)\b",
        "Remove assistant commentary from the finished text.",
    ),
)

EXTENDED_RULES = (
    (
        "comparison-without-baseline",
        r"\b(?:better|faster|cheaper|more\s+(?:accurate|reliable|efficient|secure))\b",
        "Check the baseline, comparable conditions, and measured quantity.",
    ),
    (
        "weak-copula",
        r"\b(?:serves?\s+as|acts?\s+as|constitutes?)\b",
        "Check whether a precise action or definition would explain the role more clearly.",
    ),
    (
        "vague-enablement",
        r"\b(?:allows?|enables?|empowers?)\b",
        "Specify the mechanism and observable result behind the stated capability.",
    ),
    (
        "demonstrative-bureaucracy",
        r"\b(?:the\s+)?(?:aforementioned|above[- ]mentioned|said)\s+(?:approach|solution|system|method|mechanism)\b",
        "Name the subject directly.",
    ),
    (
        "weak-assertion",
        r"\b(?:it\s+can\s+be\s+(?:said|noted|concluded)|one\s+could\s+(?:say|argue)|it\s+would\s+appear)\b",
        "State the claim and its grounds, retaining any necessary uncertainty.",
    ),
)
