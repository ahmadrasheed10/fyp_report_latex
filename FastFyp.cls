% Author: Defined by Mr. Junaid Hussain Muzamal <junaid.hussain@nu.edu.pk>
% Updated for robust compilation on modern TeX Live / Overleaf
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{FastFyp}[2023/01/24]
\LoadClass[11pt,a4paper,oneside]{book}

% Font encoding -- must come early to prevent OMS/cmtt font shape warnings
\usepackage[T1]{fontenc}

\usepackage{graphicx}
\usepackage[final]{microtype}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsfonts}
\usepackage{parskip}
\usepackage{titlesec}
\usepackage{titlecaps}
\usepackage[numbers]{natbib}
\usepackage[]{algorithm2e}
% appendix loaded WITHOUT the 'toc' option to prevent \@starttoc conflict
\usepackage[titletoc,title,header]{appendix}
\usepackage{url}
\usepackage{listings}
\usepackage{color}
\usepackage{xcolor}
\usepackage{caption}
\usepackage{array}
\usepackage{longtable}
\usepackage{booktabs}
\usepackage{multirow}
\usepackage[top=1in, bottom=1in, left=1in, right=1in]{geometry}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\leftmark}
\fancyhead[R]{\thepage}
\renewcommand{\headrulewidth}{1pt}
\renewcommand{\footrulewidth}{0pt}
\setlength{\headheight}{14pt}

\fancypagestyle{plain}{%
  \fancyhead[L]{\leftmark}
}

\setlength{\parskip}{6pt}
\captionsetup[figure]{justification=centering, labelfont=bf, textfont=bf}
\captionsetup[table]{justification=centering, labelfont=bf, textfont=bf}

% Bold LOF/LOT entries -- replaces tocloft's \cftfigfont / \cfttabfont
% (tocloft conflicts with appendix[toc] in TeX Live 2026 via \@starttoc)
\renewcommand{\l@figure}[2]{%
  {\bfseries\@dottedtocline{1}{1.5em}{2.3em}{#1}{#2}}}
\renewcommand{\l@table}[2]{%
  {\bfseries\@dottedtocline{1}{1.5em}{2.3em}{#1}{#2}}}

\lstdefinestyle{customc}{
  belowcaptionskip=0.5\baselineskip,
  breaklines=true,
  frame=L,
  xleftmargin=\parindent,
  language=C,
  showstringspaces=false,
  basicstyle=\footnotesize\ttfamily,
  keywordstyle=\bfseries\color{green!40!black},
  commentstyle=\itshape\color{purple!40!black},
  identifierstyle=\color{blue},
  stringstyle=\color{orange},
}

\makeatletter
\renewcommand{\@makechapterhead}[1]{%
  {\parindent \z@ \raggedright \normalfont
    \ifnum \c@secnumdepth >\m@ne
        \Large\bfseries Chapter \thechapter\hspace{10\p@}#1\par\nobreak
    \fi
    \vskip 10\p@
  }
}
\makeatother

\setcounter{secnumdepth}{3}

\titleformat{\section}
  {\normalfont\Large\bfseries}{\thesection}{1em}{}
\titlespacing*{\section}{0pt}{3.5ex plus 1ex minus .2ex}{2.3ex plus .2ex}

\titleformat{\subsection}
  {\normalfont\large\bfseries}{\thesubsection}{1em}{}
\titlespacing*{\subsection}{0pt}{3.25ex plus 1ex minus .2ex}{1.5ex plus .2ex}

\titleformat{\subsubsection}
  {\normalfont\normalsize\bfseries}{\thesubsubsection}{1em}{}
\titlespacing*{\subsubsection}{0pt}{3.25ex plus 1ex minus .2ex}{1.5ex plus .2ex}

\usepackage{setspace}
\setstretch{1.5}

\usepackage{mathptmx}
\captionsetup{font={small}}

% Hyperref loaded last to prevent conflicts with sectioning packages
\usepackage{hyperref}
\hypersetup{colorlinks, linkcolor=black, citecolor=blue, urlcolor=blue}
