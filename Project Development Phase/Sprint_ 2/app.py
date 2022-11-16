@import url("https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@300;400;600;700&display=swap");
/*
 * 	Default theme - Owl Carousel CSS File
 */
/*!
 * Bootstrap v4.3.1 (https://getbootstrap.com/)
 * Copyright 2011-2019 The Bootstrap Authors
 * Copyright 2011-2019 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
:root {
    --blue: #0056B3;
    --indigo: #6610f2;
    --purple: #6f42c1;
    --pink: #e83e8c;
    --red: #A91E2C;
    --orange: #fd7e14;
    --yellow: #F0B400;
    --green: #18634B;
    --teal: #0056B3;
    --cyan: #17a2b8;
    --white: #ECF0F3;
    --gray: #93a5be;
    --gray-dark: #525480;
    --primary: #e6e7ee;
    --secondary: #2D4CC8;
    --success: #18634B;
    --info: #0056B3;
    --warning: #F0B400;
    --danger: #A91E2C;
    --light: #D1D9E6;
    --dark: #31344b;
    --default: #262833;
    --white: #ECF0F3;
    --gray: #44476A;
    --neutral: #ECF0F3;
    --soft: #e6e7ee;
    --black: #262833;
    --purple: #6f42c1;
    --gray-100: #f3f7fa;
    --gray-200: #fafbfe;
    --gray-300: #e6e7ee;
    --gray-400: #D1D9E6;
    --gray-500: #b1bcce;
    --gray-600: #93a5be;
    --gray-700: #66799e;
    --gray-800: #525480;
    --facebook: #3b5999;
    --dribbble: #ea4c89;
    --github: #222222;
    --behance: #0057ff;
    --twitter: #1da1f2;
    --slack: #3aaf85;
    --breakpoint-xs: 0;
    --breakpoint-sm: 576px;
    --breakpoint-md: 768px;
    --breakpoint-lg: 992px;
    --breakpoint-xl: 1200px;
    --font-family-sans-serif: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
    --font-family-monospace: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
}

*,
*::before,
*::after {
    box-sizing: border-box;
}

html {
    font-family: sans-serif;
    line-height: 1.15;
    -webkit-text-size-adjust: 100%;
    -webkit-tap-highlight-color: rgba(38, 40, 51, 0);
}

article, aside, figcaption, figure, footer, header, hgroup, main, nav, section {
    display: block;
}

body {
    margin: 0;
    font-family: "Nunito Sans", sans-serif;
    font-size: 1rem;
    font-weight: 300;
    line-height: 1.5;
    color: #44476A;
    text-align: left;
    background-color: #e6e7ee;
}

[tabindex="-1"]:focus {
    outline: 0 !important;
}

hr {
    box-sizing: content-box;
    height: 0;
    overflow: visible;
}

h1, h2, h3, h4, h5, h6 {
    margin-top: 0;
    margin-bottom: 0.5rem;
}

p {
    margin-top: 0;
    margin-bottom: 1rem;
}

abbr[title],
abbr[data-original-title] {
    text-decoration: underline;
    -webkit-text-decoration: underline dotted;
    text-decoration: underline dotted;
    cursor: help;
    border-bottom: 0;
    -webkit-text-decoration-skip-ink: none;
    text-decoration-skip-ink: none;
}

address {
    margin-bottom: 1rem;
    font-style: normal;
    line-height: inherit;
}

ol,
ul,
dl {
    margin-top: 0;
    margin-bottom: 1rem;
}

ol ol,
ul ul,
ol ul,
ul ol {
    margin-bottom: 0;
}

dt {
    font-weight: 600;
}

dd {
    margin-bottom: .5rem;
    margin-left: 0;
}

blockquote {
    margin: 0 0 1rem;
}

b,
strong {
    font-weight: 700;
}

small {
    font-size: 80%;
}

sub,
sup {
    position: relative;
    font-size: 75%;
    line-height: 0;
    vertical-align: baseline;
}

sub {
    bottom: -.25em;
}

sup {
    top: -.5em;
}

a {
    color: #31344b;
    text-decoration: none;
    background-color: transparent;
}

a:hover {
    color: #262833;
    text-decoration: none;
}

a:not([href]):not([tabindex]) {
    color: inherit;
    text-decoration: none;
}

a:not([href]):not([tabindex]):hover, a:not([href]):not([tabindex]):focus {
    color: inherit;
    text-decoration: none;
}

a:not([href]):not([tabindex]):focus {
    outline: 0;
}

pre,
code,
kbd,
samp {
    font-family: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
    font-size: 1em;
}

pre {
    margin-top: 0;
    margin-bottom: 1rem;
    overflow: auto;
}

figure {
    margin: 0 0 1rem;
}

img {
    vertical-align: middle;
    border-style: none;
}

svg {
    overflow: hidden;
    vertical-align: middle;
}

table {
    border-collapse: collapse;
}

caption {
    padding-top: 1rem;
    padding-bottom: 1rem;
    color: #525480;
    text-align: left;
    caption-side: bottom;
}

th {
    text-align: inherit;
}

label {
    display: inline-block;
    margin-bottom: 0.5rem;
}

button {
    border-radius: 0;
}

button:focus {
    outline: 1px dotted;
    outline: 5px auto -webkit-focus-ring-color;
}

input,
button,
select,
optgroup,
textarea {
    margin: 0;
    font-family: inherit;
    font-size: inherit;
    line-height: inherit;
}

button,
input {
    overflow: visible;
}

button,
select {
    text-transform: none;
}

select {
    word-wrap: normal;
}

button,
[type="button"],
[type="reset"],
[type="submit"] {
    -webkit-appearance: button;
}

button:not(:disabled),
[type="button"]:not(:disabled),
[type="reset"]:not(:disabled),
[type="submit"]:not(:disabled) {
    cursor: pointer;
}

button::-moz-focus-inner,
[type="button"]::-moz-focus-inner,
[type="reset"]::-moz-focus-inner,
[type="submit"]::-moz-focus-inner {
    padding: 0;
    border-style: none;
}

input[type="radio"],
input[type="checkbox"] {
    box-sizing: border-box;
    padding: 0;
}

input[type="date"],
input[type="time"],
input[type="datetime-local"],
input[type="month"] {
    -webkit-appearance: listbox;
}

textarea {
    overflow: auto;
    resize: vertical;
}

fieldset {
    min-width: 0;
    padding: 0;
    margin: 0;
    border: 0;
}

legend {
    display: block;
    width: 100%;
    max-width: 100%;
    padding: 0;
    margin-bottom: .5rem;
    font-size: 1.5rem;
    line-height: inherit;
    color: inherit;
    white-space: normal;
}

@media (max-width: 1200px) {
    legend {
        font-size: calc(1.275rem + 0.3vw);
    }
}

progress {
    vertical-align: baseline;
}

[type="number"]::-webkit-inner-spin-button,
[type="number"]::-webkit-outer-spin-button {
    height: auto;
}

[type="search"] {
    outline-offset: -2px;
    -webkit-appearance: none;
}

[type="search"]::-webkit-search-decoration {
    -webkit-appearance: none;
}

::-webkit-file-upload-button {
    font: inherit;
    -webkit-appearance: button;
}

output {
    display: inline-block;
}

summary {
    display: list-item;
    cursor: pointer;
}

template {
    display: none;
}

[hidden] {
    display: none !important;
}

h1, h2, h3, h4, h5, h6,
.h1, .h2, .h3, .h4, .h5, .h6 {
    margin-bottom: 0.5rem;
    font-family: inherit;
    font-weight: 400;
    line-height: 1.3;
    color: #31344b;
}

h1, .h1 {
    font-size: 2.5rem;
}

@media (max-width: 1200px) {
    h1, .h1 {
        font-size: calc(1.375rem + 1.5vw);
    }
}

h2, .h2 {
    font-size: 2rem;
}

@media (max-width: 1200px) {
    h2, .h2 {
        font-size: calc(1.325rem + 0.9vw);
    }
}

h3, .h3 {
    font-size: 1.75rem;
}

@media (max-width: 1200px) {
    h3, .h3 {
        font-size: calc(1.3rem + 0.6vw);
    }
}

h4, .h4 {
    font-size: 1.5rem;
}

@media (max-width: 1200px) {
    h4, .h4 {
        font-size: calc(1.275rem + 0.3vw);
    }
}

h5, .h5 {
    font-size: 1.25rem;
}

h6, .h6 {
    font-size: 1rem;
}

.lead {
    font-size: 1.25rem;
    font-weight: 300;
}

.display-1 {
    font-size: 5rem;
    font-weight: 600;
    line-height: 1.3;
}

@media (max-width: 1200px) {
    .display-1 {
        font-size: calc(1.625rem + 4.5vw);
    }
}

.display-2 {
    font-size: 3.5rem;
    font-weight: 600;
    line-height: 1.3;
}

@media (max-width: 1200px) {
    .display-2 {
        font-size: calc(1.475rem + 2.7vw);
    }
}

.display-3 {
    font-size: 2.5rem;
    font-weight: 600;
    line-height: 1.3;
}

@media (max-width: 1200px) {
    .display-3 {
        font-size: calc(1.375rem + 1.5vw);
    }
}

.display-4 {
    font-size: 1.875rem;
    font-weight: 600;
    line-height: 1.3;
}

@media (max-width: 1200px) {
    .display-4 {
        font-size: calc(1.3125rem + 0.75vw);
    }
}

hr {
    margin-top: 1.5rem;
    margin-bottom: 1.5rem;
    border: 0;
    border-top: 0.0625rem solid rgba(38, 40, 51, 0.05);
}

small,
.small {
    font-size: 80%;
    font-weight: 400;
}

mark,
.mark {
    padding: 0.2em;
    background-color: #fcf8e3;
}

.list-unstyled {
    padding-left: 0;
    list-style: none;
}

.list-inline {
    padding-left: 0;
    list-style: none;
}

.list-inline-item {
    display: inline-block;
}

.list-inline-item:not(:last-child) {
    margin-right: 0.5rem;
}

.initialism {
    font-size: 90%;
    text-transform: uppercase;
}

.blockquote {
    margin-bottom: 1rem;
    font-size: 1.25rem;
}

.blockquote-footer {
    display: block;
    font-size: 80%;
    color: #525480;
}

.blockquote-footer::before {
    content: "\2014\00A0";
}

.img-fluid {
    max-width: 100%;
    height: auto;
}

.img-thumbnail {
    padding: 0.25rem;
    background-color: #e6e7ee;
    border: 0.0625rem solid #e6e7ee;
    border-radius: 0.55rem;
    box-shadow: 0 1px 2px rgba(38, 40, 51, 0.075);
    max-width: 100%;
    height: auto;
}

.figure {
    display: inline-block;
}

.figure-img {
    margin-bottom: 0.5rem;
    line-height: 1;
}

.figure-caption {
    font-size: 90%;
    color: #93a5be;
}

code {
    font-size: 87.5%;
    color: #e83e8c;
    word-break: break-word;
}

a > code {
    color: inherit;
}

kbd {
    padding: 0.2rem 0.4rem;
    font-size: 87.5%;
    color: #ECF0F3;
    background-color: #44476A;
    border-radius: 0.1rem;
    box-shadow: inset 0 -0.1rem 0 rgba(38, 40, 51, 0.25);
}

kbd kbd {
    padding: 0;
    font-size: 100%;
    font-weight: 600;
    box-shadow: none;
}

pre {
    display: block;
    font-size: 87.5%;
    color: #44476A;
}

pre code {
    font-size: inherit;
    color: inherit;
    word-break: normal;
}

.pre-scrollable {
    max-height: 340px;
    overflow-y: scroll;
}

.container {
    width: 100%;
    padding-right: 15px;
    padding-left: 15px;
    margin-right: auto;
    margin-left: auto;
}

@media (min-width: 576px) {
    .container {
        max-width: 540px;
    }
}

@media (min-width: 768px) {
    .container {
        max-width: 720px;
    }
}

@media (min-width: 992px) {
    .container {
        max-width: 960px;
    }
}

@media (min-width: 1200px) {
    .container {
        max-width: 1140px;
    }
}

.container-fluid {
    width: 100%;
    padding-right: 15px;
    padding-left: 15px;
    margin-right: auto;
    margin-left: auto;
}

.row {
    display: flex;
    flex-wrap: wrap;
    margin-right: -15px;
    margin-left: -15px;
}

.no-gutters {
    margin-right: 0;
    margin-left: 0;
}

.no-gutters > .col,
  .no-gutters > [class*="col-"] {
    padding-right: 0;
    padding-left: 0;
}

.col-1, .col-2, .col-3, .col-4, .col-5, .col-6, .col-7, .col-8, .col-9, .col-10, .col-11, .col-12, .col,
.col-auto, .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12, .col-sm,
.col-sm-auto, .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12, .col-md,
.col-md-auto, .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12, .col-lg,
.col-lg-auto, .col-xl-1, .col-xl-2, .col-xl-3, .col-xl-4, .col-xl-5, .col-xl-6, .col-xl-7, .col-xl-8, .col-xl-9, .col-xl-10, .col-xl-11, .col-xl-12, .col-xl,
.col-xl-auto {
    position: relative;
    width: 100%;
    padding-right: 15px;
    padding-left: 15px;
}

.col {
    flex-basis: 0;
    flex-grow: 1;
    max-width: 100%;
}

.col-auto {
    flex: 0 0 auto;
    width: auto;
    max-width: 100%;
}

.col-1 {
    flex: 0 0 8.33333%;
    max-width: 8.33333%;
}

.col-2 {
    flex: 0 0 16.66667%;
    max-width: 16.66667%;
}

.col-3 {
    flex: 0 0 25%;
    max-width: 25%;
}

.col-4 {
    flex: 0 0 33.33333%;
    max-width: 33.33333%;
}

.col-5 {
    flex: 0 0 41.66667%;
    max-width: 41.66667%;
}

.col-6 {
    flex: 0 0 50%;
    max-width: 50%;
}

.col-7 {
    flex: 0 0 58.33333%;
    max-width: 58.33333%;
}

.col-8 {
    flex: 0 0 66.66667%;
    max-width: 66.66667%;
}

.col-9 {
    flex: 0 0 75%;
    max-width: 75%;
}

.col-10 {
    flex: 0 0 83.33333%;
    max-width: 83.33333%;
}

.col-11 {
    flex: 0 0 91.66667%;
    max-width: 91.66667%;
}

.col-12 {
    flex: 0 0 100%;
    max-width: 100%;
}

.order-first {
    order: -1;
}

.order-last {
    order: 13;
}

.order-0 {
    order: 0;
}

.order-1 {
    order: 1;
}

.order-2 {
    order: 2;
}

.order-3 {
    order: 3;
}

.order-4 {
    order: 4;
}

.order-5 {
    order: 5;
}

.order-6 {
    order: 6;
}

.order-7 {
    order: 7;
}

.order-8 {
    order: 8;
}

.order-9 {
    order: 9;
}

.order-10 {
    order: 10;
}

.order-11 {
    order: 11;
}

.order-12 {
    order: 12;
}

.offset-1 {
    margin-left: 8.33333%;
}

.offset-2 {
    margin-left: 16.66667%;
}

.offset-3 {
    margin-left: 25%;
}

.offset-4 {
    margin-left: 33.33333%;
}

.offset-5 {
    margin-left: 41.66667%;
}

.offset-6 {
    margin-left: 50%;
}

.offset-7 {
    margin-left: 58.33333%;
}

.offset-8 {
    margin-left: 66.66667%;
}

.offset-9 {
    margin-left: 75%;
}

.offset-10 {
    margin-left: 83.33333%;
}

.offset-11 {
    margin-left: 91.66667%;
}

@media (min-width: 576px) {
    .col-sm {
        flex-basis: 0;
        flex-grow: 1;
        max-width: 100%;
    }

    .col-sm-auto {
        flex: 0 0 auto;
        width: auto;
        max-width: 100%;
    }

    .col-sm-1 {
        flex: 0 0 8.33333%;
        max-width: 8.33333%;
    }

    .col-sm-2 {
        flex: 0 0 16.66667%;
        max-width: 16.66667%;
    }

    .col-sm-3 {
        flex: 0 0 25%;
        max-width: 25%;
    }

    .col-sm-4 {
        flex: 0 0 33.33333%;
        max-width: 33.33333%;
    }

    .col-sm-5 {
        flex: 0 0 41.66667%;
        max-width: 41.66667%;
    }

    .col-sm-6 {
        flex: 0 0 50%;
        max-width: 50%;
    }

    .col-sm-7 {
        flex: 0 0 58.33333%;
        max-width: 58.33333%;
    }

    .col-sm-8 {
        flex: 0 0 66.66667%;
        max-width: 66.66667%;
    }

    .col-sm-9 {
        flex: 0 0 75%;
        max-width: 75%;
    }

    .col-sm-10 {
        flex: 0 0 83.33333%;
        max-width: 83.33333%;
    }

    .col-sm-11 {
        flex: 0 0 91.66667%;
        max-width: 91.66667%;
    }

    .col-sm-12 {
        flex: 0 0 100%;
        max-width: 100%;
    }

    .order-sm-first {
        order: -1;
    }

    .order-sm-last {
        order: 13;
    }

    .order-sm-0 {
        order: 0;
    }

    .order-sm-1 {
        order: 1;
    }

    .order-sm-2 {
        order: 2;
    }

    .order-sm-3 {
        order: 3;
    }

    .order-sm-4 {
        order: 4;
    }

    .order-sm-5 {
        order: 5;
    }

    .order-sm-6 {
        order: 6;
    }

    .order-sm-7 {
        order: 7;
    }

    .order-sm-8 {
        order: 8;
    }

    .order-sm-9 {
        order: 9;
    }

    .order-sm-10 {
        order: 10;
    }

    .order-sm-11 {
        order: 11;
    }

    .order-sm-12 {
        order: 12;
    }

    .offset-sm-0 {
        margin-left: 0;
    }

    .offset-sm-1 {
        margin-left: 8.33333%;
    }

    .offset-sm-2 {
        margin-left: 16.66667%;
    }

    .offset-sm-3 {
        margin-left: 25%;
    }

    .offset-sm-4 {
        margin-left: 33.33333%;
    }

    .offset-sm-5 {
        margin-left: 41.66667%;
    }

    .offset-sm-6 {
        margin-left: 50%;
    }

    .offset-sm-7 {
        margin-left: 58.33333%;
    }

    .offset-sm-8 {
        margin-left: 66.66667%;
    }

    .offset-sm-9 {
        margin-left: 75%;
    }

    .offset-sm-10 {
        margin-left: 83.33333%;
    }

    .offset-sm-11 {
        margin-left: 91.66667%;
    }
}

@media (min-width: 768px) {
    .col-md {
        flex-basis: 0;
        flex-grow: 1;
        max-width: 100%;
    }

    .col-md-auto {
        flex: 0 0 auto;
        width: auto;
        max-width: 100%;
    }

    .col-md-1 {
        flex: 0 0 8.33333%;
        max-width: 8.33333%;
    }

    .col-md-2 {
        flex: 0 0 16.66667%;
        max-width: 16.66667%;
    }

    .col-md-3 {
        flex: 0 0 25%;
        max-width: 25%;
    }

    .col-md-4 {
        flex: 0 0 33.33333%;
        max-width: 33.33333%;
    }

    .col-md-5 {
        flex: 0 0 41.66667%;
        max-width: 41.66667%;
    }

    .col-md-6 {
        flex: 0 0 50%;
        max-width: 50%;
    }

    .col-md-7 {
        flex: 0 0 58.33333%;
        max-width: 58.33333%;
    }

    .col-md-8 {
        flex: 0 0 66.66667%;
        max-width: 66.66667%;
    }

    .col-md-9 {
        flex: 0 0 75%;
        max-width: 75%;
    }

    .col-md-10 {
        flex: 0 0 83.33333%;
        max-width: 83.33333%;
    }

    .col-md-11 {
        flex: 0 0 91.66667%;
        max-width: 91.66667%;
    }

    .col-md-12 {
        flex: 0 0 100%;
        max-width: 100%;
    }

    .order-md-first {
        order: -1;
    }

    .order-md-last {
        order: 13;
    }

    .order-md-0 {
        order: 0;
    }

    .order-md-1 {
        order: 1;
    }

    .order-md-2 {
        order: 2;
    }

    .order-md-3 {
        order: 3;
    }

    .order-md-4 {
        order: 4;
    }

    .order-md-5 {
        order: 5;
    }

    .order-md-6 {
        order: 6;
    }

    .order-md-7 {
        order: 7;
    }

    .order-md-8 {
        order: 8;
    }

    .order-md-9 {
        order: 9;
    }

    .order-md-10 {
        order: 10;
    }

    .order-md-11 {
        order: 11;
    }

    .order-md-12 {
        order: 12;
    }

    .offset-md-0 {
        margin-left: 0;
    }

    .offset-md-1 {
        margin-left: 8.33333%;
    }

    .offset-md-2 {
        margin-left: 16.66667%;
    }

    .offset-md-3 {
        margin-left: 25%;
    }

    .offset-md-4 {
        margin-left: 33.33333%;
    }

    .offset-md-5 {
        margin-left: 41.66667%;
    }

    .offset-md-6 {
        margin-left: 50%;
    }

    .offset-md-7 {
        margin-left: 58.33333%;
    }

    .offset-md-8 {
        margin-left: 66.66667%;
    }

    .offset-md-9 {
        margin-left: 75%;
    }

    .offset-md-10 {
        margin-left: 83.33333%;
    }

    .offset-md-11 {
        margin-left: 91.66667%;
    }
}

@media (min-width: 992px) {
    .col-lg {
        flex-basis: 0;
        flex-grow: 1;
        max-width: 100%;
    }

    .col-lg-auto {
        flex: 0 0 auto;
        width: auto;
        max-width: 100%;
    }

    .col-lg-1 {
        flex: 0 0 8.33333%;
        max-width: 8.33333%;
    }

    .col-lg-2 {
        flex: 0 0 16.66667%;
        max-width: 16.66667%;
    }

    .col-lg-3 {
        flex: 0 0 25%;
        max-width: 25%;
    }

    .col-lg-4 {
        flex: 0 0 33.33333%;
        max-width: 33.33333%;
    }

    .col-lg-5 {
        flex: 0 0 41.66667%;
        max-width: 41.66667%;
    }

    .col-lg-6 {
        flex: 0 0 50%;
        max-width: 50%;
    }

    .col-lg-7 {
        flex: 0 0 58.33333%;
        max-width: 58.33333%;
    }

    .col-lg-8 {
        flex: 0 0 66.66667%;
        max-width: 66.66667%;
    }

    .col-lg-9 {
        flex: 0 0 75%;
        max-width: 75%;
    }

    .col-lg-10 {
        flex: 0 0 83.33333%;
        max-width: 83.33333%;
    }

    .col-lg-11 {
        flex: 0 0 91.66667%;
        max-width: 91.66667%;
    }

    .col-lg-12 {
        flex: 0 0 100%;
        max-width: 100%;
    }

    .order-lg-first {
        order: -1;
    }

    .order-lg-last {
        order: 13;
    }

    .order-lg-0 {
        order: 0;
    }

    .order-lg-1 {
        order: 1;
    }

    .order-lg-2 {
        order: 2;
    }

    .order-lg-3 {
        order: 3;
    }

    .order-lg-4 {
        order: 4;
    }

    .order-lg-5 {
        order: 5;
    }

    .order-lg-6 {
        order: 6;
    }

    .order-lg-7 {
        order: 7;
    }

    .order-lg-8 {
        order: 8;
    }

    .order-lg-9 {
        order: 9;
    }

    .order-lg-10 {
        order: 10;
    }

    .order-lg-11 {
        order: 11;
    }

    .order-lg-12 {
        order: 12;
    }

    .offset-lg-0 {
        margin-left: 0;
    }

    .offset-lg-1 {
        margin-left: 8.33333%;
    }

    .offset-lg-2 {
        margin-left: 16.66667%;
    }

    .offset-lg-3 {
        margin-left: 25%;
    }

    .offset-lg-4 {
        margin-left: 33.33333%;
    }

    .offset-lg-5 {
        margin-left: 41.66667%;
    }

    .offset-lg-6 {
        margin-left: 50%;
    }

    .offset-lg-7 {
        margin-left: 58.33333%;
    }

    .offset-lg-8 {
        margin-left: 66.66667%;
    }

    .offset-lg-9 {
        margin-left: 75%;
    }

    .offset-lg-10 {
        margin-left: 83.33333%;
    }

    .offset-lg-11 {
        margin-left: 91.66667%;
    }
}

@media (min-width: 1200px) {
    .col-xl {
        flex-basis: 0;
        flex-grow: 1;
        max-width: 100%;
    }

    .col-xl-auto {
        flex: 0 0 auto;
        width: auto;
        max-width: 100%;
    }

    .col-xl-1 {
        flex: 0 0 8.33333%;
        max-width: 8.33333%;
    }

    .col-xl-2 {
        flex: 0 0 16.66667%;
        max-width: 16.66667%;
    }

    .col-xl-3 {
        flex: 0 0 25%;
        max-width: 25%;
    }

    .col-xl-4 {
        flex: 0 0 33.33333%;
        max-width: 33.33333%;
    }

    .col-xl-5 {
        flex: 0 0 41.66667%;
        max-width: 41.66667%;
    }

    .col-xl-6 {
        flex: 0 0 50%;
        max-width: 50%;
    }

    .col-xl-7 {
        flex: 0 0 58.33333%;
        max-width: 58.33333%;
    }

    .col-xl-8 {
        flex: 0 0 66.66667%;
        max-width: 66.66667%;
    }

    .col-xl-9 {
        flex: 0 0 75%;
        max-width: 75%;
    }

    .col-xl-10 {
        flex: 0 0 83.33333%;
        max-width: 83.33333%;
    }

    .col-xl-11 {
        flex: 0 0 91.66667%;
        max-width: 91.66667%;
    }

    .col-xl-12 {
        flex: 0 0 100%;
        max-width: 100%;
    }

    .order-xl-first {
        order: -1;
    }

    .order-xl-last {
        order: 13;
    }

    .order-xl-0 {
        order: 0;
    }

    .order-xl-1 {
        order: 1;
    }

    .order-xl-2 {
        order: 2;
    }

    .order-xl-3 {
        order: 3;
    }

    .order-xl-4 {
        order: 4;
    }

    .order-xl-5 {
        order: 5;
    }

    .order-xl-6 {
        order: 6;
    }

    .order-xl-7 {
        order: 7;
    }

    .order-xl-8 {
        order: 8;
    }

    .order-xl-9 {
        order: 9;
    }

    .order-xl-10 {
        order: 10;
    }

    .order-xl-11 {
        order: 11;
    }

    .order-xl-12 {
        order: 12;
    }

    .offset-xl-0 {
        margin-left: 0;
    }

    .offset-xl-1 {
        margin-left: 8.33333%;
    }

    .offset-xl-2 {
        margin-left: 16.66667%;
    }

    .offset-xl-3 {
        margin-left: 25%;
    }

    .offset-xl-4 {
        margin-left: 33.33333%;
    }

    .offset-xl-5 {
        margin-left: 41.66667%;
    }

    .offset-xl-6 {
        margin-left: 50%;
    }

    .offset-xl-7 {
        margin-left: 58.33333%;
    }

    .offset-xl-8 {
        margin-left: 66.66667%;
    }

    .offset-xl-9 {
        margin-left: 75%;
    }

    .offset-xl-10 {
        margin-left: 83.33333%;
    }

    .offset-xl-11 {
        margin-left: 91.66667%;
    }
}

.table {
    width: 100%;
    margin-bottom: 1rem;
    color: #44476A;
    background-color: transparent;
}

.table th,
  .table td {
    padding: 1rem;
    vertical-align: top;
    border-top: 0.0625rem solid #D1D9E6;
}

.table thead th {
    vertical-align: bottom;
    border-bottom: 0.125rem solid #D1D9E6;
}

.table tbody + tbody {
    border-top: 0.125rem solid #D1D9E6;
}

.table-sm th,
.table-sm td {
    padding: 0.3rem;
}

.table-bordered {
    border: 0.0625rem solid #D1D9E6;
}

.table-bordered th,
  .table-bordered td {
    border: 0.0625rem solid #D1D9E6;
}

.table-bordered thead th,
  .table-bordered thead td {
    border-bottom-width: 0.125rem;
}

.table-borderless th,
.table-borderless td,
.table-borderless thead th,
.table-borderless tbody + tbody {
    border: 0;
}

.table-striped tbody tr:nth-of-type(odd) {
    background-color: rgba(38, 40, 51, 0.05);
}

.table-hover tbody tr:hover {
    color: #44476A;
    background-color: rgba(38, 40, 51, 0.03);
}

.table-primary,
.table-primary > th,
.table-primary > td {
    background-color: #eaedf2;
}

.table-primary th,
.table-primary td,
.table-primary thead th,
.table-primary tbody + tbody {
    border-color: #e9ebf0;
}

.table-hover .table-primary:hover {
    background-color: #dae0e8;
}

.table-hover .table-primary:hover > td,
  .table-hover .table-primary:hover > th {
    background-color: #dae0e8;
}

.table-secondary,
.table-secondary > th,
.table-secondary > td {
    background-color: #b7c2e7;
}

.table-secondary th,
.table-secondary td,
.table-secondary thead th,
.table-secondary tbody + tbody {
    border-color: #899bdd;
}

.table-hover .table-secondary:hover {
    background-color: #a4b2e1;
}

.table-hover .table-secondary:hover > td,
  .table-hover .table-secondary:hover > th {
    background-color: #a4b2e1;
}

.table-success,
.table-success > th,
.table-success > td {
    background-color: #b1c9c4;
}

.table-success th,
.table-success td,
.table-success thead th,
.table-success tbody + tbody {
    border-color: #7ea79c;
}

.table-hover .table-success:hover {
    background-color: #a2bfb9;
}

.table-hover .table-success:hover > td,
  .table-hover .table-success:hover > th {
    background-color: #a2bfb9;
}

.table-info,
.table-info > th,
.table-info > td {
    background-color: #aac5e1;
}

.table-info th,
.table-info td,
.table-info thead th,
.table-info tbody + tbody {
    border-color: #71a0d2;
}

.table-hover .table-info:hover {
    background-color: #97b8da;
}

.table-hover .table-info:hover > td,
  .table-hover .table-info:hover > th {
    background-color: #97b8da;
}

.table-warning,
.table-warning > th,
.table-warning > td {
    background-color: #eddfaf;
}

.table-warning th,
.table-warning td,
.table-warning thead th,
.table-warning tbody + tbody {
    border-color: #eed175;
}

.table-hover .table-warning:hover {
    background-color: #e8d79a;
}

.table-hover .table-warning:hover > td,
  .table-hover .table-warning:hover > th {
    background-color: #e8d79a;
}

.table-danger,
.table-danger > th,
.table-danger > td {
    background-color: #d9b5bb;
}

.table-danger th,
.table-danger td,
.table-danger thead th,
.table-danger tbody + tbody {
    border-color: #c9838c;
}

.table-hover .table-danger:hover {
    background-color: #d0a4ac;
}

.table-hover .table-danger:hover > td,
  .table-hover .table-danger:hover > th {
    background-color: #d0a4ac;
}

.table-light,
.table-light > th,
.table-light > td {
    background-color: #e4eaef;
}

.table-light th,
.table-light td,
.table-light thead th,
.table-light tbody + tbody {
    border-color: #dee4ec;
}

.table-hover .table-light:hover {
    background-color: #d4dee6;
}

.table-hover .table-light:hover > td,
  .table-hover .table-light:hover > th {
    background-color: #d4dee6;
}

.table-dark,
.table-dark > th,
.table-dark > td {
    background-color: #b8bbc4;
}

.table-dark th,
.table-dark td,
.table-dark thead th,
.table-dark tbody + tbody {
    border-color: #8b8e9c;
}

.table-hover .table-dark:hover {
    background-color: #aaaeb8;
}

.table-hover .table-dark:hover > td,
  .table-hover .table-dark:hover > th {
    background-color: #aaaeb8;
}

.table-default,
.table-default > th,
.table-default > td {
    background-color: #b5b8bd;
}

.table-default th,
.table-default td,
.table-default thead th,
.table-default tbody + tbody {
    border-color: #85888f;
}

.table-hover .table-default:hover {
    background-color: #a8abb1;
}

.table-hover .table-default:hover > td,
  .table-hover .table-default:hover > th {
    background-color: #a8abb1;
}

.table-white,
.table-white > th,
.table-white > td {
    background-color: #ecf0f3;
}

.table-white th,
.table-white td,
.table-white thead th,
.table-white tbody + tbody {
    border-color: #ecf0f3;
}

.table-hover .table-white:hover {
    background-color: #dce4e9;
}

.table-hover .table-white:hover > td,
  .table-hover .table-white:hover > th {
    background-color: #dce4e9;
}

.table-gray,
.table-gray > th,
.table-gray > td {
    background-color: #bdc1cd;
}

.table-gray th,
.table-gray td,
.table-gray thead th,
.table-gray tbody + tbody {
    border-color: #9598ac;
}

.table-hover .table-gray:hover {
    background-color: #aeb3c2;
}

.table-hover .table-gray:hover > td,
  .table-hover .table-gray:hover > th {
    background-color: #aeb3c2;
}

.table-neutral,
.table-neutral > th,
.table-neutral > td {
    background-color: #ecf0f3;
}

.table-neutral th,
.table-neutral td,
.table-neutral thead th,
.table-neutral tbody + tbody {
    border-color: #ecf0f3;
}

.table-hover .table-neutral:hover {
    background-color: #dce4e9;
}

.table-hover .table-neutral:hover > td,
  .table-hover .table-neutral:hover > th {
    background-color: #dce4e9;
}

.table-soft,
.table-soft > th,
.table-soft > td {
    background-color: #eaedf2;
}

.table-soft th,
.table-soft td,
.table-soft thead th,
.table-soft tbody + tbody {
    border-color: #e9ebf0;
}

.table-hover .table-soft:hover {
    background-color: #dae0e8;
}

.table-hover .table-soft:hover > td,
  .table-hover .table-soft:hover > th {
    background-color: #dae0e8;
}

.table-black,
.table-black > th,
.table-black > td {
    background-color: #b5b8bd;
}

.table-black th,
.table-black td,
.table-black thead th,
.table-black tbody + tbody {
    border-color: #85888f;
}

.table-hover .table-black:hover {
    background-color: #a8abb1;
}

.table-hover .table-black:hover > td,
  .table-hover .table-black:hover > th {
    background-color: #a8abb1;
}

.table-purple,
.table-purple > th,
.table-purple > td {
    background-color: #c9bfe5;
}

.table-purple th,
.table-purple td,
.table-purple thead th,
.table-purple tbody + tbody {
    border-color: #ab96d9;
}

.table-hover .table-purple:hover {
    background-color: #baadde;
}

.table-hover .table-purple:hover > td,
  .table-hover .table-purple:hover > th {
    background-color: #baadde;
}

.table-gray-100,
.table-gray-100 > th,
.table-gray-100 > td {
    background-color: #eef2f5;
}

.table-gray-100 th,
.table-gray-100 td,
.table-gray-100 thead th,
.table-gray-100 tbody + tbody {
    border-color: #f0f4f7;
}

.table-hover .table-gray-100:hover {
    background-color: #dee6ec;
}

.table-hover .table-gray-100:hover > td,
  .table-hover .table-gray-100:hover > th {
    background-color: #dee6ec;
}

.table-gray-200,
.table-gray-200 > th,
.table-gray-200 > td {
    background-color: #f0f3f6;
}

.table-gray-200 th,
.table-gray-200 td,
.table-gray-200 thead th,
.table-gray-200 tbody + tbody {
    border-color: #f3f6f9;
}

.table-hover .table-gray-200:hover {
    background-color: #e0e6ec;
}

.table-hover .table-gray-200:hover > td,
  .table-hover .table-gray-200:hover > th {
    background-color: #e0e6ec;
}

.table-gray-300,
.table-gray-300 > th,
.table-gray-300 > td {
    background-color: #eaedf2;
}

.table-gray-300 th,
.table-gray-300 td,
.table-gray-300 thead th,
.table-gray-300 tbody + tbody {
    border-color: #e9ebf0;
}

.table-hover .table-gray-300:hover {
    background-color: #dae0e8;
}

.table-hover .table-gray-300:hover > td,
  .table-hover .table-gray-300:hover > th {
    background-color: #dae0e8;
}

.table-gray-400,
.table-gray-400 > th,
.table-gray-400 > td {
    background-color: #e4eaef;
}

.table-gray-400 th,
.table-gray-400 td,
.table-gray-400 thead th,
.table-gray-400 tbody + tbody {
    border-color: #dee4ec;
}

.table-hover .table-gray-400:hover {
    background-color: #d4dee6;
}

.table-hover .table-gray-400:hover > td,
  .table-hover .table-gray-400:hover > th {
    background-color: #d4dee6;
}

.table-gray-500,
.table-gray-500 > th,
.table-gray-500 > td {
    background-color: #dbe1e9;
}

.table-gray-500 th,
.table-gray-500 td,
.table-gray-500 thead th,
.table-gray-500 tbody + tbody {
    border-color: #cdd5e0;
}

.table-hover .table-gray-500:hover {
    background-color: #cbd4df;
}

.table-hover .table-gray-500:hover > td,
  .table-hover .table-gray-500:hover > th {
    background-color: #cbd4df;
}

.table-gray-600,
.table-gray-600 > th,
.table-gray-600 > td {
    background-color: #d3dbe4;
}

.table-gray-600 th,
.table-gray-600 td,
.table-gray-600 thead th,
.table-gray-600 tbody + tbody {
    border-color: #bec9d7;
}

.table-hover .table-gray-600:hover {
    background-color: #c3ceda;
}

.table-hover .table-gray-600:hover > td,
  .table-hover .table-gray-600:hover > th {
    background-color: #c3ceda;
}

.table-gray-700,
.table-gray-700 > th,
.table-gray-700 > td {
    background-color: #c6cfdb;
}

.table-gray-700 th,
.table-gray-700 td,
.table-gray-700 thead th,
.table-gray-700 tbody + tbody {
    border-color: #a6b2c7;
}

.table-hover .table-gray-700:hover {
    background-color: #b6c2d1;
}

.table-hover .table-gray-700:hover > td,
  .table-hover .table-gray-700:hover > th {
    background-color: #b6c2d1;
}

.table-gray-800,
.table-gray-800 > th,
.table-gray-800 > td {
    background-color: #c1c4d3;
}

.table-gray-800 th,
.table-gray-800 td,
.table-gray-800 thead th,
.table-gray-800 tbody + tbody {
    border-color: #9c9fb7;
}

.table-hover .table-gray-800:hover {
    background-color: #b2b6c8;
}

.table-hover .table-gray-800:hover > td,
  .table-hover .table-gray-800:hover > th {
    background-color: #b2b6c8;
}

.table-facebook,
.table-facebook > th,
.table-facebook > td {
    background-color: #bac6da;
}

.table-facebook th,
.table-facebook td,
.table-facebook thead th,
.table-facebook tbody + tbody {
    border-color: #90a1c4;
}

.table-hover .table-facebook:hover {
    background-color: #a9b8d1;
}

.table-hover .table-facebook:hover > td,
  .table-hover .table-facebook:hover > th {
    background-color: #a9b8d1;
}

.table-dribbble,
.table-dribbble > th,
.table-dribbble > td {
    background-color: #ebc2d5;
}

.table-dribbble th,
.table-dribbble td,
.table-dribbble thead th,
.table-dribbble tbody + tbody {
    border-color: #eb9bbc;
}

.table-hover .table-dribbble:hover {
    background-color: #e5afc8;
}

.table-hover .table-dribbble:hover > td,
  .table-hover .table-dribbble:hover > th {
    background-color: #e5afc8;
}

.table-github,
.table-github > th,
.table-github > td {
    background-color: #b3b6b8;
}

.table-github th,
.table-github td,
.table-github thead th,
.table-github tbody + tbody {
    border-color: #838586;
}

.table-hover .table-github:hover {
    background-color: #a6a9ac;
}

.table-hover .table-github:hover > td,
  .table-hover .table-github:hover > th {
    background-color: #a6a9ac;
}

.table-behance,
.table-behance > th,
.table-behance > td {
    background-color: #aac5f6;
}

.table-behance th,
.table-behance td,
.table-behance thead th,
.table-behance tbody + tbody {
    border-color: #71a0f9;
}

.table-hover .table-behance:hover {
    background-color: #93b5f4;
}

.table-hover .table-behance:hover > td,
  .table-hover .table-behance:hover > th {
    background-color: #93b5f4;
}

.table-twitter,
.table-twitter > th,
.table-twitter > td {
    background-color: #b2daf3;
}

.table-twitter th,
.table-twitter td,
.table-twitter thead th,
.table-twitter tbody + tbody {
    border-color: #80c7f2;
}

.table-hover .table-twitter:hover {
    background-color: #9ccff0;
}

.table-hover .table-twitter:hover > td,
  .table-hover .table-twitter:hover > th {
    background-color: #9ccff0;
}

.table-slack,
.table-slack > th,
.table-slack > td {
    background-color: #baded4;
}

.table-slack th,
.table-slack td,
.table-slack thead th,
.table-slack tbody + tbody {
    border-color: #8fceba;
}

.table-hover .table-slack:hover {
    background-color: #a9d6c9;
}

.table-hover .table-slack:hover > td,
  .table-hover .table-slack:hover > th {
    background-color: #a9d6c9;
}

.table-active,
.table-active > th,
.table-active > td {
    background-color: rgba(38, 40, 51, 0.03);
}

.table-hover .table-active:hover {
    background-color: rgba(27, 29, 36, 0.03);
}

.table-hover .table-active:hover > td,
  .table-hover .table-active:hover > th {
    background-color: rgba(27, 29, 36, 0.03);
}

.table .thead-dark th {
    color: #e6e7ee;
    background-color: #44476A;
    border-color: #535781;
}

.table .thead-light th {
    color: #66799e;
    background-color: #fafbfe;
    border-color: #D1D9E6;
}

.table-dark {
    color: #e6e7ee;
    background-color: #44476A;
}

.table-dark th,
  .table-dark td,
  .table-dark thead th {
    border-color: #535781;
}

.table-dark.table-bordered {
    border: 0;
}

.table-dark.table-striped tbody tr:nth-of-type(odd) {
    background-color: rgba(236, 240, 243, 0.05);
}

.table-dark.table-hover tbody tr:hover {
    color: #e6e7ee;
    background-color: rgba(236, 240, 243, 0.075);
}

@media (max-width: 575.98px) {
    .table-responsive-sm {
        display: block;
        width: 100%;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
    }

    .table-responsive-sm > .table-bordered {
        border: 0;
    }
}

@media (max-width: 767.98px) {
    .table-responsive-md {
        display: block;
        width: 100%;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
    }

    .table-responsive-md > .table-bordered {
        border: 0;
    }
}

@media (max-width: 991.98px) {
    .table-responsive-lg {
        display: block;
        width: 100%;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
    }

    .table-responsive-lg > .table-bordered {
        border: 0;
    }
}

@media (max-width: 1199.98px) {
    .table-responsive-xl {
        display: block;
        width: 100%;
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
    }

    .table-responsive-xl > .table-bordered {
        border: 0;
    }
}

.table-responsive {
    display: block;
    width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
}

.table-responsive > .table-bordered {
    border: 0;
}

.form-control {
    display: block;
    width: 100%;
    height: calc(1.5em + 1.2rem + 0.0625rem);
    padding: 0.6rem 0.75rem;
    font-size: 1rem;
    font-weight: 300;
    line-height: 1.5;
    color: #44476A;
    background-color: #e6e7ee;
    background-clip: padding-box;
    border: 0.0625rem solid #D1D9E6;
    border-radius: 0.55rem;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    transition: all 0.3s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
    .form-control {
        transition: none;
    }
}

.form-control::-ms-expand {
    background-color: transparent;
    border: 0;
}

.form-control:focus {
    color: #44476A;
    background-color: #e6e7ee;
    border-color: #D1D9E6;
    outline: 0;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, none;
}

.form-control::placeholder {
    color: #44476A;
    opacity: 1;
}

.form-control:disabled, .form-control[readonly] {
    background-color: #e6e7ee;
    opacity: 1;
}

select.form-control:focus::-ms-value {
    color: #44476A;
    background-color: #e6e7ee;
}

.form-control-file,
.form-control-range {
    display: block;
    width: 100%;
}

.col-form-label {
    padding-top: calc(0.6rem + 0.0625rem);
    padding-bottom: calc(0.6rem + 0.0625rem);
    margin-bottom: 0;
    font-size: inherit;
    line-height: 1.5;
}

.col-form-label-lg {
    padding-top: calc(0.875rem + 0.0625rem);
    padding-bottom: calc(0.875rem + 0.0625rem);
    font-size: 1.25rem;
    line-height: 1.5;
}

.col-form-label-sm {
    padding-top: calc(0.45rem + 0.0625rem);
    padding-bottom: calc(0.45rem + 0.0625rem);
    font-size: 0.875rem;
    line-height: 1.5;
}

.form-control-plaintext {
    display: block;
    width: 100%;
    padding-top: 0.6rem;
    padding-bottom: 0.6rem;
    margin-bottom: 0;
    line-height: 1.5;
    color: #44476A;
    background-color: transparent;
    border: solid transparent;
    border-width: 0.0625rem 0;
}

.form-control-plaintext.form-control-sm, .form-control-plaintext.form-control-lg {
    padding-right: 0;
    padding-left: 0;
}

.form-control-sm {
    height: calc(1.5em + 0.9rem + 0.0625rem);
    padding: 0.45rem 0.5rem;
    font-size: 0.875rem;
    line-height: 1.5;
    border-radius: 0.1rem;
}

.form-control-lg {
    height: calc(1.5em + 1.75rem + 0.0625rem);
    padding: 0.875rem 1rem;
    font-size: 1.25rem;
    line-height: 1.5;
    border-radius: 0.3rem;
}

select.form-control[size], select.form-control[multiple] {
    height: auto;
}

textarea.form-control {
    height: auto;
}

.form-group {
    margin-bottom: 1rem;
}

.form-text {
    display: block;
    margin-top: 0.25rem;
}

.form-row {
    display: flex;
    flex-wrap: wrap;
    margin-right: -5px;
    margin-left: -5px;
}

.form-row > .col,
  .form-row > [class*="col-"] {
    padding-right: 5px;
    padding-left: 5px;
}

.form-check {
    position: relative;
    display: block;
    padding-left: 1.25rem;
}

.form-check-input {
    position: absolute;
    margin-top: 0.3rem;
    margin-left: -1.25rem;
}

.form-check-input:disabled ~ .form-check-label {
    color: #525480;
}

.form-check-label {
    margin-bottom: 0;
}

.form-check-inline {
    display: inline-flex;
    align-items: center;
    padding-left: 0;
    margin-right: 0.75rem;
}

.form-check-inline .form-check-input {
    position: static;
    margin-top: 0;
    margin-right: 0.3125rem;
    margin-left: 0;
}

.valid-feedback {
    display: none;
    width: 100%;
    margin-top: 0.25rem;
    font-size: 80%;
    color: #18634B;
}

.valid-tooltip {
    position: absolute;
    top: 100%;
    z-index: 5;
    display: none;
    max-width: 100%;
    padding: 0.25rem 0.5rem;
    margin-top: .1rem;
    font-size: 0.875rem;
    line-height: 1.5;
    color: #ECF0F3;
    background-color: rgba(24, 99, 75, 0.9);
    border-radius: 0.55rem;
}

.was-validated .form-control:valid, .form-control.is-valid {
    border-color: #18634B;
    padding-right: calc(1.5em + 1.2rem);
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%2318634B' d='M2.3 6.73L.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1z'/%3e%3c/svg%3e");
    background-repeat: no-repeat;
    background-position: center right calc(0.375em + 0.3rem);
    background-size: calc(0.4875rem + 0.6rem) calc(0.4875rem + 0.6rem);
}

.was-validated .form-control:valid:focus, .form-control.is-valid:focus {
    border-color: #18634B;
    box-shadow: 0 0 0 0 rgba(24, 99, 75, 0.25);
}

.was-validated .form-control:valid ~ .valid-feedback,
  .was-validated .form-control:valid ~ .valid-tooltip, .form-control.is-valid ~ .valid-feedback,
  .form-control.is-valid ~ .valid-tooltip {
    display: block;
}

.was-validated textarea.form-control:valid, textarea.form-control.is-valid {
    padding-right: calc(1.5em + 1.2rem);
    background-position: top calc(0.375em + 0.3rem) right calc(0.375em + 0.3rem);
}

.was-validated .custom-select:valid, .custom-select.is-valid {
    border-color: #18634B;
    padding-right: calc((1em + 1.2rem) * 3 / 4 + 1.75rem);
    background: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 5'%3e%3cpath fill='%23525480' d='M2 0L0 2h4zm0 5L0 3h4z'/%3e%3c/svg%3e") no-repeat right 0.75rem center/8px 10px, url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 8 8'%3e%3cpath fill='%2318634B' d='M2.3 6.73L.6 4.53c-.4-1.04.46-1.4 1.1-.8l1.1 1.4 3.4-3.8c.6-.63 1.6-.27 1.2.7l-4 4.6c-.43.5-.8.4-1.1.1z'/%3e%3c/svg%3e") #e6e7ee no-repeat center right 1.75rem/calc(0.4875rem + 0.6rem) calc(0.4875rem + 0.6rem);
}

.was-validated .custom-select:valid:focus, .custom-select.is-valid:focus {
    border-color: #18634B;
    box-shadow: 0 0 0 0 rgba(24, 99, 75, 0.25);
}

.was-validated .custom-select:valid ~ .valid-feedback,
  .was-validated .custom-select:valid ~ .valid-tooltip, .custom-select.is-valid ~ .valid-feedback,
  .custom-select.is-valid ~ .valid-tooltip {
    display: block;
}

.was-validated .form-control-file:valid ~ .valid-feedback,
.was-validated .form-control-file:valid ~ .valid-tooltip, .form-control-file.is-valid ~ .valid-feedback,
.form-control-file.is-valid ~ .valid-tooltip {
    display: block;
}

.was-validated .form-check-input:valid ~ .form-check-label, .form-check-input.is-valid ~ .form-check-label {
    color: #18634B;
}

.was-validated .form-check-input:valid ~ .valid-feedback,
.was-validated .form-check-input:valid ~ .valid-tooltip, .form-check-input.is-valid ~ .valid-feedback,
.form-check-input.is-valid ~ .valid-tooltip {
    display: block;
}

.was-validated .custom-control-input:valid ~ .custom-control-label, .custom-control-input.is-valid ~ .custom-control-label {
    color: #18634B;
}

.was-validated .custom-control-input:valid ~ .custom-control-label::before, .custom-control-input.is-valid ~ .custom-control-label::before {
    border-color: #18634B;
}

.was-validated .custom-control-input:valid ~ .valid-feedback,
.was-validated .custom-control-input:valid ~ .valid-tooltip, .custom-control-input.is-valid ~ .valid-feedback,
.custom-control-input.is-valid ~ .valid-tooltip {
    display: block;
}

.was-validated .custom-control-input:valid:checked ~ .custom-control-label::before, .custom-control-input.is-valid:checked ~ .custom-control-label::before {
    border-color: #228c6a;
    background-color: #228c6a;
}

.was-validated .custom-control-input:valid:focus ~ .custom-control-label::before, .custom-control-input.is-valid:focus ~ .custom-control-label::before {
    box-shadow: 0 0 0 0 rgba(24, 99, 75, 0.25);
}

.was-validated .custom-control-input:valid:focus:not(:checked) ~ .custom-control-label::before, .custom-control-input.is-valid:focus:not(:checked) ~ .custom-control-label::before {
    border-color: #18634B;
}

.was-validated .custom-file-input:valid ~ .custom-file-label, .custom-file-input.is-valid ~ .custom-file-label {
    border-color: #18634B;
}

.was-validated .custom-file-input:valid ~ .valid-feedback,
.was-validated .custom-file-input:valid ~ .valid-tooltip, .custom-file-input.is-valid ~ .valid-feedback,
.custom-file-input.is-valid ~ .valid-tooltip {
    display: block;
}

.was-validated .custom-file-input:valid:focus ~ .custom-file-label, .custom-file-input.is-valid:focus ~ .custom-file-label {
    border-color: #18634B;
    box-shadow: 0 0 0 0 rgba(24, 99, 75, 0.25);
}

.invalid-feedback {
    display: none;
    width: 100%;
    margin-top: 0.25rem;
    font-size: 80%;
    color: #A91E2C;
}

.invalid-tooltip {
    position: absolute;
    top: 100%;
    z-index: 5;
    display: none;
    max-width: 100%;
    padding: 0.25rem 0.5rem;
    margin-top: .1rem;
    font-size: 0.875rem;
    line-height: 1.5;
    color: #ECF0F3;
    background-color: rgba(169, 30, 44, 0.9);
    border-radius: 0.55rem;
}

.was-validated .form-control:invalid, .form-control.is-invalid {
    border-color: #A91E2C;
    padding-right: calc(1.5em + 1.2rem);
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='%23A91E2C' viewBox='-2 -2 7 7'%3e%3cpath stroke='%23A91E2C' d='M0 0l3 3m0-3L0 3'/%3e%3ccircle r='.5'/%3e%3ccircle cx='3' r='.5'/%3e%3ccircle cy='3' r='.5'/%3e%3ccircle cx='3' cy='3' r='.5'/%3e%3c/svg%3E");
    background-repeat: no-repeat;
    background-position: center right calc(0.375em + 0.3rem);
    background-size: calc(0.4875rem + 0.6rem) calc(0.4875rem + 0.6rem);
}

.was-validated .form-control:invalid:focus, .form-control.is-invalid:focus {
    border-color: #A91E2C;
    box-shadow: 0 0 0 0 rgba(169, 30, 44, 0.25);
}

.was-validated .form-control:invalid ~ .invalid-feedback,
  .was-validated .form-control:invalid ~ .invalid-tooltip, .form-control.is-invalid ~ .invalid-feedback,
  .form-control.is-invalid ~ .invalid-tooltip {
    display: block;
}

.was-validated textarea.form-control:invalid, textarea.form-control.is-invalid {
    padding-right: calc(1.5em + 1.2rem);
    background-position: top calc(0.375em + 0.3rem) right calc(0.375em + 0.3rem);
}

.was-validated .custom-select:invalid, .custom-select.is-invalid {
    border-color: #A91E2C;
    padding-right: calc((1em + 1.2rem) * 3 / 4 + 1.75rem);
    background: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 5'%3e%3cpath fill='%23525480' d='M2 0L0 2h4zm0 5L0 3h4z'/%3e%3c/svg%3e") no-repeat right 0.75rem center/8px 10px, url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='%23A91E2C' viewBox='-2 -2 7 7'%3e%3cpath stroke='%23A91E2C' d='M0 0l3 3m0-3L0 3'/%3e%3ccircle r='.5'/%3e%3ccircle cx='3' r='.5'/%3e%3ccircle cy='3' r='.5'/%3e%3ccircle cx='3' cy='3' r='.5'/%3e%3c/svg%3E") #e6e7ee no-repeat center right 1.75rem/calc(0.4875rem + 0.6rem) calc(0.4875rem + 0.6rem);
}

.was-validated .custom-select:invalid:focus, .custom-select.is-invalid:focus {
    border-color: #A91E2C;
    box-shadow: 0 0 0 0 rgba(169, 30, 44, 0.25);
}

.was-validated .custom-select:invalid ~ .invalid-feedback,
  .was-validated .custom-select:invalid ~ .invalid-tooltip, .custom-select.is-invalid ~ .invalid-feedback,
  .custom-select.is-invalid ~ .invalid-tooltip {
    display: block;
}

.was-validated .form-control-file:invalid ~ .invalid-feedback,
.was-validated .form-control-file:invalid ~ .invalid-tooltip, .form-control-file.is-invalid ~ .invalid-feedback,
.form-control-file.is-invalid ~ .invalid-tooltip {
    display: block;
}

.was-validated .form-check-input:invalid ~ .form-check-label, .form-check-input.is-invalid ~ .form-check-label {
    color: #A91E2C;
}

.was-validated .form-check-input:invalid ~ .invalid-feedback,
.was-validated .form-check-input:invalid ~ .invalid-tooltip, .form-check-input.is-invalid ~ .invalid-feedback,
.form-check-input.is-invalid ~ .invalid-tooltip {
    display: block;
}

.was-validated .custom-control-input:invalid ~ .custom-control-label, .custom-control-input.is-invalid ~ .custom-control-label {
    color: #A91E2C;
}

.was-validated .custom-control-input:invalid ~ .custom-control-label::before, .custom-control-input.is-invalid ~ .custom-control-label::before {
    border-color: #A91E2C;
}

.was-validated .custom-control-input:invalid ~ .invalid-feedback,
.was-validated .custom-control-input:invalid ~ .invalid-tooltip, .custom-control-input.is-invalid ~ .invalid-feedback,
.custom-control-input.is-invalid ~ .invalid-tooltip {
    display: block;
}

.was-validated .custom-control-input:invalid:checked ~ .custom-control-label::before, .custom-control-input.is-invalid:checked ~ .custom-control-label::before {
    border-color: #d42637;
    background-color: #d42637;
}

.was-validated .custom-control-input:invalid:focus ~ .custom-control-label::before, .custom-control-input.is-invalid:focus ~ .custom-control-label::before {
    box-shadow: 0 0 0 0 rgba(169, 30, 44, 0.25);
}

.was-validated .custom-control-input:invalid:focus:not(:checked) ~ .custom-control-label::before, .custom-control-input.is-invalid:focus:not(:checked) ~ .custom-control-label::before {
    border-color: #A91E2C;
}

.was-validated .custom-file-input:invalid ~ .custom-file-label, .custom-file-input.is-invalid ~ .custom-file-label {
    border-color: #A91E2C;
}

.was-validated .custom-file-input:invalid ~ .invalid-feedback,
.was-validated .custom-file-input:invalid ~ .invalid-tooltip, .custom-file-input.is-invalid ~ .invalid-feedback,
.custom-file-input.is-invalid ~ .invalid-tooltip {
    display: block;
}

.was-validated .custom-file-input:invalid:focus ~ .custom-file-label, .custom-file-input.is-invalid:focus ~ .custom-file-label {
    border-color: #A91E2C;
    box-shadow: 0 0 0 0 rgba(169, 30, 44, 0.25);
}

.form-inline {
    display: flex;
    flex-flow: row wrap;
    align-items: center;
}

.form-inline .form-check {
    width: 100%;
}

@media (min-width: 576px) {
    .form-inline label {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 0;
    }

    .form-inline .form-group {
        display: flex;
        flex: 0 0 auto;
        flex-flow: row wrap;
        align-items: center;
        margin-bottom: 0;
    }

    .form-inline .form-control {
        display: inline-block;
        width: auto;
        vertical-align: middle;
    }

    .form-inline .form-control-plaintext {
        display: inline-block;
    }

    .form-inline .input-group,
    .form-inline .custom-select {
        width: auto;
    }

    .form-inline .form-check {
        display: flex;
        align-items: center;
        justify-content: center;
        width: auto;
        padding-left: 0;
    }

    .form-inline .form-check-input {
        position: relative;
        flex-shrink: 0;
        margin-top: 0;
        margin-right: 0.25rem;
        margin-left: 0;
    }

    .form-inline .custom-control {
        align-items: center;
        justify-content: center;
    }

    .form-inline .custom-control-label {
        margin-bottom: 0;
    }
}

.btn {
    display: inline-block;
    font-weight: 400;
    color: #44476A;
    text-align: center;
    vertical-align: middle;
    -webkit-user-select: none;
    user-select: none;
    background-color: transparent;
    border: 0.0625rem solid transparent;
    padding: 0.55rem 0.95rem;
    font-size: 1rem;
    line-height: 1.5;
    border-radius: 0.55rem;
    transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
    .btn {
        transition: none;
    }
}

.btn:hover {
    color: #44476A;
    text-decoration: none;
}

.btn:focus, .btn.focus {
    outline: 0;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn.disabled, .btn:disabled {
    opacity: 0.65;
    box-shadow: none;
}

.btn:not(:disabled):not(.disabled):active, .btn:not(:disabled):not(.disabled).active {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn:not(:disabled):not(.disabled):active:focus, .btn:not(:disabled):not(.disabled).active:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

a.btn.disabled,
fieldset:disabled a.btn {
    pointer-events: none;
}

.btn-primary {
    color: #31344b;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-primary:hover {
    color: #31344b;
    background-color: #cfd1df;
    border-color: #c8cad9;
}

.btn-primary:focus, .btn-primary.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(203, 204, 214, 0.5);
}

.btn-primary.disabled, .btn-primary:disabled {
    color: #31344b;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
}

.btn-primary:not(:disabled):not(.disabled):active, .btn-primary:not(:disabled):not(.disabled).active,
  .show > .btn-primary.dropdown-toggle {
    color: #31344b;
    background-color: #c8cad9;
    border-color: #c0c3d4;
}

.btn-primary:not(:disabled):not(.disabled):active:focus, .btn-primary:not(:disabled):not(.disabled).active:focus,
    .show > .btn-primary.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(203, 204, 214, 0.5);
}

.btn-secondary {
    color: #ECF0F3;
    background-color: #2D4CC8;
    border-color: #2D4CC8;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-secondary:hover {
    color: #ECF0F3;
    background-color: #2640a9;
    border-color: #243c9e;
}

.btn-secondary:focus, .btn-secondary.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(74, 101, 206, 0.5);
}

.btn-secondary.disabled, .btn-secondary:disabled {
    color: #ECF0F3;
    background-color: #2D4CC8;
    border-color: #2D4CC8;
}

.btn-secondary:not(:disabled):not(.disabled):active, .btn-secondary:not(:disabled):not(.disabled).active,
  .show > .btn-secondary.dropdown-toggle {
    color: #ECF0F3;
    background-color: #243c9e;
    border-color: #213894;
}

.btn-secondary:not(:disabled):not(.disabled):active:focus, .btn-secondary:not(:disabled):not(.disabled).active:focus,
    .show > .btn-secondary.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(74, 101, 206, 0.5);
}

.btn-success {
    color: #ECF0F3;
    background-color: #18634B;
    border-color: #18634B;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-success:hover {
    color: #ECF0F3;
    background-color: #114434;
    border-color: #0e3a2c;
}

.btn-success:focus, .btn-success.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(56, 120, 100, 0.5);
}

.btn-success.disabled, .btn-success:disabled {
    color: #ECF0F3;
    background-color: #18634B;
    border-color: #18634B;
}

.btn-success:not(:disabled):not(.disabled):active, .btn-success:not(:disabled):not(.disabled).active,
  .show > .btn-success.dropdown-toggle {
    color: #ECF0F3;
    background-color: #0e3a2c;
    border-color: #0c3024;
}

.btn-success:not(:disabled):not(.disabled):active:focus, .btn-success:not(:disabled):not(.disabled).active:focus,
    .show > .btn-success.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(56, 120, 100, 0.5);
}

.btn-info {
    color: #ECF0F3;
    background-color: #0056B3;
    border-color: #0056B3;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-info:hover {
    color: #ECF0F3;
    background-color: #00448d;
    border-color: #003d80;
}

.btn-info:focus, .btn-info.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(35, 109, 189, 0.5);
}

.btn-info.disabled, .btn-info:disabled {
    color: #ECF0F3;
    background-color: #0056B3;
    border-color: #0056B3;
}

.btn-info:not(:disabled):not(.disabled):active, .btn-info:not(:disabled):not(.disabled).active,
  .show > .btn-info.dropdown-toggle {
    color: #ECF0F3;
    background-color: #003d80;
    border-color: #003773;
}

.btn-info:not(:disabled):not(.disabled):active:focus, .btn-info:not(:disabled):not(.disabled).active:focus,
    .show > .btn-info.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(35, 109, 189, 0.5);
}

.btn-warning {
    color: #ECF0F3;
    background-color: #F0B400;
    border-color: #F0B400;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-warning:hover {
    color: #ECF0F3;
    background-color: #ca9700;
    border-color: #bd8e00;
}

.btn-warning:focus, .btn-warning.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(239, 189, 36, 0.5);
}

.btn-warning.disabled, .btn-warning:disabled {
    color: #ECF0F3;
    background-color: #F0B400;
    border-color: #F0B400;
}

.btn-warning:not(:disabled):not(.disabled):active, .btn-warning:not(:disabled):not(.disabled).active,
  .show > .btn-warning.dropdown-toggle {
    color: #ECF0F3;
    background-color: #bd8e00;
    border-color: #b08400;
}

.btn-warning:not(:disabled):not(.disabled):active:focus, .btn-warning:not(:disabled):not(.disabled).active:focus,
    .show > .btn-warning.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(239, 189, 36, 0.5);
}

.btn-danger {
    color: #ECF0F3;
    background-color: #A91E2C;
    border-color: #A91E2C;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-danger:hover {
    color: #ECF0F3;
    background-color: #891824;
    border-color: #7e1621;
}

.btn-danger:focus, .btn-danger.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(179, 62, 74, 0.5);
}

.btn-danger.disabled, .btn-danger:disabled {
    color: #ECF0F3;
    background-color: #A91E2C;
    border-color: #A91E2C;
}

.btn-danger:not(:disabled):not(.disabled):active, .btn-danger:not(:disabled):not(.disabled).active,
  .show > .btn-danger.dropdown-toggle {
    color: #ECF0F3;
    background-color: #7e1621;
    border-color: #73141e;
}

.btn-danger:not(:disabled):not(.disabled):active:focus, .btn-danger:not(:disabled):not(.disabled).active:focus,
    .show > .btn-danger.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(179, 62, 74, 0.5);
}

.btn-light {
    color: #31344b;
    background-color: #D1D9E6;
    border-color: #D1D9E6;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-light:hover {
    color: #ECF0F3;
    background-color: #b8c5d9;
    border-color: #b0bed4;
}

.btn-light:focus, .btn-light.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(185, 192, 207, 0.5);
}

.btn-light.disabled, .btn-light:disabled {
    color: #31344b;
    background-color: #D1D9E6;
    border-color: #D1D9E6;
}

.btn-light:not(:disabled):not(.disabled):active, .btn-light:not(:disabled):not(.disabled).active,
  .show > .btn-light.dropdown-toggle {
    color: #ECF0F3;
    background-color: #b0bed4;
    border-color: #a8b7d0;
}

.btn-light:not(:disabled):not(.disabled):active:focus, .btn-light:not(:disabled):not(.disabled).active:focus,
    .show > .btn-light.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(185, 192, 207, 0.5);
}

.btn-dark {
    color: #ECF0F3;
    background-color: #31344b;
    border-color: #31344b;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-dark:hover {
    color: #ECF0F3;
    background-color: #222434;
    border-color: #1d1f2c;
}

.btn-dark:focus, .btn-dark.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(77, 80, 100, 0.5);
}

.btn-dark.disabled, .btn-dark:disabled {
    color: #ECF0F3;
    background-color: #31344b;
    border-color: #31344b;
}

.btn-dark:not(:disabled):not(.disabled):active, .btn-dark:not(:disabled):not(.disabled).active,
  .show > .btn-dark.dropdown-toggle {
    color: #ECF0F3;
    background-color: #1d1f2c;
    border-color: #181924;
}

.btn-dark:not(:disabled):not(.disabled):active:focus, .btn-dark:not(:disabled):not(.disabled).active:focus,
    .show > .btn-dark.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(77, 80, 100, 0.5);
}

.btn-default {
    color: #ECF0F3;
    background-color: #262833;
    border-color: #262833;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-default:hover {
    color: #ECF0F3;
    background-color: #16171d;
    border-color: #101116;
}

.btn-default:focus, .btn-default.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(68, 70, 80, 0.5);
}

.btn-default.disabled, .btn-default:disabled {
    color: #ECF0F3;
    background-color: #262833;
    border-color: #262833;
}

.btn-default:not(:disabled):not(.disabled):active, .btn-default:not(:disabled):not(.disabled).active,
  .show > .btn-default.dropdown-toggle {
    color: #ECF0F3;
    background-color: #101116;
    border-color: #0b0b0e;
}

.btn-default:not(:disabled):not(.disabled):active:focus, .btn-default:not(:disabled):not(.disabled).active:focus,
    .show > .btn-default.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(68, 70, 80, 0.5);
}

.btn-white {
    color: #31344b;
    background-color: #ECF0F3;
    border-color: #ECF0F3;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-white:hover {
    color: #31344b;
    background-color: #d5dde4;
    border-color: #cdd7df;
}

.btn-white:focus, .btn-white.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(208, 212, 218, 0.5);
}

.btn-white.disabled, .btn-white:disabled {
    color: #31344b;
    background-color: #ECF0F3;
    border-color: #ECF0F3;
}

.btn-white:not(:disabled):not(.disabled):active, .btn-white:not(:disabled):not(.disabled).active,
  .show > .btn-white.dropdown-toggle {
    color: #31344b;
    background-color: #cdd7df;
    border-color: #c5d1da;
}

.btn-white:not(:disabled):not(.disabled):active:focus, .btn-white:not(:disabled):not(.disabled).active:focus,
    .show > .btn-white.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(208, 212, 218, 0.5);
}

.btn-gray {
    color: #ECF0F3;
    background-color: #44476A;
    border-color: #44476A;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-gray:hover {
    color: #ECF0F3;
    background-color: #353753;
    border-color: #30324b;
}

.btn-gray:focus, .btn-gray.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(93, 96, 127, 0.5);
}

.btn-gray.disabled, .btn-gray:disabled {
    color: #ECF0F3;
    background-color: #44476A;
    border-color: #44476A;
}

.btn-gray:not(:disabled):not(.disabled):active, .btn-gray:not(:disabled):not(.disabled).active,
  .show > .btn-gray.dropdown-toggle {
    color: #ECF0F3;
    background-color: #30324b;
    border-color: #2b2d43;
}

.btn-gray:not(:disabled):not(.disabled):active:focus, .btn-gray:not(:disabled):not(.disabled).active:focus,
    .show > .btn-gray.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(93, 96, 127, 0.5);
}

.btn-neutral {
    color: #31344b;
    background-color: #ECF0F3;
    border-color: #ECF0F3;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-neutral:hover {
    color: #31344b;
    background-color: #d5dde4;
    border-color: #cdd7df;
}

.btn-neutral:focus, .btn-neutral.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(208, 212, 218, 0.5);
}

.btn-neutral.disabled, .btn-neutral:disabled {
    color: #31344b;
    background-color: #ECF0F3;
    border-color: #ECF0F3;
}

.btn-neutral:not(:disabled):not(.disabled):active, .btn-neutral:not(:disabled):not(.disabled).active,
  .show > .btn-neutral.dropdown-toggle {
    color: #31344b;
    background-color: #cdd7df;
    border-color: #c5d1da;
}

.btn-neutral:not(:disabled):not(.disabled):active:focus, .btn-neutral:not(:disabled):not(.disabled).active:focus,
    .show > .btn-neutral.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(208, 212, 218, 0.5);
}

.btn-soft {
    color: #31344b;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-soft:hover {
    color: #31344b;
    background-color: #cfd1df;
    border-color: #c8cad9;
}

.btn-soft:focus, .btn-soft.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(203, 204, 214, 0.5);
}

.btn-soft.disabled, .btn-soft:disabled {
    color: #31344b;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
}

.btn-soft:not(:disabled):not(.disabled):active, .btn-soft:not(:disabled):not(.disabled).active,
  .show > .btn-soft.dropdown-toggle {
    color: #31344b;
    background-color: #c8cad9;
    border-color: #c0c3d4;
}

.btn-soft:not(:disabled):not(.disabled):active:focus, .btn-soft:not(:disabled):not(.disabled).active:focus,
    .show > .btn-soft.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(203, 204, 214, 0.5);
}

.btn-black {
    color: #ECF0F3;
    background-color: #262833;
    border-color: #262833;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-black:hover {
    color: #ECF0F3;
    background-color: #16171d;
    border-color: #101116;
}

.btn-black:focus, .btn-black.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(68, 70, 80, 0.5);
}

.btn-black.disabled, .btn-black:disabled {
    color: #ECF0F3;
    background-color: #262833;
    border-color: #262833;
}

.btn-black:not(:disabled):not(.disabled):active, .btn-black:not(:disabled):not(.disabled).active,
  .show > .btn-black.dropdown-toggle {
    color: #ECF0F3;
    background-color: #101116;
    border-color: #0b0b0e;
}

.btn-black:not(:disabled):not(.disabled):active:focus, .btn-black:not(:disabled):not(.disabled).active:focus,
    .show > .btn-black.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(68, 70, 80, 0.5);
}

.btn-purple {
    color: #ECF0F3;
    background-color: #6f42c1;
    border-color: #6f42c1;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-purple:hover {
    color: #ECF0F3;
    background-color: #5e37a6;
    border-color: #59339d;
}

.btn-purple:focus, .btn-purple.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(130, 92, 201, 0.5);
}

.btn-purple.disabled, .btn-purple:disabled {
    color: #ECF0F3;
    background-color: #6f42c1;
    border-color: #6f42c1;
}

.btn-purple:not(:disabled):not(.disabled):active, .btn-purple:not(:disabled):not(.disabled).active,
  .show > .btn-purple.dropdown-toggle {
    color: #ECF0F3;
    background-color: #59339d;
    border-color: #533093;
}

.btn-purple:not(:disabled):not(.disabled):active:focus, .btn-purple:not(:disabled):not(.disabled).active:focus,
    .show > .btn-purple.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(130, 92, 201, 0.5);
}

.btn-gray-100 {
    color: #31344b;
    background-color: #f3f7fa;
    border-color: #f3f7fa;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-gray-100:hover {
    color: #31344b;
    background-color: #d8e5ef;
    border-color: #cfdfeb;
}

.btn-gray-100:focus, .btn-gray-100.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(214, 218, 224, 0.5);
}

.btn-gray-100.disabled, .btn-gray-100:disabled {
    color: #31344b;
    background-color: #f3f7fa;
    border-color: #f3f7fa;
}

.btn-gray-100:not(:disabled):not(.disabled):active, .btn-gray-100:not(:disabled):not(.disabled).active,
  .show > .btn-gray-100.dropdown-toggle {
    color: #31344b;
    background-color: #cfdfeb;
    border-color: #c6d9e7;
}

.btn-gray-100:not(:disabled):not(.disabled):active:focus, .btn-gray-100:not(:disabled):not(.disabled).active:focus,
    .show > .btn-gray-100.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(214, 218, 224, 0.5);
}

.btn-gray-200 {
    color: #31344b;
    background-color: #fafbfe;
    border-color: #fafbfe;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-gray-200:hover {
    color: #31344b;
    background-color: #dae2f8;
    border-color: #d0d9f6;
}

.btn-gray-200:focus, .btn-gray-200.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(220, 221, 227, 0.5);
}

.btn-gray-200.disabled, .btn-gray-200:disabled {
    color: #31344b;
    background-color: #fafbfe;
    border-color: #fafbfe;
}

.btn-gray-200:not(:disabled):not(.disabled):active, .btn-gray-200:not(:disabled):not(.disabled).active,
  .show > .btn-gray-200.dropdown-toggle {
    color: #31344b;
    background-color: #d0d9f6;
    border-color: #c5d1f3;
}

.btn-gray-200:not(:disabled):not(.disabled):active:focus, .btn-gray-200:not(:disabled):not(.disabled).active:focus,
    .show > .btn-gray-200.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(220, 221, 227, 0.5);
}

.btn-gray-300 {
    color: #31344b;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-gray-300:hover {
    color: #31344b;
    background-color: #cfd1df;
    border-color: #c8cad9;
}

.btn-gray-300:focus, .btn-gray-300.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(203, 204, 214, 0.5);
}

.btn-gray-300.disabled, .btn-gray-300:disabled {
    color: #31344b;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
}

.btn-gray-300:not(:disabled):not(.disabled):active, .btn-gray-300:not(:disabled):not(.disabled).active,
  .show > .btn-gray-300.dropdown-toggle {
    color: #31344b;
    background-color: #c8cad9;
    border-color: #c0c3d4;
}

.btn-gray-300:not(:disabled):not(.disabled):active:focus, .btn-gray-300:not(:disabled):not(.disabled).active:focus,
    .show > .btn-gray-300.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(203, 204, 214, 0.5);
}

.btn-gray-400 {
    color: #31344b;
    background-color: #D1D9E6;
    border-color: #D1D9E6;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-gray-400:hover {
    color: #ECF0F3;
    background-color: #b8c5d9;
    border-color: #b0bed4;
}

.btn-gray-400:focus, .btn-gray-400.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(185, 192, 207, 0.5);
}

.btn-gray-400.disabled, .btn-gray-400:disabled {
    color: #31344b;
    background-color: #D1D9E6;
    border-color: #D1D9E6;
}

.btn-gray-400:not(:disabled):not(.disabled):active, .btn-gray-400:not(:disabled):not(.disabled).active,
  .show > .btn-gray-400.dropdown-toggle {
    color: #ECF0F3;
    background-color: #b0bed4;
    border-color: #a8b7d0;
}

.btn-gray-400:not(:disabled):not(.disabled):active:focus, .btn-gray-400:not(:disabled):not(.disabled).active:focus,
    .show > .btn-gray-400.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(185, 192, 207, 0.5);
}

.btn-gray-500 {
    color: #ECF0F3;
    background-color: #b1bcce;
    border-color: #b1bcce;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-gray-500:hover {
    color: #ECF0F3;
    background-color: #9aa8bf;
    border-color: #92a1ba;
}

.btn-gray-500:focus, .btn-gray-500.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(186, 196, 212, 0.5);
}

.btn-gray-500.disabled, .btn-gray-500:disabled {
    color: #ECF0F3;
    background-color: #b1bcce;
    border-color: #b1bcce;
}

.btn-gray-500:not(:disabled):not(.disabled):active, .btn-gray-500:not(:disabled):not(.disabled).active,
  .show > .btn-gray-500.dropdown-toggle {
    color: #ECF0F3;
    background-color: #92a1ba;
    border-color: #8a9ab5;
}

.btn-gray-500:not(:disabled):not(.disabled):active:focus, .btn-gray-500:not(:disabled):not(.disabled).active:focus,
    .show > .btn-gray-500.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(186, 196, 212, 0.5);
}

.btn-gray-600 {
    color: #ECF0F3;
    background-color: #93a5be;
    border-color: #93a5be;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-gray-600:hover {
    color: #ECF0F3;
    background-color: #7b91b0;
    border-color: #738aab;
}

.btn-gray-600:focus, .btn-gray-600.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(160, 176, 198, 0.5);
}

.btn-gray-600.disabled, .btn-gray-600:disabled {
    color: #ECF0F3;
    background-color: #93a5be;
    border-color: #93a5be;
}

.btn-gray-600:not(:disabled):not(.disabled):active, .btn-gray-600:not(:disabled):not(.disabled).active,
  .show > .btn-gray-600.dropdown-toggle {
    color: #ECF0F3;
    background-color: #738aab;
    border-color: #6b84a6;
}

.btn-gray-600:not(:disabled):not(.disabled):active:focus, .btn-gray-600:not(:disabled):not(.disabled).active:focus,
    .show > .btn-gray-600.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(160, 176, 198, 0.5);
}

.btn-gray-700 {
    color: #ECF0F3;
    background-color: #66799e;
    border-color: #66799e;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-gray-700:hover {
    color: #ECF0F3;
    background-color: #566788;
    border-color: #516180;
}

.btn-gray-700:focus, .btn-gray-700.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(122, 139, 171, 0.5);
}

.btn-gray-700.disabled, .btn-gray-700:disabled {
    color: #ECF0F3;
    background-color: #66799e;
    border-color: #66799e;
}

.btn-gray-700:not(:disabled):not(.disabled):active, .btn-gray-700:not(:disabled):not(.disabled).active,
  .show > .btn-gray-700.dropdown-toggle {
    color: #ECF0F3;
    background-color: #516180;
    border-color: #4c5b78;
}

.btn-gray-700:not(:disabled):not(.disabled):active:focus, .btn-gray-700:not(:disabled):not(.disabled).active:focus,
    .show > .btn-gray-700.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(122, 139, 171, 0.5);
}

.btn-gray-800 {
    color: #ECF0F3;
    background-color: #525480;
    border-color: #525480;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-gray-800:hover {
    color: #ECF0F3;
    background-color: #434569;
    border-color: #3e4061;
}

.btn-gray-800:focus, .btn-gray-800.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(105, 107, 145, 0.5);
}

.btn-gray-800.disabled, .btn-gray-800:disabled {
    color: #ECF0F3;
    background-color: #525480;
    border-color: #525480;
}

.btn-gray-800:not(:disabled):not(.disabled):active, .btn-gray-800:not(:disabled):not(.disabled).active,
  .show > .btn-gray-800.dropdown-toggle {
    color: #ECF0F3;
    background-color: #3e4061;
    border-color: #393b59;
}

.btn-gray-800:not(:disabled):not(.disabled):active:focus, .btn-gray-800:not(:disabled):not(.disabled).active:focus,
    .show > .btn-gray-800.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(105, 107, 145, 0.5);
}

.btn-facebook {
    color: #ECF0F3;
    background-color: #3b5999;
    border-color: #3b5999;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-facebook:hover {
    color: #ECF0F3;
    background-color: #30497d;
    border-color: #2d4474;
}

.btn-facebook:focus, .btn-facebook.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(86, 112, 167, 0.5);
}

.btn-facebook.disabled, .btn-facebook:disabled {
    color: #ECF0F3;
    background-color: #3b5999;
    border-color: #3b5999;
}

.btn-facebook:not(:disabled):not(.disabled):active, .btn-facebook:not(:disabled):not(.disabled).active,
  .show > .btn-facebook.dropdown-toggle {
    color: #ECF0F3;
    background-color: #2d4474;
    border-color: #293e6b;
}

.btn-facebook:not(:disabled):not(.disabled):active:focus, .btn-facebook:not(:disabled):not(.disabled).active:focus,
    .show > .btn-facebook.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(86, 112, 167, 0.5);
}

.btn-dribbble {
    color: #ECF0F3;
    background-color: #ea4c89;
    border-color: #ea4c89;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-dribbble:hover {
    color: #ECF0F3;
    background-color: #e62a72;
    border-color: #e51e6b;
}

.btn-dribbble:focus, .btn-dribbble.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(234, 101, 153, 0.5);
}

.btn-dribbble.disabled, .btn-dribbble:disabled {
    color: #ECF0F3;
    background-color: #ea4c89;
    border-color: #ea4c89;
}

.btn-dribbble:not(:disabled):not(.disabled):active, .btn-dribbble:not(:disabled):not(.disabled).active,
  .show > .btn-dribbble.dropdown-toggle {
    color: #ECF0F3;
    background-color: #e51e6b;
    border-color: #dc1a65;
}

.btn-dribbble:not(:disabled):not(.disabled):active:focus, .btn-dribbble:not(:disabled):not(.disabled).active:focus,
    .show > .btn-dribbble.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(234, 101, 153, 0.5);
}

.btn-github {
    color: #ECF0F3;
    background-color: #222222;
    border-color: #222222;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-github:hover {
    color: #ECF0F3;
    background-color: #0f0f0f;
    border-color: #090909;
}

.btn-github:focus, .btn-github.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(64, 65, 65, 0.5);
}

.btn-github.disabled, .btn-github:disabled {
    color: #ECF0F3;
    background-color: #222222;
    border-color: #222222;
}

.btn-github:not(:disabled):not(.disabled):active, .btn-github:not(:disabled):not(.disabled).active,
  .show > .btn-github.dropdown-toggle {
    color: #ECF0F3;
    background-color: #090909;
    border-color: #020202;
}

.btn-github:not(:disabled):not(.disabled):active:focus, .btn-github:not(:disabled):not(.disabled).active:focus,
    .show > .btn-github.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(64, 65, 65, 0.5);
}

.btn-behance {
    color: #ECF0F3;
    background-color: #0057ff;
    border-color: #0057ff;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-behance:hover {
    color: #ECF0F3;
    background-color: #004ad9;
    border-color: #0046cc;
}

.btn-behance:focus, .btn-behance.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(35, 110, 253, 0.5);
}

.btn-behance.disabled, .btn-behance:disabled {
    color: #ECF0F3;
    background-color: #0057ff;
    border-color: #0057ff;
}

.btn-behance:not(:disabled):not(.disabled):active, .btn-behance:not(:disabled):not(.disabled).active,
  .show > .btn-behance.dropdown-toggle {
    color: #ECF0F3;
    background-color: #0046cc;
    border-color: #0041bf;
}

.btn-behance:not(:disabled):not(.disabled):active:focus, .btn-behance:not(:disabled):not(.disabled).active:focus,
    .show > .btn-behance.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(35, 110, 253, 0.5);
}

.btn-twitter {
    color: #ECF0F3;
    background-color: #1da1f2;
    border-color: #1da1f2;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-twitter:hover {
    color: #ECF0F3;
    background-color: #0d8ddc;
    border-color: #0c85d0;
}

.btn-twitter:focus, .btn-twitter.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(60, 173, 242, 0.5);
}

.btn-twitter.disabled, .btn-twitter:disabled {
    color: #ECF0F3;
    background-color: #1da1f2;
    border-color: #1da1f2;
}

.btn-twitter:not(:disabled):not(.disabled):active, .btn-twitter:not(:disabled):not(.disabled).active,
  .show > .btn-twitter.dropdown-toggle {
    color: #ECF0F3;
    background-color: #0c85d0;
    border-color: #0b7ec4;
}

.btn-twitter:not(:disabled):not(.disabled):active:focus, .btn-twitter:not(:disabled):not(.disabled).active:focus,
    .show > .btn-twitter.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(60, 173, 242, 0.5);
}

.btn-slack {
    color: #ECF0F3;
    background-color: #3aaf85;
    border-color: #3aaf85;
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075);
}

.btn-slack:hover {
    color: #ECF0F3;
    background-color: #30926f;
    border-color: #2d8968;
}

.btn-slack:focus, .btn-slack.focus {
    box-shadow: inset 0 1px 0 rgba(236, 240, 243, 0.15), 0 1px 1px rgba(38, 40, 51, 0.075), 0 0 0 0.0625rem rgba(85, 185, 150, 0.5);
}

.btn-slack.disabled, .btn-slack:disabled {
    color: #ECF0F3;
    background-color: #3aaf85;
    border-color: #3aaf85;
}

.btn-slack:not(:disabled):not(.disabled):active, .btn-slack:not(:disabled):not(.disabled).active,
  .show > .btn-slack.dropdown-toggle {
    color: #ECF0F3;
    background-color: #2d8968;
    border-color: #2a7f61;
}

.btn-slack:not(:disabled):not(.disabled):active:focus, .btn-slack:not(:disabled):not(.disabled).active:focus,
    .show > .btn-slack.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(85, 185, 150, 0.5);
}

.btn-outline-primary {
    color: #e6e7ee;
    border-color: #e6e7ee;
}

.btn-outline-primary:hover {
    color: #31344b;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
}

.btn-outline-primary:focus, .btn-outline-primary.focus {
    box-shadow: 0 0 0 0.0625rem rgba(230, 231, 238, 0.5);
}

.btn-outline-primary.disabled, .btn-outline-primary:disabled {
    color: #e6e7ee;
    background-color: transparent;
}

.btn-outline-primary:not(:disabled):not(.disabled):active, .btn-outline-primary:not(:disabled):not(.disabled).active,
  .show > .btn-outline-primary.dropdown-toggle {
    color: #31344b;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
}

.btn-outline-primary:not(:disabled):not(.disabled):active:focus, .btn-outline-primary:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-primary.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(230, 231, 238, 0.5);
}

.btn-outline-secondary {
    color: #2D4CC8;
    border-color: #2D4CC8;
}

.btn-outline-secondary:hover {
    color: #ECF0F3;
    background-color: #2D4CC8;
    border-color: #2D4CC8;
}

.btn-outline-secondary:focus, .btn-outline-secondary.focus {
    box-shadow: 0 0 0 0.0625rem rgba(45, 76, 200, 0.5);
}

.btn-outline-secondary.disabled, .btn-outline-secondary:disabled {
    color: #2D4CC8;
    background-color: transparent;
}

.btn-outline-secondary:not(:disabled):not(.disabled):active, .btn-outline-secondary:not(:disabled):not(.disabled).active,
  .show > .btn-outline-secondary.dropdown-toggle {
    color: #ECF0F3;
    background-color: #2D4CC8;
    border-color: #2D4CC8;
}

.btn-outline-secondary:not(:disabled):not(.disabled):active:focus, .btn-outline-secondary:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-secondary.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(45, 76, 200, 0.5);
}

.btn-outline-success {
    color: #18634B;
    border-color: #18634B;
}

.btn-outline-success:hover {
    color: #ECF0F3;
    background-color: #18634B;
    border-color: #18634B;
}

.btn-outline-success:focus, .btn-outline-success.focus {
    box-shadow: 0 0 0 0.0625rem rgba(24, 99, 75, 0.5);
}

.btn-outline-success.disabled, .btn-outline-success:disabled {
    color: #18634B;
    background-color: transparent;
}

.btn-outline-success:not(:disabled):not(.disabled):active, .btn-outline-success:not(:disabled):not(.disabled).active,
  .show > .btn-outline-success.dropdown-toggle {
    color: #ECF0F3;
    background-color: #18634B;
    border-color: #18634B;
}

.btn-outline-success:not(:disabled):not(.disabled):active:focus, .btn-outline-success:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-success.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(24, 99, 75, 0.5);
}

.btn-outline-info {
    color: #0056B3;
    border-color: #0056B3;
}

.btn-outline-info:hover {
    color: #ECF0F3;
    background-color: #0056B3;
    border-color: #0056B3;
}

.btn-outline-info:focus, .btn-outline-info.focus {
    box-shadow: 0 0 0 0.0625rem rgba(0, 86, 179, 0.5);
}

.btn-outline-info.disabled, .btn-outline-info:disabled {
    color: #0056B3;
    background-color: transparent;
}

.btn-outline-info:not(:disabled):not(.disabled):active, .btn-outline-info:not(:disabled):not(.disabled).active,
  .show > .btn-outline-info.dropdown-toggle {
    color: #ECF0F3;
    background-color: #0056B3;
    border-color: #0056B3;
}

.btn-outline-info:not(:disabled):not(.disabled):active:focus, .btn-outline-info:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-info.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(0, 86, 179, 0.5);
}

.btn-outline-warning {
    color: #F0B400;
    border-color: #F0B400;
}

.btn-outline-warning:hover {
    color: #ECF0F3;
    background-color: #F0B400;
    border-color: #F0B400;
}

.btn-outline-warning:focus, .btn-outline-warning.focus {
    box-shadow: 0 0 0 0.0625rem rgba(240, 180, 0, 0.5);
}

.btn-outline-warning.disabled, .btn-outline-warning:disabled {
    color: #F0B400;
    background-color: transparent;
}

.btn-outline-warning:not(:disabled):not(.disabled):active, .btn-outline-warning:not(:disabled):not(.disabled).active,
  .show > .btn-outline-warning.dropdown-toggle {
    color: #ECF0F3;
    background-color: #F0B400;
    border-color: #F0B400;
}

.btn-outline-warning:not(:disabled):not(.disabled):active:focus, .btn-outline-warning:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-warning.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(240, 180, 0, 0.5);
}

.btn-outline-danger {
    color: #A91E2C;
    border-color: #A91E2C;
}

.btn-outline-danger:hover {
    color: #ECF0F3;
    background-color: #A91E2C;
    border-color: #A91E2C;
}

.btn-outline-danger:focus, .btn-outline-danger.focus {
    box-shadow: 0 0 0 0.0625rem rgba(169, 30, 44, 0.5);
}

.btn-outline-danger.disabled, .btn-outline-danger:disabled {
    color: #A91E2C;
    background-color: transparent;
}

.btn-outline-danger:not(:disabled):not(.disabled):active, .btn-outline-danger:not(:disabled):not(.disabled).active,
  .show > .btn-outline-danger.dropdown-toggle {
    color: #ECF0F3;
    background-color: #A91E2C;
    border-color: #A91E2C;
}

.btn-outline-danger:not(:disabled):not(.disabled):active:focus, .btn-outline-danger:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-danger.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(169, 30, 44, 0.5);
}

.btn-outline-light {
    color: #D1D9E6;
    border-color: #D1D9E6;
}

.btn-outline-light:hover {
    color: #31344b;
    background-color: #D1D9E6;
    border-color: #D1D9E6;
}

.btn-outline-light:focus, .btn-outline-light.focus {
    box-shadow: 0 0 0 0.0625rem rgba(209, 217, 230, 0.5);
}

.btn-outline-light.disabled, .btn-outline-light:disabled {
    color: #D1D9E6;
    background-color: transparent;
}

.btn-outline-light:not(:disabled):not(.disabled):active, .btn-outline-light:not(:disabled):not(.disabled).active,
  .show > .btn-outline-light.dropdown-toggle {
    color: #31344b;
    background-color: #D1D9E6;
    border-color: #D1D9E6;
}

.btn-outline-light:not(:disabled):not(.disabled):active:focus, .btn-outline-light:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-light.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(209, 217, 230, 0.5);
}

.btn-outline-dark {
    color: #31344b;
    border-color: #31344b;
}

.btn-outline-dark:hover {
    color: #ECF0F3;
    background-color: #31344b;
    border-color: #31344b;
}

.btn-outline-dark:focus, .btn-outline-dark.focus {
    box-shadow: 0 0 0 0.0625rem rgba(49, 52, 75, 0.5);
}

.btn-outline-dark.disabled, .btn-outline-dark:disabled {
    color: #31344b;
    background-color: transparent;
}

.btn-outline-dark:not(:disabled):not(.disabled):active, .btn-outline-dark:not(:disabled):not(.disabled).active,
  .show > .btn-outline-dark.dropdown-toggle {
    color: #ECF0F3;
    background-color: #31344b;
    border-color: #31344b;
}

.btn-outline-dark:not(:disabled):not(.disabled):active:focus, .btn-outline-dark:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-dark.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(49, 52, 75, 0.5);
}

.btn-outline-default {
    color: #262833;
    border-color: #262833;
}

.btn-outline-default:hover {
    color: #ECF0F3;
    background-color: #262833;
    border-color: #262833;
}

.btn-outline-default:focus, .btn-outline-default.focus {
    box-shadow: 0 0 0 0.0625rem rgba(38, 40, 51, 0.5);
}

.btn-outline-default.disabled, .btn-outline-default:disabled {
    color: #262833;
    background-color: transparent;
}

.btn-outline-default:not(:disabled):not(.disabled):active, .btn-outline-default:not(:disabled):not(.disabled).active,
  .show > .btn-outline-default.dropdown-toggle {
    color: #ECF0F3;
    background-color: #262833;
    border-color: #262833;
}

.btn-outline-default:not(:disabled):not(.disabled):active:focus, .btn-outline-default:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-default.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(38, 40, 51, 0.5);
}

.btn-outline-white {
    color: #ECF0F3;
    border-color: #ECF0F3;
}

.btn-outline-white:hover {
    color: #31344b;
    background-color: #ECF0F3;
    border-color: #ECF0F3;
}

.btn-outline-white:focus, .btn-outline-white.focus {
    box-shadow: 0 0 0 0.0625rem rgba(236, 240, 243, 0.5);
}

.btn-outline-white.disabled, .btn-outline-white:disabled {
    color: #ECF0F3;
    background-color: transparent;
}

.btn-outline-white:not(:disabled):not(.disabled):active, .btn-outline-white:not(:disabled):not(.disabled).active,
  .show > .btn-outline-white.dropdown-toggle {
    color: #31344b;
    background-color: #ECF0F3;
    border-color: #ECF0F3;
}

.btn-outline-white:not(:disabled):not(.disabled):active:focus, .btn-outline-white:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-white.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(236, 240, 243, 0.5);
}

.btn-outline-gray {
    color: #44476A;
    border-color: #44476A;
}

.btn-outline-gray:hover {
    color: #ECF0F3;
    background-color: #44476A;
    border-color: #44476A;
}

.btn-outline-gray:focus, .btn-outline-gray.focus {
    box-shadow: 0 0 0 0.0625rem rgba(68, 71, 106, 0.5);
}

.btn-outline-gray.disabled, .btn-outline-gray:disabled {
    color: #44476A;
    background-color: transparent;
}

.btn-outline-gray:not(:disabled):not(.disabled):active, .btn-outline-gray:not(:disabled):not(.disabled).active,
  .show > .btn-outline-gray.dropdown-toggle {
    color: #ECF0F3;
    background-color: #44476A;
    border-color: #44476A;
}

.btn-outline-gray:not(:disabled):not(.disabled):active:focus, .btn-outline-gray:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-gray.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(68, 71, 106, 0.5);
}

.btn-outline-neutral {
    color: #ECF0F3;
    border-color: #ECF0F3;
}

.btn-outline-neutral:hover {
    color: #31344b;
    background-color: #ECF0F3;
    border-color: #ECF0F3;
}

.btn-outline-neutral:focus, .btn-outline-neutral.focus {
    box-shadow: 0 0 0 0.0625rem rgba(236, 240, 243, 0.5);
}

.btn-outline-neutral.disabled, .btn-outline-neutral:disabled {
    color: #ECF0F3;
    background-color: transparent;
}

.btn-outline-neutral:not(:disabled):not(.disabled):active, .btn-outline-neutral:not(:disabled):not(.disabled).active,
  .show > .btn-outline-neutral.dropdown-toggle {
    color: #31344b;
    background-color: #ECF0F3;
    border-color: #ECF0F3;
}

.btn-outline-neutral:not(:disabled):not(.disabled):active:focus, .btn-outline-neutral:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-neutral.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(236, 240, 243, 0.5);
}

.btn-outline-soft {
    color: #e6e7ee;
    border-color: #e6e7ee;
}

.btn-outline-soft:hover {
    color: #31344b;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
}

.btn-outline-soft:focus, .btn-outline-soft.focus {
    box-shadow: 0 0 0 0.0625rem rgba(230, 231, 238, 0.5);
}

.btn-outline-soft.disabled, .btn-outline-soft:disabled {
    color: #e6e7ee;
    background-color: transparent;
}

.btn-outline-soft:not(:disabled):not(.disabled):active, .btn-outline-soft:not(:disabled):not(.disabled).active,
  .show > .btn-outline-soft.dropdown-toggle {
    color: #31344b;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
}

.btn-outline-soft:not(:disabled):not(.disabled):active:focus, .btn-outline-soft:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-soft.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(230, 231, 238, 0.5);
}

.btn-outline-black {
    color: #262833;
    border-color: #262833;
}

.btn-outline-black:hover {
    color: #ECF0F3;
    background-color: #262833;
    border-color: #262833;
}

.btn-outline-black:focus, .btn-outline-black.focus {
    box-shadow: 0 0 0 0.0625rem rgba(38, 40, 51, 0.5);
}

.btn-outline-black.disabled, .btn-outline-black:disabled {
    color: #262833;
    background-color: transparent;
}

.btn-outline-black:not(:disabled):not(.disabled):active, .btn-outline-black:not(:disabled):not(.disabled).active,
  .show > .btn-outline-black.dropdown-toggle {
    color: #ECF0F3;
    background-color: #262833;
    border-color: #262833;
}

.btn-outline-black:not(:disabled):not(.disabled):active:focus, .btn-outline-black:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-black.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(38, 40, 51, 0.5);
}

.btn-outline-purple {
    color: #6f42c1;
    border-color: #6f42c1;
}

.btn-outline-purple:hover {
    color: #ECF0F3;
    background-color: #6f42c1;
    border-color: #6f42c1;
}

.btn-outline-purple:focus, .btn-outline-purple.focus {
    box-shadow: 0 0 0 0.0625rem rgba(111, 66, 193, 0.5);
}

.btn-outline-purple.disabled, .btn-outline-purple:disabled {
    color: #6f42c1;
    background-color: transparent;
}

.btn-outline-purple:not(:disabled):not(.disabled):active, .btn-outline-purple:not(:disabled):not(.disabled).active,
  .show > .btn-outline-purple.dropdown-toggle {
    color: #ECF0F3;
    background-color: #6f42c1;
    border-color: #6f42c1;
}

.btn-outline-purple:not(:disabled):not(.disabled):active:focus, .btn-outline-purple:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-purple.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(111, 66, 193, 0.5);
}

.btn-outline-gray-100 {
    color: #f3f7fa;
    border-color: #f3f7fa;
}

.btn-outline-gray-100:hover {
    color: #31344b;
    background-color: #f3f7fa;
    border-color: #f3f7fa;
}

.btn-outline-gray-100:focus, .btn-outline-gray-100.focus {
    box-shadow: 0 0 0 0.0625rem rgba(243, 247, 250, 0.5);
}

.btn-outline-gray-100.disabled, .btn-outline-gray-100:disabled {
    color: #f3f7fa;
    background-color: transparent;
}

.btn-outline-gray-100:not(:disabled):not(.disabled):active, .btn-outline-gray-100:not(:disabled):not(.disabled).active,
  .show > .btn-outline-gray-100.dropdown-toggle {
    color: #31344b;
    background-color: #f3f7fa;
    border-color: #f3f7fa;
}

.btn-outline-gray-100:not(:disabled):not(.disabled):active:focus, .btn-outline-gray-100:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-gray-100.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(243, 247, 250, 0.5);
}

.btn-outline-gray-200 {
    color: #fafbfe;
    border-color: #fafbfe;
}

.btn-outline-gray-200:hover {
    color: #31344b;
    background-color: #fafbfe;
    border-color: #fafbfe;
}

.btn-outline-gray-200:focus, .btn-outline-gray-200.focus {
    box-shadow: 0 0 0 0.0625rem rgba(250, 251, 254, 0.5);
}

.btn-outline-gray-200.disabled, .btn-outline-gray-200:disabled {
    color: #fafbfe;
    background-color: transparent;
}

.btn-outline-gray-200:not(:disabled):not(.disabled):active, .btn-outline-gray-200:not(:disabled):not(.disabled).active,
  .show > .btn-outline-gray-200.dropdown-toggle {
    color: #31344b;
    background-color: #fafbfe;
    border-color: #fafbfe;
}

.btn-outline-gray-200:not(:disabled):not(.disabled):active:focus, .btn-outline-gray-200:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-gray-200.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(250, 251, 254, 0.5);
}

.btn-outline-gray-300 {
    color: #e6e7ee;
    border-color: #e6e7ee;
}

.btn-outline-gray-300:hover {
    color: #31344b;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
}

.btn-outline-gray-300:focus, .btn-outline-gray-300.focus {
    box-shadow: 0 0 0 0.0625rem rgba(230, 231, 238, 0.5);
}

.btn-outline-gray-300.disabled, .btn-outline-gray-300:disabled {
    color: #e6e7ee;
    background-color: transparent;
}

.btn-outline-gray-300:not(:disabled):not(.disabled):active, .btn-outline-gray-300:not(:disabled):not(.disabled).active,
  .show > .btn-outline-gray-300.dropdown-toggle {
    color: #31344b;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
}

.btn-outline-gray-300:not(:disabled):not(.disabled):active:focus, .btn-outline-gray-300:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-gray-300.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(230, 231, 238, 0.5);
}

.btn-outline-gray-400 {
    color: #D1D9E6;
    border-color: #D1D9E6;
}

.btn-outline-gray-400:hover {
    color: #31344b;
    background-color: #D1D9E6;
    border-color: #D1D9E6;
}

.btn-outline-gray-400:focus, .btn-outline-gray-400.focus {
    box-shadow: 0 0 0 0.0625rem rgba(209, 217, 230, 0.5);
}

.btn-outline-gray-400.disabled, .btn-outline-gray-400:disabled {
    color: #D1D9E6;
    background-color: transparent;
}

.btn-outline-gray-400:not(:disabled):not(.disabled):active, .btn-outline-gray-400:not(:disabled):not(.disabled).active,
  .show > .btn-outline-gray-400.dropdown-toggle {
    color: #31344b;
    background-color: #D1D9E6;
    border-color: #D1D9E6;
}

.btn-outline-gray-400:not(:disabled):not(.disabled):active:focus, .btn-outline-gray-400:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-gray-400.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(209, 217, 230, 0.5);
}

.btn-outline-gray-500 {
    color: #b1bcce;
    border-color: #b1bcce;
}

.btn-outline-gray-500:hover {
    color: #ECF0F3;
    background-color: #b1bcce;
    border-color: #b1bcce;
}

.btn-outline-gray-500:focus, .btn-outline-gray-500.focus {
    box-shadow: 0 0 0 0.0625rem rgba(177, 188, 206, 0.5);
}

.btn-outline-gray-500.disabled, .btn-outline-gray-500:disabled {
    color: #b1bcce;
    background-color: transparent;
}

.btn-outline-gray-500:not(:disabled):not(.disabled):active, .btn-outline-gray-500:not(:disabled):not(.disabled).active,
  .show > .btn-outline-gray-500.dropdown-toggle {
    color: #ECF0F3;
    background-color: #b1bcce;
    border-color: #b1bcce;
}

.btn-outline-gray-500:not(:disabled):not(.disabled):active:focus, .btn-outline-gray-500:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-gray-500.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(177, 188, 206, 0.5);
}

.btn-outline-gray-600 {
    color: #93a5be;
    border-color: #93a5be;
}

.btn-outline-gray-600:hover {
    color: #ECF0F3;
    background-color: #93a5be;
    border-color: #93a5be;
}

.btn-outline-gray-600:focus, .btn-outline-gray-600.focus {
    box-shadow: 0 0 0 0.0625rem rgba(147, 165, 190, 0.5);
}

.btn-outline-gray-600.disabled, .btn-outline-gray-600:disabled {
    color: #93a5be;
    background-color: transparent;
}

.btn-outline-gray-600:not(:disabled):not(.disabled):active, .btn-outline-gray-600:not(:disabled):not(.disabled).active,
  .show > .btn-outline-gray-600.dropdown-toggle {
    color: #ECF0F3;
    background-color: #93a5be;
    border-color: #93a5be;
}

.btn-outline-gray-600:not(:disabled):not(.disabled):active:focus, .btn-outline-gray-600:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-gray-600.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(147, 165, 190, 0.5);
}

.btn-outline-gray-700 {
    color: #66799e;
    border-color: #66799e;
}

.btn-outline-gray-700:hover {
    color: #ECF0F3;
    background-color: #66799e;
    border-color: #66799e;
}

.btn-outline-gray-700:focus, .btn-outline-gray-700.focus {
    box-shadow: 0 0 0 0.0625rem rgba(102, 121, 158, 0.5);
}

.btn-outline-gray-700.disabled, .btn-outline-gray-700:disabled {
    color: #66799e;
    background-color: transparent;
}

.btn-outline-gray-700:not(:disabled):not(.disabled):active, .btn-outline-gray-700:not(:disabled):not(.disabled).active,
  .show > .btn-outline-gray-700.dropdown-toggle {
    color: #ECF0F3;
    background-color: #66799e;
    border-color: #66799e;
}

.btn-outline-gray-700:not(:disabled):not(.disabled):active:focus, .btn-outline-gray-700:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-gray-700.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(102, 121, 158, 0.5);
}

.btn-outline-gray-800 {
    color: #525480;
    border-color: #525480;
}

.btn-outline-gray-800:hover {
    color: #ECF0F3;
    background-color: #525480;
    border-color: #525480;
}

.btn-outline-gray-800:focus, .btn-outline-gray-800.focus {
    box-shadow: 0 0 0 0.0625rem rgba(82, 84, 128, 0.5);
}

.btn-outline-gray-800.disabled, .btn-outline-gray-800:disabled {
    color: #525480;
    background-color: transparent;
}

.btn-outline-gray-800:not(:disabled):not(.disabled):active, .btn-outline-gray-800:not(:disabled):not(.disabled).active,
  .show > .btn-outline-gray-800.dropdown-toggle {
    color: #ECF0F3;
    background-color: #525480;
    border-color: #525480;
}

.btn-outline-gray-800:not(:disabled):not(.disabled):active:focus, .btn-outline-gray-800:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-gray-800.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(82, 84, 128, 0.5);
}

.btn-outline-facebook {
    color: #3b5999;
    border-color: #3b5999;
}

.btn-outline-facebook:hover {
    color: #ECF0F3;
    background-color: #3b5999;
    border-color: #3b5999;
}

.btn-outline-facebook:focus, .btn-outline-facebook.focus {
    box-shadow: 0 0 0 0.0625rem rgba(59, 89, 153, 0.5);
}

.btn-outline-facebook.disabled, .btn-outline-facebook:disabled {
    color: #3b5999;
    background-color: transparent;
}

.btn-outline-facebook:not(:disabled):not(.disabled):active, .btn-outline-facebook:not(:disabled):not(.disabled).active,
  .show > .btn-outline-facebook.dropdown-toggle {
    color: #ECF0F3;
    background-color: #3b5999;
    border-color: #3b5999;
}

.btn-outline-facebook:not(:disabled):not(.disabled):active:focus, .btn-outline-facebook:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-facebook.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(59, 89, 153, 0.5);
}

.btn-outline-dribbble {
    color: #ea4c89;
    border-color: #ea4c89;
}

.btn-outline-dribbble:hover {
    color: #ECF0F3;
    background-color: #ea4c89;
    border-color: #ea4c89;
}

.btn-outline-dribbble:focus, .btn-outline-dribbble.focus {
    box-shadow: 0 0 0 0.0625rem rgba(234, 76, 137, 0.5);
}

.btn-outline-dribbble.disabled, .btn-outline-dribbble:disabled {
    color: #ea4c89;
    background-color: transparent;
}

.btn-outline-dribbble:not(:disabled):not(.disabled):active, .btn-outline-dribbble:not(:disabled):not(.disabled).active,
  .show > .btn-outline-dribbble.dropdown-toggle {
    color: #ECF0F3;
    background-color: #ea4c89;
    border-color: #ea4c89;
}

.btn-outline-dribbble:not(:disabled):not(.disabled):active:focus, .btn-outline-dribbble:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-dribbble.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(234, 76, 137, 0.5);
}

.btn-outline-github {
    color: #222222;
    border-color: #222222;
}

.btn-outline-github:hover {
    color: #ECF0F3;
    background-color: #222222;
    border-color: #222222;
}

.btn-outline-github:focus, .btn-outline-github.focus {
    box-shadow: 0 0 0 0.0625rem rgba(34, 34, 34, 0.5);
}

.btn-outline-github.disabled, .btn-outline-github:disabled {
    color: #222222;
    background-color: transparent;
}

.btn-outline-github:not(:disabled):not(.disabled):active, .btn-outline-github:not(:disabled):not(.disabled).active,
  .show > .btn-outline-github.dropdown-toggle {
    color: #ECF0F3;
    background-color: #222222;
    border-color: #222222;
}

.btn-outline-github:not(:disabled):not(.disabled):active:focus, .btn-outline-github:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-github.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(34, 34, 34, 0.5);
}

.btn-outline-behance {
    color: #0057ff;
    border-color: #0057ff;
}

.btn-outline-behance:hover {
    color: #ECF0F3;
    background-color: #0057ff;
    border-color: #0057ff;
}

.btn-outline-behance:focus, .btn-outline-behance.focus {
    box-shadow: 0 0 0 0.0625rem rgba(0, 87, 255, 0.5);
}

.btn-outline-behance.disabled, .btn-outline-behance:disabled {
    color: #0057ff;
    background-color: transparent;
}

.btn-outline-behance:not(:disabled):not(.disabled):active, .btn-outline-behance:not(:disabled):not(.disabled).active,
  .show > .btn-outline-behance.dropdown-toggle {
    color: #ECF0F3;
    background-color: #0057ff;
    border-color: #0057ff;
}

.btn-outline-behance:not(:disabled):not(.disabled):active:focus, .btn-outline-behance:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-behance.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(0, 87, 255, 0.5);
}

.btn-outline-twitter {
    color: #1da1f2;
    border-color: #1da1f2;
}

.btn-outline-twitter:hover {
    color: #ECF0F3;
    background-color: #1da1f2;
    border-color: #1da1f2;
}

.btn-outline-twitter:focus, .btn-outline-twitter.focus {
    box-shadow: 0 0 0 0.0625rem rgba(29, 161, 242, 0.5);
}

.btn-outline-twitter.disabled, .btn-outline-twitter:disabled {
    color: #1da1f2;
    background-color: transparent;
}

.btn-outline-twitter:not(:disabled):not(.disabled):active, .btn-outline-twitter:not(:disabled):not(.disabled).active,
  .show > .btn-outline-twitter.dropdown-toggle {
    color: #ECF0F3;
    background-color: #1da1f2;
    border-color: #1da1f2;
}

.btn-outline-twitter:not(:disabled):not(.disabled):active:focus, .btn-outline-twitter:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-twitter.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(29, 161, 242, 0.5);
}

.btn-outline-slack {
    color: #3aaf85;
    border-color: #3aaf85;
}

.btn-outline-slack:hover {
    color: #ECF0F3;
    background-color: #3aaf85;
    border-color: #3aaf85;
}

.btn-outline-slack:focus, .btn-outline-slack.focus {
    box-shadow: 0 0 0 0.0625rem rgba(58, 175, 133, 0.5);
}

.btn-outline-slack.disabled, .btn-outline-slack:disabled {
    color: #3aaf85;
    background-color: transparent;
}

.btn-outline-slack:not(:disabled):not(.disabled):active, .btn-outline-slack:not(:disabled):not(.disabled).active,
  .show > .btn-outline-slack.dropdown-toggle {
    color: #ECF0F3;
    background-color: #3aaf85;
    border-color: #3aaf85;
}

.btn-outline-slack:not(:disabled):not(.disabled):active:focus, .btn-outline-slack:not(:disabled):not(.disabled).active:focus,
    .show > .btn-outline-slack.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, 0 0 0 0.0625rem rgba(58, 175, 133, 0.5);
}

.btn-link {
    font-weight: 400;
    color: #31344b;
    text-decoration: none;
}

.btn-link:hover {
    color: #262833;
    text-decoration: none;
}

.btn-link:focus, .btn-link.focus {
    text-decoration: none;
    box-shadow: none;
}

.btn-link:disabled, .btn-link.disabled {
    color: #93a5be;
    pointer-events: none;
}

.btn-lg, .btn-group-lg > .btn {
    padding: 0.875rem 1rem;
    font-size: 1.25rem;
    line-height: 1.5;
    border-radius: 0.3rem;
}

.btn-sm, .btn-group-sm > .btn {
    padding: 0.45rem 0.5rem;
    font-size: 0.875rem;
    line-height: 1.5;
    border-radius: 0.55rem;
}

.btn-block {
    display: block;
    width: 100%;
}

.btn-block + .btn-block {
    margin-top: 0.5rem;
}

input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
    width: 100%;
}

.fade {
    transition: opacity 0.15s linear;
}

@media (prefers-reduced-motion: reduce) {
    .fade {
        transition: none;
    }
}

.fade:not(.show) {
    opacity: 0;
}

.collapse:not(.show) {
    display: none;
}

.collapsing {
    position: relative;
    height: 0;
    overflow: hidden;
    transition: height 0.35s ease;
}

@media (prefers-reduced-motion: reduce) {
    .collapsing {
        transition: none;
    }
}

.dropup,
.dropright,
.dropdown,
.dropleft {
    position: relative;
}

.dropdown-toggle {
    white-space: nowrap;
}

.dropdown-toggle::after {
    display: inline-block;
    margin-left: 0.255em;
    vertical-align: 0.255em;
    content: "";
    border-top: 0.3em solid;
    border-right: 0.3em solid transparent;
    border-bottom: 0;
    border-left: 0.3em solid transparent;
}

.dropdown-toggle:empty::after {
    margin-left: 0;
}

.dropdown-menu {
    position: absolute;
    top: 100%;
    left: 0;
    z-index: 1000;
    display: none;
    float: left;
    min-width: 10rem;
    padding: 0.7rem 0;
    margin: 0.825rem 0 0;
    font-size: 0.875rem;
    color: #44476A;
    text-align: left;
    list-style: none;
    background-color: #e6e7ee;
    background-clip: padding-box;
    border: 0.0625rem solid #D1D9E6;
    border-radius: 0.55rem;
    box-shadow: 6px 6px 12px #b8b9be, -6px -6px 12px #ffffff;
}

.dropdown-menu-left {
    right: auto;
    left: 0;
}

.dropdown-menu-right {
    right: 0;
    left: auto;
}

@media (min-width: 576px) {
    .dropdown-menu-sm-left {
        right: auto;
        left: 0;
    }

    .dropdown-menu-sm-right {
        right: 0;
        left: auto;
    }
}

@media (min-width: 768px) {
    .dropdown-menu-md-left {
        right: auto;
        left: 0;
    }

    .dropdown-menu-md-right {
        right: 0;
        left: auto;
    }
}

@media (min-width: 992px) {
    .dropdown-menu-lg-left {
        right: auto;
        left: 0;
    }

    .dropdown-menu-lg-right {
        right: 0;
        left: auto;
    }
}

@media (min-width: 1200px) {
    .dropdown-menu-xl-left {
        right: auto;
        left: 0;
    }

    .dropdown-menu-xl-right {
        right: 0;
        left: auto;
    }
}

.dropup .dropdown-menu {
    top: auto;
    bottom: 100%;
    margin-top: 0;
    margin-bottom: 0.825rem;
}

.dropup .dropdown-toggle::after {
    display: inline-block;
    margin-left: 0.255em;
    vertical-align: 0.255em;
    content: "";
    border-top: 0;
    border-right: 0.3em solid transparent;
    border-bottom: 0.3em solid;
    border-left: 0.3em solid transparent;
}

.dropup .dropdown-toggle:empty::after {
    margin-left: 0;
}

.dropright .dropdown-menu {
    top: 0;
    right: auto;
    left: 100%;
    margin-top: 0;
    margin-left: 0.825rem;
}

.dropright .dropdown-toggle::after {
    display: inline-block;
    margin-left: 0.255em;
    vertical-align: 0.255em;
    content: "";
    border-top: 0.3em solid transparent;
    border-right: 0;
    border-bottom: 0.3em solid transparent;
    border-left: 0.3em solid;
}

.dropright .dropdown-toggle:empty::after {
    margin-left: 0;
}

.dropright .dropdown-toggle::after {
    vertical-align: 0;
}

.dropleft .dropdown-menu {
    top: 0;
    right: 100%;
    left: auto;
    margin-top: 0;
    margin-right: 0.825rem;
}

.dropleft .dropdown-toggle::after {
    display: inline-block;
    margin-left: 0.255em;
    vertical-align: 0.255em;
    content: "";
}

.dropleft .dropdown-toggle::after {
    display: none;
}

.dropleft .dropdown-toggle::before {
    display: inline-block;
    margin-right: 0.255em;
    vertical-align: 0.255em;
    content: "";
    border-top: 0.3em solid transparent;
    border-right: 0.3em solid;
    border-bottom: 0.3em solid transparent;
}

.dropleft .dropdown-toggle:empty::after {
    margin-left: 0;
}

.dropleft .dropdown-toggle::before {
    vertical-align: 0;
}

.dropdown-menu[x-placement^="top"], .dropdown-menu[x-placement^="right"], .dropdown-menu[x-placement^="bottom"], .dropdown-menu[x-placement^="left"] {
    right: auto;
    bottom: auto;
}

.dropdown-divider {
    height: 0;
    margin: 0.5rem 0;
    overflow: hidden;
    border-top: 1px solid #D1D9E6;
}

.dropdown-item {
    display: block;
    width: 100%;
    padding: 0.25rem 1.5rem;
    clear: both;
    font-weight: 400;
    color: #44476A;
    text-align: inherit;
    white-space: nowrap;
    background-color: transparent;
    border: 0;
}

.dropdown-item:hover, .dropdown-item:focus {
    color: #3a3d5a;
    text-decoration: none;
    background-color: #31344b;
}

.dropdown-item.active, .dropdown-item:active {
    color: #ECF0F3;
    text-decoration: none;
    background-color: #D1D9E6;
}

.dropdown-item.disabled, .dropdown-item:disabled {
    color: #93a5be;
    pointer-events: none;
    background-color: transparent;
}

.dropdown-menu.show {
    display: block;
}

.dropdown-header {
    display: block;
    padding: 0.7rem 1.5rem;
    margin-bottom: 0;
    font-size: 0.875rem;
    color: #44476A;
    white-space: nowrap;
}

.dropdown-item-text {
    display: block;
    padding: 0.25rem 1.5rem;
    color: #44476A;
}

.btn-group,
.btn-group-vertical {
    position: relative;
    display: inline-flex;
    vertical-align: middle;
}

.btn-group > .btn,
  .btn-group-vertical > .btn {
    position: relative;
    flex: 1 1 auto;
}

.btn-group > .btn:hover,
    .btn-group-vertical > .btn:hover {
    z-index: 1;
}

.btn-group > .btn:focus, .btn-group > .btn:active, .btn-group > .btn.active,
    .btn-group-vertical > .btn:focus,
    .btn-group-vertical > .btn:active,
    .btn-group-vertical > .btn.active {
    z-index: 1;
}

.btn-toolbar {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
}

.btn-toolbar .input-group {
    width: auto;
}

.btn-group > .btn:not(:first-child),
.btn-group > .btn-group:not(:first-child) {
    margin-left: -0.0625rem;
}

.btn-group > .btn:not(:last-child):not(.dropdown-toggle),
.btn-group > .btn-group:not(:last-child) > .btn {
    border-top-right-radius: 0;
    border-bottom-right-radius: 0;
}

.btn-group > .btn:not(:first-child),
.btn-group > .btn-group:not(:first-child) > .btn {
    border-top-left-radius: 0;
    border-bottom-left-radius: 0;
}

.dropdown-toggle-split {
    padding-right: 0.7125rem;
    padding-left: 0.7125rem;
}

.dropdown-toggle-split::after,
  .dropup .dropdown-toggle-split::after,
  .dropright .dropdown-toggle-split::after {
    margin-left: 0;
}

.dropleft .dropdown-toggle-split::before {
    margin-right: 0;
}

.btn-sm + .dropdown-toggle-split, .btn-group-sm > .btn + .dropdown-toggle-split {
    padding-right: 0.375rem;
    padding-left: 0.375rem;
}

.btn-lg + .dropdown-toggle-split, .btn-group-lg > .btn + .dropdown-toggle-split {
    padding-right: 0.75rem;
    padding-left: 0.75rem;
}

.btn-group.show .dropdown-toggle {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-group.show .dropdown-toggle.btn-link {
    box-shadow: none;
}

.btn-group-vertical {
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
}

.btn-group-vertical > .btn,
  .btn-group-vertical > .btn-group {
    width: 100%;
}

.btn-group-vertical > .btn:not(:first-child),
  .btn-group-vertical > .btn-group:not(:first-child) {
    margin-top: -0.0625rem;
}

.btn-group-vertical > .btn:not(:last-child):not(.dropdown-toggle),
  .btn-group-vertical > .btn-group:not(:last-child) > .btn {
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
}

.btn-group-vertical > .btn:not(:first-child),
  .btn-group-vertical > .btn-group:not(:first-child) > .btn {
    border-top-left-radius: 0;
    border-top-right-radius: 0;
}

.btn-group-toggle > .btn,
.btn-group-toggle > .btn-group > .btn {
    margin-bottom: 0;
}

.btn-group-toggle > .btn input[type="radio"],
  .btn-group-toggle > .btn input[type="checkbox"],
  .btn-group-toggle > .btn-group > .btn input[type="radio"],
  .btn-group-toggle > .btn-group > .btn input[type="checkbox"] {
    position: absolute;
    clip: rect(0, 0, 0, 0);
    pointer-events: none;
}

.input-group {
    position: relative;
    display: flex;
    flex-wrap: wrap;
    align-items: stretch;
    width: 100%;
}

.input-group > .form-control,
  .input-group > .form-control-plaintext,
  .input-group > .custom-select,
  .input-group > .custom-file {
    position: relative;
    flex: 1 1 auto;
    width: 1%;
    margin-bottom: 0;
}

.input-group > .form-control + .form-control,
    .input-group > .form-control + .custom-select,
    .input-group > .form-control + .custom-file,
    .input-group > .form-control-plaintext + .form-control,
    .input-group > .form-control-plaintext + .custom-select,
    .input-group > .form-control-plaintext + .custom-file,
    .input-group > .custom-select + .form-control,
    .input-group > .custom-select + .custom-select,
    .input-group > .custom-select + .custom-file,
    .input-group > .custom-file + .form-control,
    .input-group > .custom-file + .custom-select,
    .input-group > .custom-file + .custom-file {
    margin-left: -0.0625rem;
}

.input-group > .form-control:focus,
  .input-group > .custom-select:focus,
  .input-group > .custom-file .custom-file-input:focus ~ .custom-file-label {
    z-index: 3;
}

.input-group > .custom-file .custom-file-input:focus {
    z-index: 4;
}

.input-group > .form-control:not(:last-child),
  .input-group > .custom-select:not(:last-child) {
    border-top-right-radius: 0;
    border-bottom-right-radius: 0;
}

.input-group > .form-control:not(:first-child),
  .input-group > .custom-select:not(:first-child) {
    border-top-left-radius: 0;
    border-bottom-left-radius: 0;
}

.input-group > .custom-file {
    display: flex;
    align-items: center;
}

.input-group > .custom-file:not(:last-child) .custom-file-label,
    .input-group > .custom-file:not(:last-child) .custom-file-label::after {
    border-top-right-radius: 0;
    border-bottom-right-radius: 0;
}

.input-group > .custom-file:not(:first-child) .custom-file-label {
    border-top-left-radius: 0;
    border-bottom-left-radius: 0;
}

.input-group-prepend,
.input-group-append {
    display: flex;
}

.input-group-prepend .btn,
  .input-group-append .btn {
    position: relative;
    z-index: 2;
}

.input-group-prepend .btn:focus,
    .input-group-append .btn:focus {
    z-index: 3;
}

.input-group-prepend .btn + .btn,
  .input-group-prepend .btn + .input-group-text,
  .input-group-prepend .input-group-text + .input-group-text,
  .input-group-prepend .input-group-text + .btn,
  .input-group-append .btn + .btn,
  .input-group-append .btn + .input-group-text,
  .input-group-append .input-group-text + .input-group-text,
  .input-group-append .input-group-text + .btn {
    margin-left: -0.0625rem;
}

.input-group-prepend {
    margin-right: -0.0625rem;
}

.input-group-append {
    margin-left: -0.0625rem;
}

.input-group-text {
    display: flex;
    align-items: center;
    padding: 0.6rem 0.75rem;
    margin-bottom: 0;
    font-size: 1rem;
    font-weight: 400;
    line-height: 1.5;
    color: #44476A;
    text-align: center;
    white-space: nowrap;
    background-color: #e6e7ee;
    border: 0.0625rem solid #D1D9E6;
    border-radius: 0.55rem;
}

.input-group-text input[type="radio"],
  .input-group-text input[type="checkbox"] {
    margin-top: 0;
}

.input-group-lg > .form-control:not(textarea),
.input-group-lg > .custom-select {
    height: calc(1.5em + 1.75rem + 0.0625rem);
}

.input-group-lg > .form-control,
.input-group-lg > .custom-select,
.input-group-lg > .input-group-prepend > .input-group-text,
.input-group-lg > .input-group-append > .input-group-text,
.input-group-lg > .input-group-prepend > .btn,
.input-group-lg > .input-group-append > .btn {
    padding: 0.875rem 1rem;
    font-size: 1.25rem;
    line-height: 1.5;
    border-radius: 0.3rem;
}

.input-group-sm > .form-control:not(textarea),
.input-group-sm > .custom-select {
    height: calc(1.5em + 0.9rem + 0.0625rem);
}

.input-group-sm > .form-control,
.input-group-sm > .custom-select,
.input-group-sm > .input-group-prepend > .input-group-text,
.input-group-sm > .input-group-append > .input-group-text,
.input-group-sm > .input-group-prepend > .btn,
.input-group-sm > .input-group-append > .btn {
    padding: 0.45rem 0.5rem;
    font-size: 0.875rem;
    line-height: 1.5;
    border-radius: 0.1rem;
}

.input-group-lg > .custom-select,
.input-group-sm > .custom-select {
    padding-right: 1.75rem;
}

.input-group > .input-group-prepend > .btn,
.input-group > .input-group-prepend > .input-group-text,
.input-group > .input-group-append:not(:last-child) > .btn,
.input-group > .input-group-append:not(:last-child) > .input-group-text,
.input-group > .input-group-append:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group > .input-group-append:last-child > .input-group-text:not(:last-child) {
    border-top-right-radius: 0;
    border-bottom-right-radius: 0;
}

.input-group > .input-group-append > .btn,
.input-group > .input-group-append > .input-group-text,
.input-group > .input-group-prepend:not(:first-child) > .btn,
.input-group > .input-group-prepend:not(:first-child) > .input-group-text,
.input-group > .input-group-prepend:first-child > .btn:not(:first-child),
.input-group > .input-group-prepend:first-child > .input-group-text:not(:first-child) {
    border-top-left-radius: 0;
    border-bottom-left-radius: 0;
}

.custom-control {
    position: relative;
    display: block;
    min-height: 1.5rem;
    padding-left: 3rem;
}

.custom-control-inline {
    display: inline-flex;
    margin-right: 1rem;
}

.custom-control-input {
    position: absolute;
    z-index: -1;
    opacity: 0;
}

.custom-control-input:checked ~ .custom-control-label::before {
    color: #ECF0F3;
    border-color: #e6e7ee;
    background-color: #e6e7ee;
    box-shadow: none;
}

.custom-control-input:focus ~ .custom-control-label::before {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF, none;
}

.custom-control-input:focus:not(:checked) ~ .custom-control-label::before {
    border-color: #D1D9E6;
}

.custom-control-input:not(:disabled):active ~ .custom-control-label::before {
    color: #ECF0F3;
    background-color: transparent;
    border-color: #e6e7ee;
    box-shadow: none;
}

.custom-control-input:disabled ~ .custom-control-label {
    color: #525480;
}

.custom-control-input:disabled ~ .custom-control-label::before {
    background-color: #fafbfe;
}

.custom-control-label {
    position: relative;
    margin-bottom: 0;
    vertical-align: top;
}

.custom-control-label::before {
    position: absolute;
    top: 0.125rem;
    left: -3rem;
    display: block;
    width: 1.25rem;
    height: 1.25rem;
    pointer-events: none;
    content: "";
    background-color: #ECF0F3;
    border: #b1bcce solid 1px;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.custom-control-label::after {
    position: absolute;
    top: 0.125rem;
    left: -3rem;
    display: block;
    width: 1.25rem;
    height: 1.25rem;
    content: "";
    background: no-repeat 50% / 50% 50%;
}

.custom-checkbox .custom-control-label::before {
    border-radius: 50%;
}

.custom-checkbox .custom-control-input:checked ~ .custom-control-label::after {
    background-image: "Font Awesome 5 Free";
}

.custom-checkbox .custom-control-input:indeterminate ~ .custom-control-label::before {
    border-color: #e6e7ee;
    background-color: #e6e7ee;
    box-shadow: none;
}

.custom-checkbox .custom-control-input:indeterminate ~ .custom-control-label::after {
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 4'%3e%3cpath stroke='%23ECF0F3' d='M0 2h4'/%3e%3c/svg%3e");
}

.custom-checkbox .custom-control-input:disabled:checked ~ .custom-control-label::before {
    background-color: rgba(230, 231, 238, 0.7);
}

.custom-checkbox .custom-control-input:disabled:indeterminate ~ .custom-control-label::before {
    background-color: rgba(230, 231, 238, 0.7);
}

.custom-radio .custom-control-label::before {
    border-radius: 50%;
}

.custom-radio .custom-control-input:checked ~ .custom-control-label::after {
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='-4 -4 8 8'%3e%3ccircle r='3' fill='%23ECF0F3'/%3e%3c/svg%3e");
}

.custom-radio .custom-control-input:disabled:checked ~ .custom-control-label::before {
    background-color: rgba(230, 231, 238, 0.7);
}

.custom-switch {
    padding-left: 4.25rem;
}

.custom-switch .custom-control-label::before {
    left: -4.25rem;
    width: 2.5rem;
    pointer-events: all;
    border-radius: 0.625rem;
}

.custom-switch .custom-control-label::after {
    top: calc(0.125rem + 2px);
    left: calc(-4.25rem + 2px);
    width: calc(1.25rem - 4px);
    height: calc(1.25rem - 4px);
    background-color: #b1bcce;
    border-radius: 0.625rem;
    transition: transform 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
    .custom-switch .custom-control-label::after {
        transition: none;
    }
}

.custom-switch .custom-control-input:checked ~ .custom-control-label::after {
    background-color: #ECF0F3;
    transform: translateX(1.25rem);
}

.custom-switch .custom-control-input:disabled:checked ~ .custom-control-label::before {
    background-color: rgba(230, 231, 238, 0.7);
}

.custom-select {
    display: inline-block;
    width: 100%;
    height: calc(1.5em + 1.2rem + 0.0625rem);
    padding: 0.6rem 1.75rem 0.6rem 0.75rem;
    font-size: 1rem;
    font-weight: 300;
    line-height: 1.5;
    color: #44476A;
    vertical-align: middle;
    background: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 5'%3e%3cpath fill='%23525480' d='M2 0L0 2h4zm0 5L0 3h4z'/%3e%3c/svg%3e") no-repeat right 0.75rem center/8px 10px;
    background-color: #e6e7ee;
    border: 0.0625rem solid #D1D9E6;
    border-radius: 0.55rem;
    box-shadow: inset 0 1px 2px rgba(38, 40, 51, 0.075);
    -webkit-appearance: none;
    appearance: none;
}

.custom-select:focus {
    border-color: #D1D9E6;
    outline: 0;
    box-shadow: inset 0 1px 2px rgba(38, 40, 51, 0.075), 0 0 0 0 #e6e7ee;
}

.custom-select:focus::-ms-value {
    color: #44476A;
    background-color: #e6e7ee;
}

.custom-select[multiple], .custom-select[size]:not([size="1"]) {
    height: auto;
    padding-right: 0.75rem;
    background-image: none;
}

.custom-select:disabled {
    color: #93a5be;
    background-color: #fafbfe;
}

.custom-select::-ms-expand {
    display: none;
}

.custom-select-sm {
    height: calc(1.5em + 0.9rem + 0.0625rem);
    padding-top: 0.45rem;
    padding-bottom: 0.45rem;
    padding-left: 0.5rem;
    font-size: 0.875rem;
}

.custom-select-lg {
    height: calc(1.5em + 1.75rem + 0.0625rem);
    padding-top: 0.875rem;
    padding-bottom: 0.875rem;
    padding-left: 1rem;
    font-size: 1.25rem;
}

.custom-file {
    position: relative;
    display: inline-block;
    width: 100%;
    height: calc(1.5em + 1.2rem + 0.0625rem);
    margin-bottom: 0;
}

.custom-file-input {
    position: relative;
    z-index: 2;
    width: 100%;
    height: calc(1.5em + 1.2rem + 0.0625rem);
    margin: 0;
    opacity: 0;
}

.custom-file-input:focus ~ .custom-file-label {
    border-color: #D1D9E6;
    box-shadow: none;
}

.custom-file-input:disabled ~ .custom-file-label {
    background-color: #e6e7ee;
}

.custom-file-input:lang(en) ~ .custom-file-label::after {
    content: "Browse";
}

.custom-file-input ~ .custom-file-label[data-browse]::after {
    content: attr(data-browse);
}

.custom-file-label {
    position: absolute;
    top: 0;
    right: 0;
    left: 0;
    z-index: 1;
    height: calc(1.5em + 1.2rem + 0.0625rem);
    padding: 0.6rem 0.75rem;
    font-weight: 300;
    line-height: 1.5;
    color: #44476A;
    background-color: #e6e7ee;
    border: 0.0625rem solid #D1D9E6;
    border-radius: 0.55rem;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.custom-file-label::after {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    z-index: 3;
    display: block;
    height: calc(1.5em + 1.2rem);
    padding: 0.6rem 0.75rem;
    line-height: 1.5;
    color: #44476A;
    content: "Browse";
    background-color: #e6e7ee;
    border-left: inherit;
    border-radius: 0 0.55rem 0.55rem 0;
}

.custom-range {
    width: 100%;
    height: calc(1rem + 0);
    padding: 0;
    background-color: transparent;
    -webkit-appearance: none;
    appearance: none;
}

.custom-range:focus {
    outline: none;
}

.custom-range:focus::-webkit-slider-thumb {
    box-shadow: 0 0 0 1px #e6e7ee, none;
}

.custom-range:focus::-moz-range-thumb {
    box-shadow: 0 0 0 1px #e6e7ee, none;
}

.custom-range:focus::-ms-thumb {
    box-shadow: 0 0 0 1px #e6e7ee, none;
}

.custom-range::-moz-focus-outer {
    border: 0;
}

.custom-range::-webkit-slider-thumb {
    width: 1rem;
    height: 1rem;
    margin-top: -0.25rem;
    background-color: #e6e7ee;
    border: 0;
    border-radius: 1rem;
    box-shadow: 0 0.1rem 0.25rem rgba(38, 40, 51, 0.1);
    -webkit-transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    -webkit-appearance: none;
    appearance: none;
}

@media (prefers-reduced-motion: reduce) {
    .custom-range::-webkit-slider-thumb {
        -webkit-transition: none;
        transition: none;
    }
}

.custom-range::-webkit-slider-thumb:active {
    background-color: white;
}

.custom-range::-webkit-slider-runnable-track {
    width: 100%;
    height: 0.5rem;
    color: transparent;
    cursor: pointer;
    background-color: #e6e7ee;
    border-color: transparent;
    border-radius: 1rem;
    box-shadow: inset 0 0.25rem 0.25rem rgba(38, 40, 51, 0.1);
}

.custom-range::-moz-range-thumb {
    width: 1rem;
    height: 1rem;
    background-color: #e6e7ee;
    border: 0;
    border-radius: 1rem;
    box-shadow: 0 0.1rem 0.25rem rgba(38, 40, 51, 0.1);
    -moz-transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    appearance: none;
}

@media (prefers-reduced-motion: reduce) {
    .custom-range::-moz-range-thumb {
        -moz-transition: none;
        transition: none;
    }
}

.custom-range::-moz-range-thumb:active {
    background-color: white;
}

.custom-range::-moz-range-track {
    width: 100%;
    height: 0.5rem;
    color: transparent;
    cursor: pointer;
    background-color: #e6e7ee;
    border-color: transparent;
    border-radius: 1rem;
    box-shadow: inset 0 0.25rem 0.25rem rgba(38, 40, 51, 0.1);
}

.custom-range::-ms-thumb {
    width: 1rem;
    height: 1rem;
    margin-top: 0;
    margin-right: 0;
    margin-left: 0;
    background-color: #e6e7ee;
    border: 0;
    border-radius: 1rem;
    box-shadow: 0 0.1rem 0.25rem rgba(38, 40, 51, 0.1);
    -ms-transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
    appearance: none;
}

@media (prefers-reduced-motion: reduce) {
    .custom-range::-ms-thumb {
        -ms-transition: none;
        transition: none;
    }
}

.custom-range::-ms-thumb:active {
    background-color: white;
}

.custom-range::-ms-track {
    width: 100%;
    height: 0.5rem;
    color: transparent;
    cursor: pointer;
    background-color: transparent;
    border-color: transparent;
    border-width: 0.5rem;
    box-shadow: inset 0 0.25rem 0.25rem rgba(38, 40, 51, 0.1);
}

.custom-range::-ms-fill-lower {
    background-color: #e6e7ee;
    border-radius: 1rem;
}

.custom-range::-ms-fill-upper {
    margin-right: 15px;
    background-color: #e6e7ee;
    border-radius: 1rem;
}

.custom-range:disabled::-webkit-slider-thumb {
    background-color: #b1bcce;
}

.custom-range:disabled::-webkit-slider-runnable-track {
    cursor: default;
}

.custom-range:disabled::-moz-range-thumb {
    background-color: #b1bcce;
}

.custom-range:disabled::-moz-range-track {
    cursor: default;
}

.custom-range:disabled::-ms-thumb {
    background-color: #b1bcce;
}

.custom-control-label::before,
.custom-file-label,
.custom-select {
    transition: background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
    .custom-control-label::before,
    .custom-file-label,
    .custom-select {
        transition: none;
    }
}

.nav {
    display: flex;
    flex-wrap: wrap;
    padding-left: 0;
    margin-bottom: 0;
    list-style: none;
}

.nav-link {
    display: block;
    padding: 0.25rem 0.75rem;
}

.nav-link:hover, .nav-link:focus {
    text-decoration: none;
}

.nav-link.disabled {
    color: #93a5be;
    pointer-events: none;
    cursor: default;
}

.nav-tabs {
    border-bottom: 0.0625rem solid #fafbfe;
}

.nav-tabs .nav-item {
    margin-bottom: -0.0625rem;
}

.nav-tabs .nav-link {
    border: 0.0625rem solid transparent;
    border-top-left-radius: 0.55rem;
    border-top-right-radius: 0.55rem;
}

.nav-tabs .nav-link:hover, .nav-tabs .nav-link:focus {
    border-color: #fafbfe #fafbfe #fafbfe;
}

.nav-tabs .nav-link.disabled {
    color: #93a5be;
    background-color: transparent;
    border-color: transparent;
}

.nav-tabs .nav-link.active,
  .nav-tabs .nav-item.show .nav-link {
    color: #e6e7ee;
    background-color: #f3f7fa;
    border-color: #e6e7ee #e6e7ee #f3f7fa;
}

.nav-tabs .dropdown-menu {
    margin-top: -0.0625rem;
    border-top-left-radius: 0;
    border-top-right-radius: 0;
}

.nav-pills .nav-link {
    border-radius: 0.55rem;
}

.nav-pills .nav-link.active,
.nav-pills .show > .nav-link {
    color: #31344b;
    background-color: #e6e7ee;
}

.nav-fill .nav-item {
    flex: 1 1 auto;
    text-align: center;
}

.nav-justified .nav-item {
    flex-basis: 0;
    flex-grow: 1;
    text-align: center;
}

.tab-content > .tab-pane {
    display: none;
}

.tab-content > .active {
    display: block;
}

.navbar {
    position: relative;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 1rem;
}

.navbar > .container,
  .navbar > .container-fluid {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
}

.navbar-brand {
    display: inline-block;
    padding-top: 0.0625rem;
    padding-bottom: 0.0625rem;
    margin-right: 1rem;
    font-size: 1.25rem;
    line-height: inherit;
    white-space: nowrap;
}

.navbar-brand:hover, .navbar-brand:focus {
    text-decoration: none;
}

.navbar-nav {
    display: flex;
    flex-direction: column;
    padding-left: 0;
    margin-bottom: 0;
    list-style: none;
}

.navbar-nav .nav-link {
    padding-right: 0;
    padding-left: 0;
}

.navbar-nav .dropdown-menu {
    position: static;
    float: none;
}

.navbar-text {
    display: inline-block;
    padding-top: 0.25rem;
    padding-bottom: 0.25rem;
}

.navbar-collapse {
    flex-basis: 100%;
    flex-grow: 1;
    align-items: center;
}

.navbar-toggler {
    padding: 0.25rem 0.75rem;
    font-size: 1.25rem;
    line-height: 1;
    background-color: transparent;
    border: 0.0625rem solid transparent;
    border-radius: 0.55rem;
}

.navbar-toggler:hover, .navbar-toggler:focus {
    text-decoration: none;
}

.navbar-toggler-icon {
    display: inline-block;
    width: 1.5em;
    height: 1.5em;
    vertical-align: middle;
    content: "";
    background: no-repeat center center;
    background-size: 100% 100%;
}

@media (max-width: 575.98px) {
    .navbar-expand-sm > .container,
  .navbar-expand-sm > .container-fluid {
        padding-right: 0;
        padding-left: 0;
    }
}

@media (min-width: 576px) {
    .navbar-expand-sm {
        flex-flow: row nowrap;
        justify-content: flex-start;
    }

    .navbar-expand-sm .navbar-nav {
        flex-direction: row;
    }

    .navbar-expand-sm .navbar-nav .dropdown-menu {
        position: absolute;
    }

    .navbar-expand-sm .navbar-nav .nav-link {
        padding-right: 1rem;
        padding-left: 1rem;
    }

    .navbar-expand-sm > .container,
    .navbar-expand-sm > .container-fluid {
        flex-wrap: nowrap;
    }

    .navbar-expand-sm .navbar-collapse {
        display: flex !important;
        flex-basis: auto;
    }

    .navbar-expand-sm .navbar-toggler {
        display: none;
    }
}

@media (max-width: 767.98px) {
    .navbar-expand-md > .container,
  .navbar-expand-md > .container-fluid {
        padding-right: 0;
        padding-left: 0;
    }
}

@media (min-width: 768px) {
    .navbar-expand-md {
        flex-flow: row nowrap;
        justify-content: flex-start;
    }

    .navbar-expand-md .navbar-nav {
        flex-direction: row;
    }

    .navbar-expand-md .navbar-nav .dropdown-menu {
        position: absolute;
    }

    .navbar-expand-md .navbar-nav .nav-link {
        padding-right: 1rem;
        padding-left: 1rem;
    }

    .navbar-expand-md > .container,
    .navbar-expand-md > .container-fluid {
        flex-wrap: nowrap;
    }

    .navbar-expand-md .navbar-collapse {
        display: flex !important;
        flex-basis: auto;
    }

    .navbar-expand-md .navbar-toggler {
        display: none;
    }
}

@media (max-width: 991.98px) {
    .navbar-expand-lg > .container,
  .navbar-expand-lg > .container-fluid {
        padding-right: 0;
        padding-left: 0;
    }
}

@media (min-width: 992px) {
    .navbar-expand-lg {
        flex-flow: row nowrap;
        justify-content: flex-start;
    }

    .navbar-expand-lg .navbar-nav {
        flex-direction: row;
    }

    .navbar-expand-lg .navbar-nav .dropdown-menu {
        position: absolute;
    }

    .navbar-expand-lg .navbar-nav .nav-link {
        padding-right: 1rem;
        padding-left: 1rem;
    }

    .navbar-expand-lg > .container,
    .navbar-expand-lg > .container-fluid {
        flex-wrap: nowrap;
    }

    .navbar-expand-lg .navbar-collapse {
        display: flex !important;
        flex-basis: auto;
    }

    .navbar-expand-lg .navbar-toggler {
        display: none;
    }
}

@media (max-width: 1199.98px) {
    .navbar-expand-xl > .container,
  .navbar-expand-xl > .container-fluid {
        padding-right: 0;
        padding-left: 0;
    }
}

@media (min-width: 1200px) {
    .navbar-expand-xl {
        flex-flow: row nowrap;
        justify-content: flex-start;
    }

    .navbar-expand-xl .navbar-nav {
        flex-direction: row;
    }

    .navbar-expand-xl .navbar-nav .dropdown-menu {
        position: absolute;
    }

    .navbar-expand-xl .navbar-nav .nav-link {
        padding-right: 1rem;
        padding-left: 1rem;
    }

    .navbar-expand-xl > .container,
    .navbar-expand-xl > .container-fluid {
        flex-wrap: nowrap;
    }

    .navbar-expand-xl .navbar-collapse {
        display: flex !important;
        flex-basis: auto;
    }

    .navbar-expand-xl .navbar-toggler {
        display: none;
    }
}

.navbar-expand {
    flex-flow: row nowrap;
    justify-content: flex-start;
}

.navbar-expand > .container,
  .navbar-expand > .container-fluid {
    padding-right: 0;
    padding-left: 0;
}

.navbar-expand .navbar-nav {
    flex-direction: row;
}

.navbar-expand .navbar-nav .dropdown-menu {
    position: absolute;
}

.navbar-expand .navbar-nav .nav-link {
    padding-right: 1rem;
    padding-left: 1rem;
}

.navbar-expand > .container,
  .navbar-expand > .container-fluid {
    flex-wrap: nowrap;
}

.navbar-expand .navbar-collapse {
    display: flex !important;
    flex-basis: auto;
}

.navbar-expand .navbar-toggler {
    display: none;
}

.navbar-light .navbar-brand {
    color: #44476A;
}

.navbar-light .navbar-brand:hover, .navbar-light .navbar-brand:focus {
    color: #44476A;
}

.navbar-light .navbar-nav .nav-link {
    color: #44476A;
}

.navbar-light .navbar-nav .nav-link:hover, .navbar-light .navbar-nav .nav-link:focus {
    color: #31344b;
}

.navbar-light .navbar-nav .nav-link.disabled {
    color: rgba(82, 84, 128, 0.9);
}

.navbar-light .navbar-nav .show > .nav-link,
.navbar-light .navbar-nav .active > .nav-link,
.navbar-light .navbar-nav .nav-link.show,
.navbar-light .navbar-nav .nav-link.active {
    color: #44476A;
}

.navbar-light .navbar-toggler {
    color: #44476A;
    border-color: transparent;
}

.navbar-light .navbar-toggler-icon {
    background-image: url("data:image/svg+xml;charset=utf8,%3Csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath stroke='%2344476A' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3E%3C/svg%3E");
}

.navbar-light .navbar-text {
    color: #44476A;
}

.navbar-light .navbar-text a {
    color: #44476A;
}

.navbar-light .navbar-text a:hover, .navbar-light .navbar-text a:focus {
    color: #44476A;
}

.navbar-dark .navbar-brand {
    color: rgba(236, 240, 243, 0.65);
}

.navbar-dark .navbar-brand:hover, .navbar-dark .navbar-brand:focus {
    color: rgba(236, 240, 243, 0.65);
}

.navbar-dark .navbar-nav .nav-link {
    color: #31344b;
}

.navbar-dark .navbar-nav .nav-link:hover, .navbar-dark .navbar-nav .nav-link:focus {
    color: #262833;
}

.navbar-dark .navbar-nav .nav-link.disabled {
    color: rgba(236, 240, 243, 0.25);
}

.navbar-dark .navbar-nav .show > .nav-link,
.navbar-dark .navbar-nav .active > .nav-link,
.navbar-dark .navbar-nav .nav-link.show,
.navbar-dark .navbar-nav .nav-link.active {
    color: rgba(236, 240, 243, 0.65);
}

.navbar-dark .navbar-toggler {
    color: #31344b;
    border-color: transparent;
}

.navbar-dark .navbar-toggler-icon {
    background-image: url("data:image/svg+xml,%3csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3e%3cpath stroke='%2331344b' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e");
}

.navbar-dark .navbar-text {
    color: #31344b;
}

.navbar-dark .navbar-text a {
    color: rgba(236, 240, 243, 0.65);
}

.navbar-dark .navbar-text a:hover, .navbar-dark .navbar-text a:focus {
    color: rgba(236, 240, 243, 0.65);
}

.card {
    position: relative;
    display: flex;
    flex-direction: column;
    min-width: 0;
    word-wrap: break-word;
    background-color: #e6e7ee;
    background-clip: border-box;
    border: 0.0625rem solid rgba(243, 247, 250, 0.05);
    border-radius: 0.55rem;
}

.card > hr {
    margin-right: 0;
    margin-left: 0;
}

.card > .list-group:first-child .list-group-item:first-child {
    border-top-left-radius: 0.55rem;
    border-top-right-radius: 0.55rem;
}

.card > .list-group:last-child .list-group-item:last-child {
    border-bottom-right-radius: 0.55rem;
    border-bottom-left-radius: 0.55rem;
}

.card-body {
    flex: 1 1 auto;
    padding: 1.5rem;
}

.card-title {
    margin-bottom: 1.25rem;
}

.card-subtitle {
    margin-top: -0.625rem;
    margin-bottom: 0;
}

.card-text:last-child {
    margin-bottom: 0;
}

.card-link:hover {
    text-decoration: none;
}

.card-link + .card-link {
    margin-left: 1.5rem;
}

.card-header {
    padding: 1.25rem 1.5rem;
    margin-bottom: 0;
    background-color: #f3f7fa;
    border-bottom: 0.0625rem solid rgba(243, 247, 250, 0.05);
}

.card-header:first-child {
    border-radius: calc(0.55rem - 0.0625rem) calc(0.55rem - 0.0625rem) 0 0;
}

.card-header + .list-group .list-group-item:first-child {
    border-top: 0;
}

.card-footer {
    padding: 1.25rem 1.5rem;
    background-color: #f3f7fa;
    border-top: 0.0625rem solid rgba(243, 247, 250, 0.05);
}

.card-footer:last-child {
    border-radius: 0 0 calc(0.55rem - 0.0625rem) calc(0.55rem - 0.0625rem);
}

.card-header-tabs {
    margin-right: -0.75rem;
    margin-bottom: -1.25rem;
    margin-left: -0.75rem;
    border-bottom: 0;
}

.card-header-pills {
    margin-right: -0.75rem;
    margin-left: -0.75rem;
}

.card-img-overlay {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    padding: 1.25rem;
}

.card-img {
    width: 100%;
    border-radius: calc(0.55rem - 0.0625rem);
}

.card-img-top {
    width: 100%;
    border-top-left-radius: calc(0.55rem - 0.0625rem);
    border-top-right-radius: calc(0.55rem - 0.0625rem);
}

.card-img-bottom {
    width: 100%;
    border-bottom-right-radius: calc(0.55rem - 0.0625rem);
    border-bottom-left-radius: calc(0.55rem - 0.0625rem);
}

.card-deck {
    display: flex;
    flex-direction: column;
}

.card-deck .card {
    margin-bottom: 15px;
}

@media (min-width: 576px) {
    .card-deck {
        flex-flow: row wrap;
        margin-right: -15px;
        margin-left: -15px;
    }

    .card-deck .card {
        display: flex;
        flex: 1 0 0%;
        flex-direction: column;
        margin-right: 15px;
        margin-bottom: 0;
        margin-left: 15px;
    }
}

.card-group {
    display: flex;
    flex-direction: column;
}

.card-group > .card {
    margin-bottom: 15px;
}

@media (min-width: 576px) {
    .card-group {
        flex-flow: row wrap;
    }

    .card-group > .card {
        flex: 1 0 0%;
        margin-bottom: 0;
    }

    .card-group > .card + .card {
        margin-left: 0;
        border-left: 0;
    }

    .card-group > .card:not(:last-child) {
        border-top-right-radius: 0;
        border-bottom-right-radius: 0;
    }

    .card-group > .card:not(:last-child) .card-img-top,
          .card-group > .card:not(:last-child) .card-header {
        border-top-right-radius: 0;
    }

    .card-group > .card:not(:last-child) .card-img-bottom,
          .card-group > .card:not(:last-child) .card-footer {
        border-bottom-right-radius: 0;
    }

    .card-group > .card:not(:first-child) {
        border-top-left-radius: 0;
        border-bottom-left-radius: 0;
    }

    .card-group > .card:not(:first-child) .card-img-top,
          .card-group > .card:not(:first-child) .card-header {
        border-top-left-radius: 0;
    }

    .card-group > .card:not(:first-child) .card-img-bottom,
          .card-group > .card:not(:first-child) .card-footer {
        border-bottom-left-radius: 0;
    }
}

.card-columns .card {
    margin-bottom: 1.25rem;
}

@media (min-width: 576px) {
    .card-columns {
        column-count: 3;
        column-gap: 1.25rem;
        orphans: 1;
        widows: 1;
    }

    .card-columns .card {
        display: inline-block;
        width: 100%;
    }
}

.accordion > .card {
    overflow: hidden;
}

.accordion > .card:not(:first-of-type) .card-header:first-child {
    border-radius: 0;
}

.accordion > .card:not(:first-of-type):not(:last-of-type) {
    border-bottom: 0;
    border-radius: 0;
}

.accordion > .card:first-of-type {
    border-bottom: 0;
    border-bottom-right-radius: 0;
    border-bottom-left-radius: 0;
}

.accordion > .card:last-of-type {
    border-top-left-radius: 0;
    border-top-right-radius: 0;
}

.accordion > .card .card-header {
    margin-bottom: -0.0625rem;
}

.breadcrumb {
    display: flex;
    flex-wrap: wrap;
    padding: 0.75rem 1rem;
    margin-bottom: 1rem;
    list-style: none;
    background-color: #fafbfe;
    border-radius: 0.55rem;
}

.breadcrumb-item + .breadcrumb-item {
    padding-left: 0.5rem;
}

.breadcrumb-item + .breadcrumb-item::before {
    display: inline-block;
    padding-right: 0.5rem;
    color: #66799e;
    content: "/";
}

.breadcrumb-item + .breadcrumb-item:hover::before {
    text-decoration: underline;
}

.breadcrumb-item + .breadcrumb-item:hover::before {
    text-decoration: none;
}

.breadcrumb-item.active {
    color: #ECF0F3;
}

.pagination {
    display: flex;
    padding-left: 0;
    list-style: none;
    border-radius: 0.55rem;
}

.page-link {
    position: relative;
    display: block;
    padding: 0.5rem 0.75rem;
    margin-left: -0.0625rem;
    line-height: 1.25;
    color: #93a5be;
    background-color: #ECF0F3;
    border: 0.0625rem solid #fafbfe;
}

.page-link:hover {
    z-index: 2;
    color: #93a5be;
    text-decoration: none;
    background-color: #fafbfe;
    border-color: #fafbfe;
}

.page-link:focus {
    z-index: 2;
    outline: 0;
    box-shadow: none;
}

.page-item:first-child .page-link {
    margin-left: 0;
    border-top-left-radius: 0.55rem;
    border-bottom-left-radius: 0.55rem;
}

.page-item:last-child .page-link {
    border-top-right-radius: 0.55rem;
    border-bottom-right-radius: 0.55rem;
}

.page-item.active .page-link {
    z-index: 1;
    color: #ECF0F3;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
}

.page-item.disabled .page-link {
    color: #525480;
    pointer-events: none;
    cursor: auto;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
}

.pagination-lg .page-link {
    padding: 0.75rem 1.5rem;
    font-size: 1.25rem;
    line-height: 1.5;
}

.pagination-lg .page-item:first-child .page-link {
    border-top-left-radius: 0.3rem;
    border-bottom-left-radius: 0.3rem;
}

.pagination-lg .page-item:last-child .page-link {
    border-top-right-radius: 0.3rem;
    border-bottom-right-radius: 0.3rem;
}

.pagination-sm .page-link {
    padding: 0.25rem 0.5rem;
    font-size: 0.875rem;
    line-height: 1.5;
}

.pagination-sm .page-item:first-child .page-link {
    border-top-left-radius: 0.1rem;
    border-bottom-left-radius: 0.1rem;
}

.pagination-sm .page-item:last-child .page-link {
    border-top-right-radius: 0.1rem;
    border-bottom-right-radius: 0.1rem;
}

.badge {
    display: inline-block;
    padding: 0.275rem 0.425rem;
    font-size: 0.7rem;
    font-weight: 600;
    line-height: 1;
    text-align: center;
    white-space: nowrap;
    vertical-align: baseline;
    border-radius: 0.55rem;
    transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
    .badge {
        transition: none;
    }
}

a.badge:hover, a.badge:focus {
    text-decoration: none;
}

.badge:empty {
    display: none;
}

.btn .badge {
    position: relative;
    top: -1px;
}

.badge-pill {
    padding-right: 0.875em;
    padding-left: 0.875em;
    border-radius: 10rem;
}

.badge-primary {
    color: #31344b;
    background-color: #e6e7ee;
}

a.badge-primary:hover, a.badge-primary:focus {
    color: #31344b;
    background-color: #c8cad9;
}

a.badge-primary:focus, a.badge-primary.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(230, 231, 238, 0.5);
}

.badge-secondary {
    color: #ECF0F3;
    background-color: #2D4CC8;
}

a.badge-secondary:hover, a.badge-secondary:focus {
    color: #ECF0F3;
    background-color: #243c9e;
}

a.badge-secondary:focus, a.badge-secondary.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(45, 76, 200, 0.5);
}

.badge-success {
    color: #ECF0F3;
    background-color: #18634B;
}

a.badge-success:hover, a.badge-success:focus {
    color: #ECF0F3;
    background-color: #0e3a2c;
}

a.badge-success:focus, a.badge-success.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(24, 99, 75, 0.5);
}

.badge-info {
    color: #ECF0F3;
    background-color: #0056B3;
}

a.badge-info:hover, a.badge-info:focus {
    color: #ECF0F3;
    background-color: #003d80;
}

a.badge-info:focus, a.badge-info.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(0, 86, 179, 0.5);
}

.badge-warning {
    color: #ECF0F3;
    background-color: #F0B400;
}

a.badge-warning:hover, a.badge-warning:focus {
    color: #ECF0F3;
    background-color: #bd8e00;
}

a.badge-warning:focus, a.badge-warning.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(240, 180, 0, 0.5);
}

.badge-danger {
    color: #ECF0F3;
    background-color: #A91E2C;
}

a.badge-danger:hover, a.badge-danger:focus {
    color: #ECF0F3;
    background-color: #7e1621;
}

a.badge-danger:focus, a.badge-danger.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(169, 30, 44, 0.5);
}

.badge-light {
    color: #31344b;
    background-color: #D1D9E6;
}

a.badge-light:hover, a.badge-light:focus {
    color: #31344b;
    background-color: #b0bed4;
}

a.badge-light:focus, a.badge-light.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(209, 217, 230, 0.5);
}

.badge-dark {
    color: #ECF0F3;
    background-color: #31344b;
}

a.badge-dark:hover, a.badge-dark:focus {
    color: #ECF0F3;
    background-color: #1d1f2c;
}

a.badge-dark:focus, a.badge-dark.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(49, 52, 75, 0.5);
}

.badge-default {
    color: #ECF0F3;
    background-color: #262833;
}

a.badge-default:hover, a.badge-default:focus {
    color: #ECF0F3;
    background-color: #101116;
}

a.badge-default:focus, a.badge-default.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(38, 40, 51, 0.5);
}

.badge-white {
    color: #31344b;
    background-color: #ECF0F3;
}

a.badge-white:hover, a.badge-white:focus {
    color: #31344b;
    background-color: #cdd7df;
}

a.badge-white:focus, a.badge-white.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(236, 240, 243, 0.5);
}

.badge-gray {
    color: #ECF0F3;
    background-color: #44476A;
}

a.badge-gray:hover, a.badge-gray:focus {
    color: #ECF0F3;
    background-color: #30324b;
}

a.badge-gray:focus, a.badge-gray.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(68, 71, 106, 0.5);
}

.badge-neutral {
    color: #31344b;
    background-color: #ECF0F3;
}

a.badge-neutral:hover, a.badge-neutral:focus {
    color: #31344b;
    background-color: #cdd7df;
}

a.badge-neutral:focus, a.badge-neutral.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(236, 240, 243, 0.5);
}

.badge-soft {
    color: #31344b;
    background-color: #e6e7ee;
}

a.badge-soft:hover, a.badge-soft:focus {
    color: #31344b;
    background-color: #c8cad9;
}

a.badge-soft:focus, a.badge-soft.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(230, 231, 238, 0.5);
}

.badge-black {
    color: #ECF0F3;
    background-color: #262833;
}

a.badge-black:hover, a.badge-black:focus {
    color: #ECF0F3;
    background-color: #101116;
}

a.badge-black:focus, a.badge-black.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(38, 40, 51, 0.5);
}

.badge-purple {
    color: #ECF0F3;
    background-color: #6f42c1;
}

a.badge-purple:hover, a.badge-purple:focus {
    color: #ECF0F3;
    background-color: #59339d;
}

a.badge-purple:focus, a.badge-purple.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(111, 66, 193, 0.5);
}

.badge-gray-100 {
    color: #31344b;
    background-color: #f3f7fa;
}

a.badge-gray-100:hover, a.badge-gray-100:focus {
    color: #31344b;
    background-color: #cfdfeb;
}

a.badge-gray-100:focus, a.badge-gray-100.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(243, 247, 250, 0.5);
}

.badge-gray-200 {
    color: #31344b;
    background-color: #fafbfe;
}

a.badge-gray-200:hover, a.badge-gray-200:focus {
    color: #31344b;
    background-color: #d0d9f6;
}

a.badge-gray-200:focus, a.badge-gray-200.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(250, 251, 254, 0.5);
}

.badge-gray-300 {
    color: #31344b;
    background-color: #e6e7ee;
}

a.badge-gray-300:hover, a.badge-gray-300:focus {
    color: #31344b;
    background-color: #c8cad9;
}

a.badge-gray-300:focus, a.badge-gray-300.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(230, 231, 238, 0.5);
}

.badge-gray-400 {
    color: #31344b;
    background-color: #D1D9E6;
}

a.badge-gray-400:hover, a.badge-gray-400:focus {
    color: #31344b;
    background-color: #b0bed4;
}

a.badge-gray-400:focus, a.badge-gray-400.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(209, 217, 230, 0.5);
}

.badge-gray-500 {
    color: #ECF0F3;
    background-color: #b1bcce;
}

a.badge-gray-500:hover, a.badge-gray-500:focus {
    color: #ECF0F3;
    background-color: #92a1ba;
}

a.badge-gray-500:focus, a.badge-gray-500.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(177, 188, 206, 0.5);
}

.badge-gray-600 {
    color: #ECF0F3;
    background-color: #93a5be;
}

a.badge-gray-600:hover, a.badge-gray-600:focus {
    color: #ECF0F3;
    background-color: #738aab;
}

a.badge-gray-600:focus, a.badge-gray-600.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(147, 165, 190, 0.5);
}

.badge-gray-700 {
    color: #ECF0F3;
    background-color: #66799e;
}

a.badge-gray-700:hover, a.badge-gray-700:focus {
    color: #ECF0F3;
    background-color: #516180;
}

a.badge-gray-700:focus, a.badge-gray-700.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(102, 121, 158, 0.5);
}

.badge-gray-800 {
    color: #ECF0F3;
    background-color: #525480;
}

a.badge-gray-800:hover, a.badge-gray-800:focus {
    color: #ECF0F3;
    background-color: #3e4061;
}

a.badge-gray-800:focus, a.badge-gray-800.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(82, 84, 128, 0.5);
}

.badge-facebook {
    color: #ECF0F3;
    background-color: #3b5999;
}

a.badge-facebook:hover, a.badge-facebook:focus {
    color: #ECF0F3;
    background-color: #2d4474;
}

a.badge-facebook:focus, a.badge-facebook.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(59, 89, 153, 0.5);
}

.badge-dribbble {
    color: #ECF0F3;
    background-color: #ea4c89;
}

a.badge-dribbble:hover, a.badge-dribbble:focus {
    color: #ECF0F3;
    background-color: #e51e6b;
}

a.badge-dribbble:focus, a.badge-dribbble.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(234, 76, 137, 0.5);
}

.badge-github {
    color: #ECF0F3;
    background-color: #222222;
}

a.badge-github:hover, a.badge-github:focus {
    color: #ECF0F3;
    background-color: #090909;
}

a.badge-github:focus, a.badge-github.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(34, 34, 34, 0.5);
}

.badge-behance {
    color: #ECF0F3;
    background-color: #0057ff;
}

a.badge-behance:hover, a.badge-behance:focus {
    color: #ECF0F3;
    background-color: #0046cc;
}

a.badge-behance:focus, a.badge-behance.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(0, 87, 255, 0.5);
}

.badge-twitter {
    color: #ECF0F3;
    background-color: #1da1f2;
}

a.badge-twitter:hover, a.badge-twitter:focus {
    color: #ECF0F3;
    background-color: #0c85d0;
}

a.badge-twitter:focus, a.badge-twitter.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(29, 161, 242, 0.5);
}

.badge-slack {
    color: #ECF0F3;
    background-color: #3aaf85;
}

a.badge-slack:hover, a.badge-slack:focus {
    color: #ECF0F3;
    background-color: #2d8968;
}

a.badge-slack:focus, a.badge-slack.focus {
    outline: 0;
    box-shadow: 0 0 0 0 rgba(58, 175, 133, 0.5);
}

.jumbotron {
    padding: 2rem 1rem;
    margin-bottom: 2rem;
    background-color: #fafbfe;
    border-radius: 0.3rem;
}

@media (min-width: 576px) {
    .jumbotron {
        padding: 4rem 2rem;
    }
}

.jumbotron-fluid {
    padding-right: 0;
    padding-left: 0;
    border-radius: 0;
}

.alert {
    position: relative;
    padding: 1rem 1.5rem;
    margin-bottom: 1rem;
    border: 0.0625rem solid transparent;
    border-radius: 0.55rem;
}

.alert-heading {
    color: inherit;
}

.alert-link {
    font-weight: 600;
}

.alert-dismissible {
    padding-right: 4.5rem;
}

.alert-dismissible .close {
    position: absolute;
    top: 0;
    right: 0;
    padding: 1rem 1.5rem;
    color: inherit;
}

.alert-primary {
    color: #c7c8d0;
    background-color: #e6e8ee;
    border-color: #d7d8df;
}

.alert-primary hr {
    border-top-color: #c9cad4;
}

.alert-primary .alert-link {
    color: #abadb9;
}

.alert-secondary {
    color: #2c46b0;
    background-color: #3c59cb;
    border-color: #2c49bc;
}

.alert-secondary hr {
    border-top-color: #2741a7;
}

.alert-secondary .alert-link {
    color: #223687;
}

.alert-success {
    color: #1a5a47;
    background-color: #296e58;
    border-color: #195e49;
}

.alert-success hr {
    border-top-color: #144a39;
}

.alert-success .alert-link {
    color: #0f3228;
}

.alert-info {
    color: #064f9f;
    background-color: #1362b8;
    border-color: #0352a9;
}

.alert-info hr {
    border-top-color: #034690;
}

.alert-info .alert-link {
    color: #04376e;
}

.alert-warning {
    color: #d09e08;
    background-color: #f0b913;
    border-color: #e0a904;
}

.alert-warning hr {
    border-top-color: #c79604;
}

.alert-warning .alert-link {
    color: #9f7906;
}

.alert-danger {
    color: #94202d;
    background-color: #ae2f3c;
    border-color: #9f1f2d;
}

.alert-danger hr {
    border-top-color: #8a1b27;
}

.alert-danger .alert-link {
    color: #6a1720;
}

.alert-light {
    color: #b6bdc9;
    background-color: #d3dbe7;
    border-color: #c3cbd8;
}

.alert-light hr {
    border-top-color: #b4bece;
}

.alert-light .alert-link {
    color: #99a2b3;
}

.alert-dark {
    color: #2f3247;
    background-color: #404358;
    border-color: #303349;
}

.alert-dark hr {
    border-top-color: #26283a;
}

.alert-dark .alert-link {
    color: #1b1c28;
}

.alert-default {
    color: #262833;
    background-color: #363842;
    border-color: #262833;
}

.alert-default hr {
    border-top-color: #1b1d24;
}

.alert-default .alert-link {
    color: #101116;
}

.alert-white {
    color: #ccd0d4;
    background-color: #ecf0f3;
    border-color: #dce0e4;
}

.alert-white hr {
    border-top-color: #ced3d9;
}

.alert-white .alert-link {
    color: #b0b7bd;
}

.alert-gray {
    color: #3f4261;
    background-color: #515575;
    border-color: #424566;
}

.alert-gray hr {
    border-top-color: #383b57;
}

.alert-gray .alert-link {
    color: #2b2d42;
}

.alert-neutral {
    color: #ccd0d4;
    background-color: #ecf0f3;
    border-color: #dce0e4;
}

.alert-neutral hr {
    border-top-color: #ced3d9;
}

.alert-neutral .alert-link {
    color: #b0b7bd;
}

.alert-soft {
    color: #c7c8d0;
    background-color: #e6e8ee;
    border-color: #d7d8df;
}

.alert-soft hr {
    border-top-color: #c9cad4;
}

.alert-soft .alert-link {
    color: #abadb9;
}

.alert-black {
    color: #262833;
    background-color: #363842;
    border-color: #262833;
}

.alert-black hr {
    border-top-color: #1b1d24;
}

.alert-black .alert-link {
    color: #101116;
}

.alert-purple {
    color: #633eaa;
    background-color: #7950c5;
    border-color: #6940b6;
}

.alert-purple hr {
    border-top-color: #5e39a3;
}

.alert-purple .alert-link {
    color: #4d3085;
}

.alert-gray-100 {
    color: #d2d6da;
    background-color: #f2f6f9;
    border-color: #e3e6ea;
}

.alert-gray-100 hr {
    border-top-color: #d4d9df;
}

.alert-gray-100 .alert-link {
    color: #b6bdc3;
}

.alert-gray-200 {
    color: #d8d9de;
    background-color: #f9fafd;
    border-color: #e9eaee;
}

.alert-gray-200 hr {
    border-top-color: #dbdce3;
}

.alert-gray-200 .alert-link {
    color: #bcbec7;
}

.alert-gray-300 {
    color: #c7c8d0;
    background-color: #e6e8ee;
    border-color: #d7d8df;
}

.alert-gray-300 hr {
    border-top-color: #c9cad4;
}

.alert-gray-300 .alert-link {
    color: #abadb9;
}

.alert-gray-400 {
    color: #b6bdc9;
    background-color: #d3dbe7;
    border-color: #c3cbd8;
}

.alert-gray-400 hr {
    border-top-color: #b4bece;
}

.alert-gray-400 .alert-link {
    color: #99a2b3;
}

.alert-gray-500 {
    color: #9ba4b5;
    background-color: #b6c0d1;
    border-color: #a6b0c2;
}

.alert-gray-500 hr {
    border-top-color: #97a3b8;
}

.alert-gray-500 .alert-link {
    color: #7e899f;
}

.alert-gray-600 {
    color: #8291a8;
    background-color: #9aabc2;
    border-color: #8a9bb3;
}

.alert-gray-600 hr {
    border-top-color: #7b8ea9;
}

.alert-gray-600 .alert-link {
    color: #657792;
}

.alert-gray-700 {
    color: #5c6c8d;
    background-color: #7183a5;
    border-color: #617395;
}

.alert-gray-700 hr {
    border-top-color: #576786;
}

.alert-gray-700 .alert-link {
    color: #48546e;
}

.alert-gray-800 {
    color: #4b4d74;
    background-color: #5e6089;
    border-color: #4e507a;
}

.alert-gray-800 hr {
    border-top-color: #44466a;
}

.alert-gray-800 .alert-link {
    color: #373855;
}

.alert-facebook {
    color: #385189;
    background-color: #4965a0;
    border-color: #395591;
}

.alert-facebook hr {
    border-top-color: #324a7f;
}

.alert-facebook .alert-link {
    color: #293c65;
}

.alert-dribbble {
    color: #cb467b;
    background-color: #ea5991;
    border-color: #da4982;
}

.alert-dribbble hr {
    border-top-color: #d63473;
}

.alert-dribbble .alert-link {
    color: #ad3162;
}

.alert-github {
    color: #232325;
    background-color: #323233;
    border-color: #222223;
}

.alert-github hr {
    border-top-color: #151516;
}

.alert-github .alert-link {
    color: #0a0a0b;
}

.alert-behance {
    color: #064fde;
    background-color: #1363fe;
    border-color: #0353ef;
}

.alert-behance hr {
    border-top-color: #034ad6;
}

.alert-behance .alert-link {
    color: #053dac;
}

.alert-twitter {
    color: #1e8ed3;
    background-color: #2ea7f2;
    border-color: #1e97e3;
}

.alert-twitter hr {
    border-top-color: #1a88ce;
}

.alert-twitter .alert-link {
    color: #1870a6;
}

.alert-slack {
    color: #379978;
    background-color: #48b48e;
    border-color: #38a47e;
}

.alert-slack hr {
    border-top-color: #32916f;
}

.alert-slack .alert-link {
    color: #2a735b;
}

@keyframes progress-bar-stripes {
    from {
        background-position: 1rem 0;
    }

    to {
        background-position: 0 0;
    }
}

.progress {
    display: flex;
    height: 1rem;
    overflow: hidden;
    font-size: 0.75rem;
    background-color: #fafbfe;
    border-radius: 0.55rem;
    box-shadow: inset 0 0.1rem 0.1rem rgba(38, 40, 51, 0.1);
}

.progress-bar {
    display: flex;
    flex-direction: column;
    justify-content: center;
    color: #ECF0F3;
    text-align: center;
    white-space: nowrap;
    background-color: #e6e7ee;
    transition: width 0.6s ease;
}

@media (prefers-reduced-motion: reduce) {
    .progress-bar {
        transition: none;
    }
}

.progress-bar-striped {
    background-image: linear-gradient(45deg, rgba(236, 240, 243, 0.15) 25%, transparent 25%, transparent 50%, rgba(236, 240, 243, 0.15) 50%, rgba(236, 240, 243, 0.15) 75%, transparent 75%, transparent);
    background-size: 1rem 1rem;
}

.progress-bar-animated {
    animation: progress-bar-stripes 1s linear infinite;
}

@media (prefers-reduced-motion: reduce) {
    .progress-bar-animated {
        animation: none;
    }
}

.media {
    display: flex;
    align-items: flex-start;
}

.media-body {
    flex: 1;
}

.list-group {
    display: flex;
    flex-direction: column;
    padding-left: 0;
    margin-bottom: 0;
}

.list-group-item-action {
    width: 100%;
    color: #44476A;
    text-align: inherit;
}

.list-group-item-action:hover, .list-group-item-action:focus {
    z-index: 1;
    color: #44476A;
    text-decoration: none;
    background-color: #e6e7ee;
}

.list-group-item-action:active {
    color: #44476A;
    background-color: #fafbfe;
}

.list-group-item {
    position: relative;
    display: block;
    padding: 1rem 1rem;
    margin-bottom: -0.0625rem;
    background-color: transparent;
    border: 0.0625rem solid #D1D9E6;
}

.list-group-item:first-child {
    border-top-left-radius: 0.55rem;
    border-top-right-radius: 0.55rem;
}

.list-group-item:last-child {
    margin-bottom: 0;
    border-bottom-right-radius: 0.55rem;
    border-bottom-left-radius: 0.55rem;
}

.list-group-item.disabled, .list-group-item:disabled {
    color: #93a5be;
    pointer-events: none;
    background-color: transparent;
}

.list-group-item.active {
    z-index: 2;
    color: #44476A;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
}

.list-group-horizontal {
    flex-direction: row;
}

.list-group-horizontal .list-group-item {
    margin-right: -0.0625rem;
    margin-bottom: 0;
}

.list-group-horizontal .list-group-item:first-child {
    border-top-left-radius: 0.55rem;
    border-bottom-left-radius: 0.55rem;
    border-top-right-radius: 0;
}

.list-group-horizontal .list-group-item:last-child {
    margin-right: 0;
    border-top-right-radius: 0.55rem;
    border-bottom-right-radius: 0.55rem;
    border-bottom-left-radius: 0;
}

@media (min-width: 576px) {
    .list-group-horizontal-sm {
        flex-direction: row;
    }

    .list-group-horizontal-sm .list-group-item {
        margin-right: -0.0625rem;
        margin-bottom: 0;
    }

    .list-group-horizontal-sm .list-group-item:first-child {
        border-top-left-radius: 0.55rem;
        border-bottom-left-radius: 0.55rem;
        border-top-right-radius: 0;
    }

    .list-group-horizontal-sm .list-group-item:last-child {
        margin-right: 0;
        border-top-right-radius: 0.55rem;
        border-bottom-right-radius: 0.55rem;
        border-bottom-left-radius: 0;
    }
}

@media (min-width: 768px) {
    .list-group-horizontal-md {
        flex-direction: row;
    }

    .list-group-horizontal-md .list-group-item {
        margin-right: -0.0625rem;
        margin-bottom: 0;
    }

    .list-group-horizontal-md .list-group-item:first-child {
        border-top-left-radius: 0.55rem;
        border-bottom-left-radius: 0.55rem;
        border-top-right-radius: 0;
    }

    .list-group-horizontal-md .list-group-item:last-child {
        margin-right: 0;
        border-top-right-radius: 0.55rem;
        border-bottom-right-radius: 0.55rem;
        border-bottom-left-radius: 0;
    }
}

@media (min-width: 992px) {
    .list-group-horizontal-lg {
        flex-direction: row;
    }

    .list-group-horizontal-lg .list-group-item {
        margin-right: -0.0625rem;
        margin-bottom: 0;
    }

    .list-group-horizontal-lg .list-group-item:first-child {
        border-top-left-radius: 0.55rem;
        border-bottom-left-radius: 0.55rem;
        border-top-right-radius: 0;
    }

    .list-group-horizontal-lg .list-group-item:last-child {
        margin-right: 0;
        border-top-right-radius: 0.55rem;
        border-bottom-right-radius: 0.55rem;
        border-bottom-left-radius: 0;
    }
}

@media (min-width: 1200px) {
    .list-group-horizontal-xl {
        flex-direction: row;
    }

    .list-group-horizontal-xl .list-group-item {
        margin-right: -0.0625rem;
        margin-bottom: 0;
    }

    .list-group-horizontal-xl .list-group-item:first-child {
        border-top-left-radius: 0.55rem;
        border-bottom-left-radius: 0.55rem;
        border-top-right-radius: 0;
    }

    .list-group-horizontal-xl .list-group-item:last-child {
        margin-right: 0;
        border-top-right-radius: 0.55rem;
        border-bottom-right-radius: 0.55rem;
        border-bottom-left-radius: 0;
    }
}

.list-group-flush .list-group-item {
    border-right: 0;
    border-left: 0;
    border-radius: 0;
}

.list-group-flush .list-group-item:last-child {
    margin-bottom: -0.0625rem;
}

.list-group-flush:first-child .list-group-item:first-child {
    border-top: 0;
}

.list-group-flush:last-child .list-group-item:last-child {
    margin-bottom: 0;
    border-bottom: 0;
}

.list-group-item-primary {
    color: #8a8b94;
    background-color: #eaedf2;
}

.list-group-item-primary.list-group-item-action:hover, .list-group-item-primary.list-group-item-action:focus {
    color: #8a8b94;
    background-color: #dae0e8;
}

.list-group-item-primary.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #8a8b94;
    border-color: #8a8b94;
}

.list-group-item-secondary {
    color: #2a3b80;
    background-color: #b7c2e7;
}

.list-group-item-secondary.list-group-item-action:hover, .list-group-item-secondary.list-group-item-action:focus {
    color: #2a3b80;
    background-color: #a4b2e1;
}

.list-group-item-secondary.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #2a3b80;
    border-color: #2a3b80;
}

.list-group-item-success {
    color: #1f473f;
    background-color: #b1c9c4;
}

.list-group-item-success.list-group-item-action:hover, .list-group-item-success.list-group-item-action:focus {
    color: #1f473f;
    background-color: #a2bfb9;
}

.list-group-item-success.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #1f473f;
    border-color: #1f473f;
}

.list-group-item-info {
    color: #124076;
    background-color: #aac5e1;
}

.list-group-item-info.list-group-item-action:hover, .list-group-item-info.list-group-item-action:focus {
    color: #124076;
    background-color: #97b8da;
}

.list-group-item-info.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #124076;
    border-color: #124076;
}

.list-group-item-warning {
    color: #8f7118;
    background-color: #eddfaf;
}

.list-group-item-warning.list-group-item-action:hover, .list-group-item-warning.list-group-item-action:focus {
    color: #8f7118;
    background-color: #e8d79a;
}

.list-group-item-warning.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #8f7118;
    border-color: #8f7118;
}

.list-group-item-danger {
    color: #6a232f;
    background-color: #d9b5bb;
}

.list-group-item-danger.list-group-item-action:hover, .list-group-item-danger.list-group-item-action:focus {
    color: #6a232f;
    background-color: #d0a4ac;
}

.list-group-item-danger.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #6a232f;
    border-color: #6a232f;
}

.list-group-item-light {
    color: #7f8490;
    background-color: #e4eaef;
}

.list-group-item-light.list-group-item-action:hover, .list-group-item-light.list-group-item-action:focus {
    color: #7f8490;
    background-color: #d4dee6;
}

.list-group-item-light.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #7f8490;
    border-color: #7f8490;
}

.list-group-item-dark {
    color: #2c2e3f;
    background-color: #b8bbc4;
}

.list-group-item-dark.list-group-item-action:hover, .list-group-item-dark.list-group-item-action:focus {
    color: #2c2e3f;
    background-color: #aaaeb8;
}

.list-group-item-dark.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #2c2e3f;
    border-color: #2c2e3f;
}

.list-group-item-default {
    color: #262833;
    background-color: #b5b8bd;
}

.list-group-item-default.list-group-item-action:hover, .list-group-item-default.list-group-item-action:focus {
    color: #262833;
    background-color: #a8abb1;
}

.list-group-item-default.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #262833;
    border-color: #262833;
}

.list-group-item-white {
    color: #8d9097;
    background-color: #ecf0f3;
}

.list-group-item-white.list-group-item-action:hover, .list-group-item-white.list-group-item-action:focus {
    color: #8d9097;
    background-color: #dce4e9;
}

.list-group-item-white.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #8d9097;
    border-color: #8d9097;
}

.list-group-item-gray {
    color: #363850;
    background-color: #bdc1cd;
}

.list-group-item-gray.list-group-item-action:hover, .list-group-item-gray.list-group-item-action:focus {
    color: #363850;
    background-color: #aeb3c2;
}

.list-group-item-gray.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #363850;
    border-color: #363850;
}

.list-group-item-neutral {
    color: #8d9097;
    background-color: #ecf0f3;
}

.list-group-item-neutral.list-group-item-action:hover, .list-group-item-neutral.list-group-item-action:focus {
    color: #8d9097;
    background-color: #dce4e9;
}

.list-group-item-neutral.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #8d9097;
    border-color: #8d9097;
}

.list-group-item-soft {
    color: #8a8b94;
    background-color: #eaedf2;
}

.list-group-item-soft.list-group-item-action:hover, .list-group-item-soft.list-group-item-action:focus {
    color: #8a8b94;
    background-color: #dae0e8;
}

.list-group-item-soft.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #8a8b94;
    border-color: #8a8b94;
}

.list-group-item-black {
    color: #262833;
    background-color: #b5b8bd;
}

.list-group-item-black.list-group-item-action:hover, .list-group-item-black.list-group-item-action:focus {
    color: #262833;
    background-color: #a8abb1;
}

.list-group-item-black.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #262833;
    border-color: #262833;
}

.list-group-item-purple {
    color: #4c367d;
    background-color: #c9bfe5;
}

.list-group-item-purple.list-group-item-action:hover, .list-group-item-purple.list-group-item-action:focus {
    color: #4c367d;
    background-color: #baadde;
}

.list-group-item-purple.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #4c367d;
    border-color: #4c367d;
}

.list-group-item-gray-100 {
    color: #91949a;
    background-color: #eef2f5;
}

.list-group-item-gray-100.list-group-item-action:hover, .list-group-item-gray-100.list-group-item-action:focus {
    color: #91949a;
    background-color: #dee6ec;
}

.list-group-item-gray-100.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #91949a;
    border-color: #91949a;
}

.list-group-item-gray-200 {
    color: #94969d;
    background-color: #f0f3f6;
}

.list-group-item-gray-200.list-group-item-action:hover, .list-group-item-gray-200.list-group-item-action:focus {
    color: #94969d;
    background-color: #e0e6ec;
}

.list-group-item-gray-200.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #94969d;
    border-color: #94969d;
}

.list-group-item-gray-300 {
    color: #8a8b94;
    background-color: #eaedf2;
}

.list-group-item-gray-300.list-group-item-action:hover, .list-group-item-gray-300.list-group-item-action:focus {
    color: #8a8b94;
    background-color: #dae0e8;
}

.list-group-item-gray-300.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #8a8b94;
    border-color: #8a8b94;
}

.list-group-item-gray-400 {
    color: #7f8490;
    background-color: #e4eaef;
}

.list-group-item-gray-400.list-group-item-action:hover, .list-group-item-gray-400.list-group-item-action:focus {
    color: #7f8490;
    background-color: #d4dee6;
}

.list-group-item-gray-400.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #7f8490;
    border-color: #7f8490;
}

.list-group-item-gray-500 {
    color: #6e7584;
    background-color: #dbe1e9;
}

.list-group-item-gray-500.list-group-item-action:hover, .list-group-item-gray-500.list-group-item-action:focus {
    color: #6e7584;
    background-color: #cbd4df;
}

.list-group-item-gray-500.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #6e7584;
    border-color: #6e7584;
}

.list-group-item-gray-600 {
    color: #5f697b;
    background-color: #d3dbe4;
}

.list-group-item-gray-600.list-group-item-action:hover, .list-group-item-gray-600.list-group-item-action:focus {
    color: #5f697b;
    background-color: #c3ceda;
}

.list-group-item-gray-600.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #5f697b;
    border-color: #5f697b;
}

.list-group-item-gray-700 {
    color: #47526b;
    background-color: #c6cfdb;
}

.list-group-item-gray-700.list-group-item-action:hover, .list-group-item-gray-700.list-group-item-action:focus {
    color: #47526b;
    background-color: #b6c2d1;
}

.list-group-item-gray-700.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #47526b;
    border-color: #47526b;
}

.list-group-item-gray-800 {
    color: #3d3f5b;
    background-color: #c1c4d3;
}

.list-group-item-gray-800.list-group-item-action:hover, .list-group-item-gray-800.list-group-item-action:focus {
    color: #3d3f5b;
    background-color: #b2b6c8;
}

.list-group-item-gray-800.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #3d3f5b;
    border-color: #3d3f5b;
}

.list-group-item-facebook {
    color: #314168;
    background-color: #bac6da;
}

.list-group-item-facebook.list-group-item-action:hover, .list-group-item-facebook.list-group-item-action:focus {
    color: #314168;
    background-color: #a9b8d1;
}

.list-group-item-facebook.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #314168;
    border-color: #314168;
}

.list-group-item-dribbble {
    color: #8c3b60;
    background-color: #ebc2d5;
}

.list-group-item-dribbble.list-group-item-action:hover, .list-group-item-dribbble.list-group-item-action:focus {
    color: #8c3b60;
    background-color: #e5afc8;
}

.list-group-item-dribbble.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #8c3b60;
    border-color: #8c3b60;
}

.list-group-item-github {
    color: #24252a;
    background-color: #b3b6b8;
}

.list-group-item-github.list-group-item-action:hover, .list-group-item-github.list-group-item-action:focus {
    color: #24252a;
    background-color: #a6a9ac;
}

.list-group-item-github.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #24252a;
    border-color: #24252a;
}

.list-group-item-behance {
    color: #12409d;
    background-color: #aac5f6;
}

.list-group-item-behance.list-group-item-action:hover, .list-group-item-behance.list-group-item-action:focus {
    color: #12409d;
    background-color: #93b5f4;
}

.list-group-item-behance.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #12409d;
    border-color: #12409d;
}

.list-group-item-twitter {
    color: #216796;
    background-color: #b2daf3;
}

.list-group-item-twitter.list-group-item-action:hover, .list-group-item-twitter.list-group-item-action:focus {
    color: #216796;
    background-color: #9ccff0;
}

.list-group-item-twitter.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #216796;
    border-color: #216796;
}

.list-group-item-slack {
    color: #306e5e;
    background-color: #baded4;
}

.list-group-item-slack.list-group-item-action:hover, .list-group-item-slack.list-group-item-action:focus {
    color: #306e5e;
    background-color: #a9d6c9;
}

.list-group-item-slack.list-group-item-action.active {
    color: #ECF0F3;
    background-color: #306e5e;
    border-color: #306e5e;
}

.close {
    float: right;
    font-size: 1.5rem;
    font-weight: 600;
    line-height: 1;
    color: rgba(0, 0, 0, 0.6);
    text-shadow: none;
    opacity: .5;
}

@media (max-width: 1200px) {
    .close {
        font-size: calc(1.275rem + 0.3vw);
    }
}

.close:hover {
    color: rgba(0, 0, 0, 0.6);
    text-decoration: none;
}

.close:not(:disabled):not(.disabled):hover, .close:not(:disabled):not(.disabled):focus {
    opacity: .75;
}

button.close {
    padding: 0;
    background-color: transparent;
    border: 0;
    -webkit-appearance: none;
    appearance: none;
}

a.close.disabled {
    pointer-events: none;
}

.toast {
    max-width: 350px;
    overflow: hidden;
    font-size: 1rem;
    background-color: #e6e7ee;
    background-clip: padding-box;
    border: 1px solid #D1D9E6;
    box-shadow: 3px 3px 6px #b8b9be, -3px -3px 6px #ffffff;
    -webkit-backdrop-filter: blur(10px);
    backdrop-filter: blur(10px);
    opacity: 0;
    border-radius: 0.55rem;
}

.toast:not(:last-child) {
    margin-bottom: 0.75rem;
}

.toast.showing {
    opacity: 1;
}

.toast.show {
    display: block;
    opacity: 1;
}

.toast.hide {
    display: none;
}

.toast-header {
    display: flex;
    align-items: center;
    padding: 0.25rem 0.75rem;
    color: #31344b;
    background-color: rgba(230, 231, 238, 0.85);
    background-clip: padding-box;
    border-bottom: 1px solid #D1D9E6;
}

.toast-body {
    padding: 0.75rem;
}

.modal-open {
    overflow: hidden;
}

.modal-open .modal {
    overflow-x: hidden;
    overflow-y: auto;
}

.modal {
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1050;
    display: none;
    width: 100%;
    height: 100%;
    overflow: hidden;
    outline: 0;
}

.modal-dialog {
    position: relative;
    width: auto;
    margin: 0.5rem;
    pointer-events: none;
}

.modal.fade .modal-dialog {
    transition: transform 0.3s ease-out;
    transform: translate(0, -50px);
}

@media (prefers-reduced-motion: reduce) {
    .modal.fade .modal-dialog {
        transition: none;
    }
}

.modal.show .modal-dialog {
    transform: none;
}

.modal-dialog-scrollable {
    display: flex;
    max-height: calc(100% - 1rem);
}

.modal-dialog-scrollable .modal-content {
    max-height: calc(100vh - 1rem);
    overflow: hidden;
}

.modal-dialog-scrollable .modal-header,
  .modal-dialog-scrollable .modal-footer {
    flex-shrink: 0;
}

.modal-dialog-scrollable .modal-body {
    overflow-y: auto;
}

.modal-dialog-centered {
    display: flex;
    align-items: center;
    min-height: calc(100% - 1rem);
}

.modal-dialog-centered::before {
    display: block;
    height: calc(100vh - 1rem);
    content: "";
}

.modal-dialog-centered.modal-dialog-scrollable {
    flex-direction: column;
    justify-content: center;
    height: 100%;
}

.modal-dialog-centered.modal-dialog-scrollable .modal-content {
    max-height: none;
}

.modal-dialog-centered.modal-dialog-scrollable::before {
    content: none;
}

.modal-content {
    position: relative;
    display: flex;
    flex-direction: column;
    width: 100%;
    pointer-events: auto;
    background-color: #e6e7ee;
    background-clip: padding-box;
    border: 1px solid #D1D9E6;
    border-radius: 0.3rem;
    box-shadow: 0 0.25rem 0.5rem rgba(38, 40, 51, 0.5);
    outline: 0;
}

.modal-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1040;
    width: 100vw;
    height: 100vh;
    background-color: #e6e7ee;
}

.modal-backdrop.fade {
    opacity: 0;
}

.modal-backdrop.show {
    opacity: 0.9;
}

.modal-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    padding: 1.25rem;
    border-bottom: 1px solid #D1D9E6;
    border-top-left-radius: 0.3rem;
    border-top-right-radius: 0.3rem;
}

.modal-header .close {
    padding: 1.25rem;
    margin: -1rem -1rem -1rem auto;
}

.modal-title {
    margin-bottom: 0;
    line-height: 1.8;
}

.modal-body {
    position: relative;
    flex: 1 1 auto;
    padding: 1.5rem;
}

.modal-footer {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    padding: 1.5rem;
    border-top: 1px solid #D1D9E6;
    border-bottom-right-radius: 0.3rem;
    border-bottom-left-radius: 0.3rem;
}

.modal-footer > :not(:first-child) {
    margin-left: .25rem;
}

.modal-footer > :not(:last-child) {
    margin-right: .25rem;
}

.modal-scrollbar-measure {
    position: absolute;
    top: -9999px;
    width: 50px;
    height: 50px;
    overflow: scroll;
}

@media (min-width: 576px) {
    .modal-dialog {
        max-width: 500px;
        margin: 1.75rem auto;
    }

    .modal-dialog-scrollable {
        max-height: calc(100% - 3.5rem);
    }

    .modal-dialog-scrollable .modal-content {
        max-height: calc(100vh - 3.5rem);
    }

    .modal-dialog-centered {
        min-height: calc(100% - 3.5rem);
    }

    .modal-dialog-centered::before {
        height: calc(100vh - 3.5rem);
    }

    .modal-content {
        box-shadow: 0 0.5rem 1rem rgba(38, 40, 51, 0.5);
    }

    .modal-sm {
        max-width: 380px;
    }
}

@media (min-width: 992px) {
    .modal-lg,
  .modal-xl {
        max-width: 800px;
    }
}

@media (min-width: 1200px) {
    .modal-xl {
        max-width: 1140px;
    }
}

.tooltip {
    position: absolute;
    z-index: 1070;
    display: block;
    margin: 0;
    font-family: "Nunito Sans", sans-serif;
    font-style: normal;
    font-weight: 400;
    line-height: 1.5;
    text-align: left;
    text-align: start;
    text-decoration: none;
    text-shadow: none;
    text-transform: none;
    letter-spacing: normal;
    word-break: normal;
    word-spacing: normal;
    white-space: normal;
    line-break: auto;
    font-size: 0.875rem;
    word-wrap: break-word;
    opacity: 0;
}

.tooltip.show {
    opacity: 0.9;
}

.tooltip .arrow {
    position: absolute;
    display: block;
    width: 0.8rem;
    height: 0.4rem;
}

.tooltip .arrow::before {
    position: absolute;
    content: "";
    border-color: transparent;
    border-style: solid;
}

.bs-tooltip-top, .bs-tooltip-auto[x-placement^="top"] {
    padding: 0.4rem 0;
}

.bs-tooltip-top .arrow, .bs-tooltip-auto[x-placement^="top"] .arrow {
    bottom: 0;
}

.bs-tooltip-top .arrow::before, .bs-tooltip-auto[x-placement^="top"] .arrow::before {
    top: 0;
    border-width: 0.4rem 0.4rem 0;
    border-top-color: #ECF0F3;
}

.bs-tooltip-right, .bs-tooltip-auto[x-placement^="right"] {
    padding: 0 0.4rem;
}

.bs-tooltip-right .arrow, .bs-tooltip-auto[x-placement^="right"] .arrow {
    left: 0;
    width: 0.4rem;
    height: 0.8rem;
}

.bs-tooltip-right .arrow::before, .bs-tooltip-auto[x-placement^="right"] .arrow::before {
    right: 0;
    border-width: 0.4rem 0.4rem 0.4rem 0;
    border-right-color: #ECF0F3;
}

.bs-tooltip-bottom, .bs-tooltip-auto[x-placement^="bottom"] {
    padding: 0.4rem 0;
}

.bs-tooltip-bottom .arrow, .bs-tooltip-auto[x-placement^="bottom"] .arrow {
    top: 0;
}

.bs-tooltip-bottom .arrow::before, .bs-tooltip-auto[x-placement^="bottom"] .arrow::before {
    bottom: 0;
    border-width: 0 0.4rem 0.4rem;
    border-bottom-color: #ECF0F3;
}

.bs-tooltip-left, .bs-tooltip-auto[x-placement^="left"] {
    padding: 0 0.4rem;
}

.bs-tooltip-left .arrow, .bs-tooltip-auto[x-placement^="left"] .arrow {
    right: 0;
    width: 0.4rem;
    height: 0.8rem;
}

.bs-tooltip-left .arrow::before, .bs-tooltip-auto[x-placement^="left"] .arrow::before {
    left: 0;
    border-width: 0.4rem 0 0.4rem 0.4rem;
    border-left-color: #ECF0F3;
}

.tooltip-inner {
    max-width: 200px;
    padding: 0.25rem 0.5rem;
    color: #262833;
    text-align: center;
    background-color: #ECF0F3;
    border-radius: 0.55rem;
}

.popover {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 1060;
    display: block;
    max-width: 276px;
    font-family: "Nunito Sans", sans-serif;
    font-style: normal;
    font-weight: 400;
    line-height: 1.5;
    text-align: left;
    text-align: start;
    text-decoration: none;
    text-shadow: none;
    text-transform: none;
    letter-spacing: normal;
    word-break: normal;
    word-spacing: normal;
    white-space: normal;
    line-break: auto;
    font-size: 0.875rem;
    word-wrap: break-word;
    background-color: #e6e7ee;
    background-clip: padding-box;
    border: 1px solid #D1D9E6;
    border-radius: 0.3rem;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.popover .arrow {
    position: absolute;
    display: block;
    width: 1.5rem;
    height: 0.75rem;
    margin: 0 0.3rem;
}

.popover .arrow::before, .popover .arrow::after {
    position: absolute;
    display: block;
    content: "";
    border-color: transparent;
    border-style: solid;
}

.bs-popover-top, .bs-popover-auto[x-placement^="top"] {
    margin-bottom: 0.75rem;
}

.bs-popover-top > .arrow, .bs-popover-auto[x-placement^="top"] > .arrow {
    bottom: calc((0.75rem + 1px) * -1);
}

.bs-popover-top > .arrow::before, .bs-popover-auto[x-placement^="top"] > .arrow::before {
    bottom: 0;
    border-width: 0.75rem 0.75rem 0;
    border-top-color: transparent;
}

.bs-popover-top > .arrow::after, .bs-popover-auto[x-placement^="top"] > .arrow::after {
    bottom: 1px;
    border-width: 0.75rem 0.75rem 0;
    border-top-color: #D1D9E6;
}

.bs-popover-right, .bs-popover-auto[x-placement^="right"] {
    margin-left: 0.75rem;
}

.bs-popover-right > .arrow, .bs-popover-auto[x-placement^="right"] > .arrow {
    left: calc((0.75rem + 1px) * -1);
    width: 0.75rem;
    height: 1.5rem;
    margin: 0.3rem 0;
}

.bs-popover-right > .arrow::before, .bs-popover-auto[x-placement^="right"] > .arrow::before {
    left: 0;
    border-width: 0.75rem 0.75rem 0.75rem 0;
    border-right-color: transparent;
}

.bs-popover-right > .arrow::after, .bs-popover-auto[x-placement^="right"] > .arrow::after {
    left: 1px;
    border-width: 0.75rem 0.75rem 0.75rem 0;
    border-right-color: #D1D9E6;
}

.bs-popover-bottom, .bs-popover-auto[x-placement^="bottom"] {
    margin-top: 0.75rem;
}

.bs-popover-bottom > .arrow, .bs-popover-auto[x-placement^="bottom"] > .arrow {
    top: calc((0.75rem + 1px) * -1);
}

.bs-popover-bottom > .arrow::before, .bs-popover-auto[x-placement^="bottom"] > .arrow::before {
    top: 0;
    border-width: 0 0.75rem 0.75rem 0.75rem;
    border-bottom-color: transparent;
}

.bs-popover-bottom > .arrow::after, .bs-popover-auto[x-placement^="bottom"] > .arrow::after {
    top: 1px;
    border-width: 0 0.75rem 0.75rem 0.75rem;
    border-bottom-color: #D1D9E6;
}

.bs-popover-bottom .popover-header::before, .bs-popover-auto[x-placement^="bottom"] .popover-header::before {
    position: absolute;
    top: 0;
    left: 50%;
    display: block;
    width: 1.5rem;
    margin-left: -0.75rem;
    content: "";
    border-bottom: 1px solid #e6e7ee;
}

.bs-popover-left, .bs-popover-auto[x-placement^="left"] {
    margin-right: 0.75rem;
}

.bs-popover-left > .arrow, .bs-popover-auto[x-placement^="left"] > .arrow {
    right: calc((0.75rem + 1px) * -1);
    width: 0.75rem;
    height: 1.5rem;
    margin: 0.3rem 0;
}

.bs-popover-left > .arrow::before, .bs-popover-auto[x-placement^="left"] > .arrow::before {
    right: 0;
    border-width: 0.75rem 0 0.75rem 0.75rem;
    border-left-color: transparent;
}

.bs-popover-left > .arrow::after, .bs-popover-auto[x-placement^="left"] > .arrow::after {
    right: 1px;
    border-width: 0.75rem 0 0.75rem 0.75rem;
    border-left-color: #D1D9E6;
}

.popover-header {
    padding: 0.75rem 0.75rem;
    margin-bottom: 0;
    font-size: 1rem;
    color: #31344b;
    background-color: #e6e7ee;
    border-bottom: 1px solid #d7d8e4;
    border-top-left-radius: calc(0.3rem - 1px);
    border-top-right-radius: calc(0.3rem - 1px);
}

.popover-header:empty {
    display: none;
}

.popover-body {
    padding: 0.75rem 0.75rem;
    color: #44476A;
}

.carousel {
    position: relative;
}

.carousel.pointer-event {
    touch-action: pan-y;
}

.carousel-inner {
    position: relative;
    width: 100%;
    overflow: hidden;
}

.carousel-inner::after {
    display: block;
    clear: both;
    content: "";
}

.carousel-item {
    position: relative;
    display: none;
    float: left;
    width: 100%;
    margin-right: -100%;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    transition: transform 0.6s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
    .carousel-item {
        transition: none;
    }
}

.carousel-item.active,
.carousel-item-next,
.carousel-item-prev {
    display: block;
}

.carousel-item-next:not(.carousel-item-left),
.active.carousel-item-right {
    transform: translateX(100%);
}

.carousel-item-prev:not(.carousel-item-right),
.active.carousel-item-left {
    transform: translateX(-100%);
}

.carousel-fade .carousel-item {
    opacity: 0;
    transition-property: opacity;
    transform: none;
}

.carousel-fade .carousel-item.active,
.carousel-fade .carousel-item-next.carousel-item-left,
.carousel-fade .carousel-item-prev.carousel-item-right {
    z-index: 1;
    opacity: 1;
}

.carousel-fade .active.carousel-item-left,
.carousel-fade .active.carousel-item-right {
    z-index: 0;
    opacity: 0;
    transition: 0s 0.6s opacity;
}

@media (prefers-reduced-motion: reduce) {
    .carousel-fade .active.carousel-item-left,
    .carousel-fade .active.carousel-item-right {
        transition: none;
    }
}

.carousel-control-prev,
.carousel-control-next {
    position: absolute;
    top: 0;
    bottom: 0;
    z-index: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 15%;
    color: #ECF0F3;
    text-align: center;
    opacity: 0.5;
    transition: opacity 0.15s ease;
}

@media (prefers-reduced-motion: reduce) {
    .carousel-control-prev,
    .carousel-control-next {
        transition: none;
    }
}

.carousel-control-prev:hover, .carousel-control-prev:focus,
  .carousel-control-next:hover,
  .carousel-control-next:focus {
    color: #ECF0F3;
    text-decoration: none;
    outline: 0;
    opacity: 0.9;
}

.carousel-control-prev {
    left: 0;
}

.carousel-control-next {
    right: 0;
}

.carousel-control-prev-icon,
.carousel-control-next-icon {
    display: inline-block;
    width: 20px;
    height: 20px;
    background: no-repeat 50% / 100% 100%;
}

.carousel-control-prev-icon {
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='%23ECF0F3' viewBox='0 0 8 8'%3e%3cpath d='M5.25 0l-4 4 4 4 1.5-1.5-2.5-2.5 2.5-2.5-1.5-1.5z'/%3e%3c/svg%3e");
}

.carousel-control-next-icon {
    background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' fill='%23ECF0F3' viewBox='0 0 8 8'%3e%3cpath d='M2.75 0l-1.5 1.5 2.5 2.5-2.5 2.5 1.5 1.5 4-4-4-4z'/%3e%3c/svg%3e");
}

.carousel-indicators {
    position: absolute;
    right: 0;
    bottom: 0px;
    left: 0;
    z-index: 15;
    display: flex;
    justify-content: center;
    padding-left: 0;
    margin-right: 15%;
    margin-left: 15%;
    list-style: none;
}

.carousel-indicators li {
    box-sizing: content-box;
    flex: 0 1 auto;
    width: 30px;
    height: 3px;
    margin-right: 3px;
    margin-left: 3px;
    text-indent: -999px;
    cursor: pointer;
    background-color: #ECF0F3;
    background-clip: padding-box;
    border-top: 10px solid transparent;
    border-bottom: 10px solid transparent;
    opacity: .5;
    transition: opacity 0.6s ease;
}

@media (prefers-reduced-motion: reduce) {
    .carousel-indicators li {
        transition: none;
    }
}

.carousel-indicators .active {
    opacity: 1;
}

.carousel-caption {
    position: absolute;
    right: 15%;
    bottom: 20px;
    left: 15%;
    z-index: 10;
    padding-top: 20px;
    padding-bottom: 20px;
    color: #ECF0F3;
    text-align: center;
}

@keyframes spinner-border {
    to {
        transform: rotate(360deg);
    }
}

.spinner-border {
    display: inline-block;
    width: 2rem;
    height: 2rem;
    vertical-align: text-bottom;
    border: 0.25em solid currentColor;
    border-right-color: transparent;
    border-radius: 50%;
    animation: spinner-border .75s linear infinite;
}

.spinner-border-sm {
    width: 1rem;
    height: 1rem;
    border-width: 0.2em;
}

@keyframes spinner-grow {
    0% {
        transform: scale(0);
    }

    50% {
        opacity: 1;
    }
}

.spinner-grow {
    display: inline-block;
    width: 2rem;
    height: 2rem;
    vertical-align: text-bottom;
    background-color: currentColor;
    border-radius: 50%;
    opacity: 0;
    animation: spinner-grow .75s linear infinite;
}

.spinner-grow-sm {
    width: 1rem;
    height: 1rem;
}

.align-baseline {
    vertical-align: baseline !important;
}

.align-top {
    vertical-align: top !important;
}

.align-middle {
    vertical-align: middle !important;
}

.align-bottom {
    vertical-align: bottom !important;
}

.align-text-bottom {
    vertical-align: text-bottom !important;
}

.align-text-top {
    vertical-align: text-top !important;
}

.bg-primary {
    background-color: #e6e7ee !important;
}

a.bg-primary:hover, a.bg-primary:focus,
button.bg-primary:hover,
button.bg-primary:focus {
    background-color: #c8cad9 !important;
}

.bg-secondary {
    background-color: #2D4CC8 !important;
}

a.bg-secondary:hover, a.bg-secondary:focus,
button.bg-secondary:hover,
button.bg-secondary:focus {
    background-color: #243c9e !important;
}

.bg-success {
    background-color: #18634B !important;
}

a.bg-success:hover, a.bg-success:focus,
button.bg-success:hover,
button.bg-success:focus {
    background-color: #0e3a2c !important;
}

.bg-info {
    background-color: #0056B3 !important;
}

a.bg-info:hover, a.bg-info:focus,
button.bg-info:hover,
button.bg-info:focus {
    background-color: #003d80 !important;
}

.bg-warning {
    background-color: #F0B400 !important;
}

a.bg-warning:hover, a.bg-warning:focus,
button.bg-warning:hover,
button.bg-warning:focus {
    background-color: #bd8e00 !important;
}

.bg-danger {
    background-color: #A91E2C !important;
}

a.bg-danger:hover, a.bg-danger:focus,
button.bg-danger:hover,
button.bg-danger:focus {
    background-color: #7e1621 !important;
}

.bg-light {
    background-color: #D1D9E6 !important;
}

a.bg-light:hover, a.bg-light:focus,
button.bg-light:hover,
button.bg-light:focus {
    background-color: #b0bed4 !important;
}

.bg-dark {
    background-color: #31344b !important;
}

a.bg-dark:hover, a.bg-dark:focus,
button.bg-dark:hover,
button.bg-dark:focus {
    background-color: #1d1f2c !important;
}

.bg-default {
    background-color: #262833 !important;
}

a.bg-default:hover, a.bg-default:focus,
button.bg-default:hover,
button.bg-default:focus {
    background-color: #101116 !important;
}

.bg-white {
    background-color: #ECF0F3 !important;
}

a.bg-white:hover, a.bg-white:focus,
button.bg-white:hover,
button.bg-white:focus {
    background-color: #cdd7df !important;
}

.bg-gray {
    background-color: #44476A !important;
}

a.bg-gray:hover, a.bg-gray:focus,
button.bg-gray:hover,
button.bg-gray:focus {
    background-color: #30324b !important;
}

.bg-neutral {
    background-color: #ECF0F3 !important;
}

a.bg-neutral:hover, a.bg-neutral:focus,
button.bg-neutral:hover,
button.bg-neutral:focus {
    background-color: #cdd7df !important;
}

.bg-soft {
    background-color: #e6e7ee !important;
}

a.bg-soft:hover, a.bg-soft:focus,
button.bg-soft:hover,
button.bg-soft:focus {
    background-color: #c8cad9 !important;
}

.bg-black {
    background-color: #262833 !important;
}

a.bg-black:hover, a.bg-black:focus,
button.bg-black:hover,
button.bg-black:focus {
    background-color: #101116 !important;
}

.bg-purple {
    background-color: #6f42c1 !important;
}

a.bg-purple:hover, a.bg-purple:focus,
button.bg-purple:hover,
button.bg-purple:focus {
    background-color: #59339d !important;
}

.bg-gray-100 {
    background-color: #f3f7fa !important;
}

a.bg-gray-100:hover, a.bg-gray-100:focus,
button.bg-gray-100:hover,
button.bg-gray-100:focus {
    background-color: #cfdfeb !important;
}

.bg-gray-200 {
    background-color: #fafbfe !important;
}

a.bg-gray-200:hover, a.bg-gray-200:focus,
button.bg-gray-200:hover,
button.bg-gray-200:focus {
    background-color: #d0d9f6 !important;
}

.bg-gray-300 {
    background-color: #e6e7ee !important;
}

a.bg-gray-300:hover, a.bg-gray-300:focus,
button.bg-gray-300:hover,
button.bg-gray-300:focus {
    background-color: #c8cad9 !important;
}

.bg-gray-400 {
    background-color: #D1D9E6 !important;
}

a.bg-gray-400:hover, a.bg-gray-400:focus,
button.bg-gray-400:hover,
button.bg-gray-400:focus {
    background-color: #b0bed4 !important;
}

.bg-gray-500 {
    background-color: #b1bcce !important;
}

a.bg-gray-500:hover, a.bg-gray-500:focus,
button.bg-gray-500:hover,
button.bg-gray-500:focus {
    background-color: #92a1ba !important;
}

.bg-gray-600 {
    background-color: #93a5be !important;
}

a.bg-gray-600:hover, a.bg-gray-600:focus,
button.bg-gray-600:hover,
button.bg-gray-600:focus {
    background-color: #738aab !important;
}

.bg-gray-700 {
    background-color: #66799e !important;
}

a.bg-gray-700:hover, a.bg-gray-700:focus,
button.bg-gray-700:hover,
button.bg-gray-700:focus {
    background-color: #516180 !important;
}

.bg-gray-800 {
    background-color: #525480 !important;
}

a.bg-gray-800:hover, a.bg-gray-800:focus,
button.bg-gray-800:hover,
button.bg-gray-800:focus {
    background-color: #3e4061 !important;
}

.bg-facebook {
    background-color: #3b5999 !important;
}

a.bg-facebook:hover, a.bg-facebook:focus,
button.bg-facebook:hover,
button.bg-facebook:focus {
    background-color: #2d4474 !important;
}

.bg-dribbble {
    background-color: #ea4c89 !important;
}

a.bg-dribbble:hover, a.bg-dribbble:focus,
button.bg-dribbble:hover,
button.bg-dribbble:focus {
    background-color: #e51e6b !important;
}

.bg-github {
    background-color: #222222 !important;
}

a.bg-github:hover, a.bg-github:focus,
button.bg-github:hover,
button.bg-github:focus {
    background-color: #090909 !important;
}

.bg-behance {
    background-color: #0057ff !important;
}

a.bg-behance:hover, a.bg-behance:focus,
button.bg-behance:hover,
button.bg-behance:focus {
    background-color: #0046cc !important;
}

.bg-twitter {
    background-color: #1da1f2 !important;
}

a.bg-twitter:hover, a.bg-twitter:focus,
button.bg-twitter:hover,
button.bg-twitter:focus {
    background-color: #0c85d0 !important;
}

.bg-slack {
    background-color: #3aaf85 !important;
}

a.bg-slack:hover, a.bg-slack:focus,
button.bg-slack:hover,
button.bg-slack:focus {
    background-color: #2d8968 !important;
}

.bg-white {
    background-color: #ECF0F3 !important;
}

.bg-transparent {
    background-color: transparent !important;
}

.border {
    border: 0.0625rem solid #fafbfe !important;
}

.border-top {
    border-top: 0.0625rem solid #fafbfe !important;
}

.border-right {
    border-right: 0.0625rem solid #fafbfe !important;
}

.border-bottom {
    border-bottom: 0.0625rem solid #fafbfe !important;
}

.border-left {
    border-left: 0.0625rem solid #fafbfe !important;
}

.border-0 {
    border: 0 !important;
}

.border-top-0 {
    border-top: 0 !important;
}

.border-right-0 {
    border-right: 0 !important;
}

.border-bottom-0 {
    border-bottom: 0 !important;
}

.border-left-0 {
    border-left: 0 !important;
}

.border-primary {
    border-color: #e6e7ee !important;
}

.border-secondary {
    border-color: #2D4CC8 !important;
}

.border-success {
    border-color: #18634B !important;
}

.border-info {
    border-color: #0056B3 !important;
}

.border-warning {
    border-color: #F0B400 !important;
}

.border-danger {
    border-color: #A91E2C !important;
}

.border-light {
    border-color: #D1D9E6 !important;
}

.border-dark {
    border-color: #31344b !important;
}

.border-default {
    border-color: #262833 !important;
}

.border-white {
    border-color: #ECF0F3 !important;
}

.border-gray {
    border-color: #44476A !important;
}

.border-neutral {
    border-color: #ECF0F3 !important;
}

.border-soft {
    border-color: #e6e7ee !important;
}

.border-black {
    border-color: #262833 !important;
}

.border-purple {
    border-color: #6f42c1 !important;
}

.border-gray-100 {
    border-color: #f3f7fa !important;
}

.border-gray-200 {
    border-color: #fafbfe !important;
}

.border-gray-300 {
    border-color: #e6e7ee !important;
}

.border-gray-400 {
    border-color: #D1D9E6 !important;
}

.border-gray-500 {
    border-color: #b1bcce !important;
}

.border-gray-600 {
    border-color: #93a5be !important;
}

.border-gray-700 {
    border-color: #66799e !important;
}

.border-gray-800 {
    border-color: #525480 !important;
}

.border-facebook {
    border-color: #3b5999 !important;
}

.border-dribbble {
    border-color: #ea4c89 !important;
}

.border-github {
    border-color: #222222 !important;
}

.border-behance {
    border-color: #0057ff !important;
}

.border-twitter {
    border-color: #1da1f2 !important;
}

.border-slack {
    border-color: #3aaf85 !important;
}

.border-white {
    border-color: #ECF0F3 !important;
}

.rounded-sm {
    border-radius: 0.1rem !important;
}

.rounded {
    border-radius: 0.55rem !important;
}

.rounded-top {
    border-top-left-radius: 0.55rem !important;
    border-top-right-radius: 0.55rem !important;
}

.rounded-right {
    border-top-right-radius: 0.55rem !important;
    border-bottom-right-radius: 0.55rem !important;
}

.rounded-bottom {
    border-bottom-right-radius: 0.55rem !important;
    border-bottom-left-radius: 0.55rem !important;
}

.rounded-left {
    border-top-left-radius: 0.55rem !important;
    border-bottom-left-radius: 0.55rem !important;
}

.rounded-lg {
    border-radius: 0.3rem !important;
}

.rounded-circle {
    border-radius: 50% !important;
}

.rounded-pill {
    border-radius: 50rem !important;
}

.rounded-0 {
    border-radius: 0 !important;
}

.clearfix::after {
    display: block;
    clear: both;
    content: "";
}

.d-none {
    display: none !important;
}

.d-inline {
    display: inline !important;
}

.d-inline-block {
    display: inline-block !important;
}

.d-block {
    display: block !important;
}

.d-table {
    display: table !important;
}

.d-table-row {
    display: table-row !important;
}

.d-table-cell {
    display: table-cell !important;
}

.d-flex {
    display: flex !important;
}

.d-inline-flex {
    display: inline-flex !important;
}

@media (min-width: 576px) {
    .d-sm-none {
        display: none !important;
    }

    .d-sm-inline {
        display: inline !important;
    }

    .d-sm-inline-block {
        display: inline-block !important;
    }

    .d-sm-block {
        display: block !important;
    }

    .d-sm-table {
        display: table !important;
    }

    .d-sm-table-row {
        display: table-row !important;
    }

    .d-sm-table-cell {
        display: table-cell !important;
    }

    .d-sm-flex {
        display: flex !important;
    }

    .d-sm-inline-flex {
        display: inline-flex !important;
    }
}

@media (min-width: 768px) {
    .d-md-none {
        display: none !important;
    }

    .d-md-inline {
        display: inline !important;
    }

    .d-md-inline-block {
        display: inline-block !important;
    }

    .d-md-block {
        display: block !important;
    }

    .d-md-table {
        display: table !important;
    }

    .d-md-table-row {
        display: table-row !important;
    }

    .d-md-table-cell {
        display: table-cell !important;
    }

    .d-md-flex {
        display: flex !important;
    }

    .d-md-inline-flex {
        display: inline-flex !important;
    }
}

@media (min-width: 992px) {
    .d-lg-none {
        display: none !important;
    }

    .d-lg-inline {
        display: inline !important;
    }

    .d-lg-inline-block {
        display: inline-block !important;
    }

    .d-lg-block {
        display: block !important;
    }

    .d-lg-table {
        display: table !important;
    }

    .d-lg-table-row {
        display: table-row !important;
    }

    .d-lg-table-cell {
        display: table-cell !important;
    }

    .d-lg-flex {
        display: flex !important;
    }

    .d-lg-inline-flex {
        display: inline-flex !important;
    }
}

@media (min-width: 1200px) {
    .d-xl-none {
        display: none !important;
    }

    .d-xl-inline {
        display: inline !important;
    }

    .d-xl-inline-block {
        display: inline-block !important;
    }

    .d-xl-block {
        display: block !important;
    }

    .d-xl-table {
        display: table !important;
    }

    .d-xl-table-row {
        display: table-row !important;
    }

    .d-xl-table-cell {
        display: table-cell !important;
    }

    .d-xl-flex {
        display: flex !important;
    }

    .d-xl-inline-flex {
        display: inline-flex !important;
    }
}

@media print {
    .d-print-none {
        display: none !important;
    }

    .d-print-inline {
        display: inline !important;
    }

    .d-print-inline-block {
        display: inline-block !important;
    }

    .d-print-block {
        display: block !important;
    }

    .d-print-table {
        display: table !important;
    }

    .d-print-table-row {
        display: table-row !important;
    }

    .d-print-table-cell {
        display: table-cell !important;
    }

    .d-print-flex {
        display: flex !important;
    }

    .d-print-inline-flex {
        display: inline-flex !important;
    }
}

.embed-responsive {
    position: relative;
    display: block;
    width: 100%;
    padding: 0;
    overflow: hidden;
}

.embed-responsive::before {
    display: block;
    content: "";
}

.embed-responsive .embed-responsive-item,
  .embed-responsive iframe,
  .embed-responsive embed,
  .embed-responsive object,
  .embed-responsive video {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: 0;
}

.embed-responsive-21by9::before {
    padding-top: 42.85714%;
}

.embed-responsive-16by9::before {
    padding-top: 56.25%;
}

.embed-responsive-4by3::before {
    padding-top: 75%;
}

.embed-responsive-1by1::before {
    padding-top: 100%;
}

.flex-row {
    flex-direction: row !important;
}

.flex-column {
    flex-direction: column !important;
}

.flex-row-reverse {
    flex-direction: row-reverse !important;
}

.flex-column-reverse {
    flex-direction: column-reverse !important;
}

.flex-wrap {
    flex-wrap: wrap !important;
}

.flex-nowrap {
    flex-wrap: nowrap !important;
}

.flex-wrap-reverse {
    flex-wrap: wrap-reverse !important;
}

.flex-fill {
    flex: 1 1 auto !important;
}

.flex-grow-0 {
    flex-grow: 0 !important;
}

.flex-grow-1 {
    flex-grow: 1 !important;
}

.flex-shrink-0 {
    flex-shrink: 0 !important;
}

.flex-shrink-1 {
    flex-shrink: 1 !important;
}

.justify-content-start {
    justify-content: flex-start !important;
}

.justify-content-end {
    justify-content: flex-end !important;
}

.justify-content-center {
    justify-content: center !important;
}

.justify-content-between {
    justify-content: space-between !important;
}

.justify-content-around {
    justify-content: space-around !important;
}

.align-items-start {
    align-items: flex-start !important;
}

.align-items-end {
    align-items: flex-end !important;
}

.align-items-center {
    align-items: center !important;
}

.align-items-baseline {
    align-items: baseline !important;
}

.align-items-stretch {
    align-items: stretch !important;
}

.align-content-start {
    align-content: flex-start !important;
}

.align-content-end {
    align-content: flex-end !important;
}

.align-content-center {
    align-content: center !important;
}

.align-content-between {
    align-content: space-between !important;
}

.align-content-around {
    align-content: space-around !important;
}

.align-content-stretch {
    align-content: stretch !important;
}

.align-self-auto {
    align-self: auto !important;
}

.align-self-start {
    align-self: flex-start !important;
}

.align-self-end {
    align-self: flex-end !important;
}

.align-self-center {
    align-self: center !important;
}

.align-self-baseline {
    align-self: baseline !important;
}

.align-self-stretch {
    align-self: stretch !important;
}

@media (min-width: 576px) {
    .flex-sm-row {
        flex-direction: row !important;
    }

    .flex-sm-column {
        flex-direction: column !important;
    }

    .flex-sm-row-reverse {
        flex-direction: row-reverse !important;
    }

    .flex-sm-column-reverse {
        flex-direction: column-reverse !important;
    }

    .flex-sm-wrap {
        flex-wrap: wrap !important;
    }

    .flex-sm-nowrap {
        flex-wrap: nowrap !important;
    }

    .flex-sm-wrap-reverse {
        flex-wrap: wrap-reverse !important;
    }

    .flex-sm-fill {
        flex: 1 1 auto !important;
    }

    .flex-sm-grow-0 {
        flex-grow: 0 !important;
    }

    .flex-sm-grow-1 {
        flex-grow: 1 !important;
    }

    .flex-sm-shrink-0 {
        flex-shrink: 0 !important;
    }

    .flex-sm-shrink-1 {
        flex-shrink: 1 !important;
    }

    .justify-content-sm-start {
        justify-content: flex-start !important;
    }

    .justify-content-sm-end {
        justify-content: flex-end !important;
    }

    .justify-content-sm-center {
        justify-content: center !important;
    }

    .justify-content-sm-between {
        justify-content: space-between !important;
    }

    .justify-content-sm-around {
        justify-content: space-around !important;
    }

    .align-items-sm-start {
        align-items: flex-start !important;
    }

    .align-items-sm-end {
        align-items: flex-end !important;
    }

    .align-items-sm-center {
        align-items: center !important;
    }

    .align-items-sm-baseline {
        align-items: baseline !important;
    }

    .align-items-sm-stretch {
        align-items: stretch !important;
    }

    .align-content-sm-start {
        align-content: flex-start !important;
    }

    .align-content-sm-end {
        align-content: flex-end !important;
    }

    .align-content-sm-center {
        align-content: center !important;
    }

    .align-content-sm-between {
        align-content: space-between !important;
    }

    .align-content-sm-around {
        align-content: space-around !important;
    }

    .align-content-sm-stretch {
        align-content: stretch !important;
    }

    .align-self-sm-auto {
        align-self: auto !important;
    }

    .align-self-sm-start {
        align-self: flex-start !important;
    }

    .align-self-sm-end {
        align-self: flex-end !important;
    }

    .align-self-sm-center {
        align-self: center !important;
    }

    .align-self-sm-baseline {
        align-self: baseline !important;
    }

    .align-self-sm-stretch {
        align-self: stretch !important;
    }
}

@media (min-width: 768px) {
    .flex-md-row {
        flex-direction: row !important;
    }

    .flex-md-column {
        flex-direction: column !important;
    }

    .flex-md-row-reverse {
        flex-direction: row-reverse !important;
    }

    .flex-md-column-reverse {
        flex-direction: column-reverse !important;
    }

    .flex-md-wrap {
        flex-wrap: wrap !important;
    }

    .flex-md-nowrap {
        flex-wrap: nowrap !important;
    }

    .flex-md-wrap-reverse {
        flex-wrap: wrap-reverse !important;
    }

    .flex-md-fill {
        flex: 1 1 auto !important;
    }

    .flex-md-grow-0 {
        flex-grow: 0 !important;
    }

    .flex-md-grow-1 {
        flex-grow: 1 !important;
    }

    .flex-md-shrink-0 {
        flex-shrink: 0 !important;
    }

    .flex-md-shrink-1 {
        flex-shrink: 1 !important;
    }

    .justify-content-md-start {
        justify-content: flex-start !important;
    }

    .justify-content-md-end {
        justify-content: flex-end !important;
    }

    .justify-content-md-center {
        justify-content: center !important;
    }

    .justify-content-md-between {
        justify-content: space-between !important;
    }

    .justify-content-md-around {
        justify-content: space-around !important;
    }

    .align-items-md-start {
        align-items: flex-start !important;
    }

    .align-items-md-end {
        align-items: flex-end !important;
    }

    .align-items-md-center {
        align-items: center !important;
    }

    .align-items-md-baseline {
        align-items: baseline !important;
    }

    .align-items-md-stretch {
        align-items: stretch !important;
    }

    .align-content-md-start {
        align-content: flex-start !important;
    }

    .align-content-md-end {
        align-content: flex-end !important;
    }

    .align-content-md-center {
        align-content: center !important;
    }

    .align-content-md-between {
        align-content: space-between !important;
    }

    .align-content-md-around {
        align-content: space-around !important;
    }

    .align-content-md-stretch {
        align-content: stretch !important;
    }

    .align-self-md-auto {
        align-self: auto !important;
    }

    .align-self-md-start {
        align-self: flex-start !important;
    }

    .align-self-md-end {
        align-self: flex-end !important;
    }

    .align-self-md-center {
        align-self: center !important;
    }

    .align-self-md-baseline {
        align-self: baseline !important;
    }

    .align-self-md-stretch {
        align-self: stretch !important;
    }
}

@media (min-width: 992px) {
    .flex-lg-row {
        flex-direction: row !important;
    }

    .flex-lg-column {
        flex-direction: column !important;
    }

    .flex-lg-row-reverse {
        flex-direction: row-reverse !important;
    }

    .flex-lg-column-reverse {
        flex-direction: column-reverse !important;
    }

    .flex-lg-wrap {
        flex-wrap: wrap !important;
    }

    .flex-lg-nowrap {
        flex-wrap: nowrap !important;
    }

    .flex-lg-wrap-reverse {
        flex-wrap: wrap-reverse !important;
    }

    .flex-lg-fill {
        flex: 1 1 auto !important;
    }

    .flex-lg-grow-0 {
        flex-grow: 0 !important;
    }

    .flex-lg-grow-1 {
        flex-grow: 1 !important;
    }

    .flex-lg-shrink-0 {
        flex-shrink: 0 !important;
    }

    .flex-lg-shrink-1 {
        flex-shrink: 1 !important;
    }

    .justify-content-lg-start {
        justify-content: flex-start !important;
    }

    .justify-content-lg-end {
        justify-content: flex-end !important;
    }

    .justify-content-lg-center {
        justify-content: center !important;
    }

    .justify-content-lg-between {
        justify-content: space-between !important;
    }

    .justify-content-lg-around {
        justify-content: space-around !important;
    }

    .align-items-lg-start {
        align-items: flex-start !important;
    }

    .align-items-lg-end {
        align-items: flex-end !important;
    }

    .align-items-lg-center {
        align-items: center !important;
    }

    .align-items-lg-baseline {
        align-items: baseline !important;
    }

    .align-items-lg-stretch {
        align-items: stretch !important;
    }

    .align-content-lg-start {
        align-content: flex-start !important;
    }

    .align-content-lg-end {
        align-content: flex-end !important;
    }

    .align-content-lg-center {
        align-content: center !important;
    }

    .align-content-lg-between {
        align-content: space-between !important;
    }

    .align-content-lg-around {
        align-content: space-around !important;
    }

    .align-content-lg-stretch {
        align-content: stretch !important;
    }

    .align-self-lg-auto {
        align-self: auto !important;
    }

    .align-self-lg-start {
        align-self: flex-start !important;
    }

    .align-self-lg-end {
        align-self: flex-end !important;
    }

    .align-self-lg-center {
        align-self: center !important;
    }

    .align-self-lg-baseline {
        align-self: baseline !important;
    }

    .align-self-lg-stretch {
        align-self: stretch !important;
    }
}

@media (min-width: 1200px) {
    .flex-xl-row {
        flex-direction: row !important;
    }

    .flex-xl-column {
        flex-direction: column !important;
    }

    .flex-xl-row-reverse {
        flex-direction: row-reverse !important;
    }

    .flex-xl-column-reverse {
        flex-direction: column-reverse !important;
    }

    .flex-xl-wrap {
        flex-wrap: wrap !important;
    }

    .flex-xl-nowrap {
        flex-wrap: nowrap !important;
    }

    .flex-xl-wrap-reverse {
        flex-wrap: wrap-reverse !important;
    }

    .flex-xl-fill {
        flex: 1 1 auto !important;
    }

    .flex-xl-grow-0 {
        flex-grow: 0 !important;
    }

    .flex-xl-grow-1 {
        flex-grow: 1 !important;
    }

    .flex-xl-shrink-0 {
        flex-shrink: 0 !important;
    }

    .flex-xl-shrink-1 {
        flex-shrink: 1 !important;
    }

    .justify-content-xl-start {
        justify-content: flex-start !important;
    }

    .justify-content-xl-end {
        justify-content: flex-end !important;
    }

    .justify-content-xl-center {
        justify-content: center !important;
    }

    .justify-content-xl-between {
        justify-content: space-between !important;
    }

    .justify-content-xl-around {
        justify-content: space-around !important;
    }

    .align-items-xl-start {
        align-items: flex-start !important;
    }

    .align-items-xl-end {
        align-items: flex-end !important;
    }

    .align-items-xl-center {
        align-items: center !important;
    }

    .align-items-xl-baseline {
        align-items: baseline !important;
    }

    .align-items-xl-stretch {
        align-items: stretch !important;
    }

    .align-content-xl-start {
        align-content: flex-start !important;
    }

    .align-content-xl-end {
        align-content: flex-end !important;
    }

    .align-content-xl-center {
        align-content: center !important;
    }

    .align-content-xl-between {
        align-content: space-between !important;
    }

    .align-content-xl-around {
        align-content: space-around !important;
    }

    .align-content-xl-stretch {
        align-content: stretch !important;
    }

    .align-self-xl-auto {
        align-self: auto !important;
    }

    .align-self-xl-start {
        align-self: flex-start !important;
    }

    .align-self-xl-end {
        align-self: flex-end !important;
    }

    .align-self-xl-center {
        align-self: center !important;
    }

    .align-self-xl-baseline {
        align-self: baseline !important;
    }

    .align-self-xl-stretch {
        align-self: stretch !important;
    }
}

.float-left {
    float: left !important;
}

.float-right {
    float: right !important;
}

.float-none {
    float: none !important;
}

@media (min-width: 576px) {
    .float-sm-left {
        float: left !important;
    }

    .float-sm-right {
        float: right !important;
    }

    .float-sm-none {
        float: none !important;
    }
}

@media (min-width: 768px) {
    .float-md-left {
        float: left !important;
    }

    .float-md-right {
        float: right !important;
    }

    .float-md-none {
        float: none !important;
    }
}

@media (min-width: 992px) {
    .float-lg-left {
        float: left !important;
    }

    .float-lg-right {
        float: right !important;
    }

    .float-lg-none {
        float: none !important;
    }
}

@media (min-width: 1200px) {
    .float-xl-left {
        float: left !important;
    }

    .float-xl-right {
        float: right !important;
    }

    .float-xl-none {
        float: none !important;
    }
}

.overflow-auto {
    overflow: auto !important;
}

.overflow-hidden {
    overflow: hidden !important;
}

.position-static {
    position: static !important;
}

.position-relative {
    position: relative !important;
}

.position-absolute {
    position: absolute !important;
}

.position-fixed, .headroom--pinned, .headroom--unpinned {
    position: fixed !important;
}

.position-sticky {
    position: sticky !important;
}

.fixed-top {
    position: fixed;
    top: 0;
    right: 0;
    left: 0;
    z-index: 1030;
}

.fixed-bottom {
    position: fixed;
    right: 0;
    bottom: 0;
    left: 0;
    z-index: 1030;
}

@supports (position: sticky) {
    .sticky-top {
        position: sticky;
        top: 0;
        z-index: 1020;
    }
}

.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
}

.sr-only-focusable:active, .sr-only-focusable:focus {
    position: static;
    width: auto;
    height: auto;
    overflow: visible;
    clip: auto;
    white-space: normal;
}

.shadow-sm {
    box-shadow: 0 0.125rem 0.25rem rgba(38, 40, 51, 0.075) !important;
}

.shadow {
    box-shadow: 0 0.5rem 1rem rgba(38, 40, 51, 0.15) !important;
}

.shadow-lg {
    box-shadow: 0 1rem 3rem rgba(38, 40, 51, 0.175) !important;
}

.shadow-none {
    box-shadow: none !important;
}

.w-25 {
    width: 25% !important;
}

.w-50 {
    width: 50% !important;
}

.w-75 {
    width: 75% !important;
}

.w-100 {
    width: 100% !important;
}

.w-auto {
    width: auto !important;
}

.w-60 {
    width: 60% !important;
}

.h-25 {
    height: 25% !important;
}

.h-50 {
    height: 50% !important;
}

.h-75 {
    height: 75% !important;
}

.h-100 {
    height: 100% !important;
}

.h-auto {
    height: auto !important;
}

.h-60 {
    height: 60% !important;
}

.mw-100 {
    max-width: 100% !important;
}

.mh-100 {
    max-height: 100% !important;
}

.min-vw-100 {
    min-width: 100vw !important;
}

.min-vh-100 {
    min-height: 100vh !important;
}

.vw-100 {
    width: 100vw !important;
}

.vh-100 {
    height: 100vh !important;
}

.stretched-link::after {
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    z-index: 1;
    pointer-events: auto;
    content: "";
    background-color: rgba(0, 0, 0, 0);
}

.m-0 {
    margin: 0 !important;
}

.mt-0,
.my-0 {
    margin-top: 0 !important;
}

.mr-0,
.mx-0 {
    margin-right: 0 !important;
}

.mb-0,
.my-0 {
    margin-bottom: 0 !important;
}

.ml-0,
.mx-0 {
    margin-left: 0 !important;
}

.m-1 {
    margin: 0.25rem !important;
}

.mt-1,
.my-1 {
    margin-top: 0.25rem !important;
}

.mr-1,
.mx-1 {
    margin-right: 0.25rem !important;
}

.mb-1,
.my-1 {
    margin-bottom: 0.25rem !important;
}

.ml-1,
.mx-1 {
    margin-left: 0.25rem !important;
}

.m-2 {
    margin: 0.5rem !important;
}

.mt-2,
.my-2 {
    margin-top: 0.5rem !important;
}

.mr-2,
.mx-2 {
    margin-right: 0.5rem !important;
}

.mb-2,
.my-2 {
    margin-bottom: 0.5rem !important;
}

.ml-2,
.mx-2 {
    margin-left: 0.5rem !important;
}

.m-3 {
    margin: 1rem !important;
}

.mt-3,
.my-3 {
    margin-top: 1rem !important;
}

.mr-3,
.mx-3 {
    margin-right: 1rem !important;
}

.mb-3,
.my-3 {
    margin-bottom: 1rem !important;
}

.ml-3,
.mx-3 {
    margin-left: 1rem !important;
}

.m-4 {
    margin: 1.5rem !important;
}

.mt-4,
.my-4 {
    margin-top: 1.5rem !important;
}

.mr-4,
.mx-4 {
    margin-right: 1.5rem !important;
}

.mb-4,
.my-4 {
    margin-bottom: 1.5rem !important;
}

.ml-4,
.mx-4 {
    margin-left: 1.5rem !important;
}

.m-5 {
    margin: 3rem !important;
}

.mt-5,
.my-5 {
    margin-top: 3rem !important;
}

.mr-5,
.mx-5 {
    margin-right: 3rem !important;
}

.mb-5,
.my-5 {
    margin-bottom: 3rem !important;
}

.ml-5,
.mx-5 {
    margin-left: 3rem !important;
}

.m-6 {
    margin: 5rem !important;
}

.mt-6,
.my-6 {
    margin-top: 5rem !important;
}

.mr-6,
.mx-6 {
    margin-right: 5rem !important;
}

.mb-6,
.my-6 {
    margin-bottom: 5rem !important;
}

.ml-6,
.mx-6 {
    margin-left: 5rem !important;
}

.m-7 {
    margin: 8rem !important;
}

.mt-7,
.my-7 {
    margin-top: 8rem !important;
}

.mr-7,
.mx-7 {
    margin-right: 8rem !important;
}

.mb-7,
.my-7 {
    margin-bottom: 8rem !important;
}

.ml-7,
.mx-7 {
    margin-left: 8rem !important;
}

.m-8 {
    margin: 10rem !important;
}

.mt-8,
.my-8 {
    margin-top: 10rem !important;
}

.mr-8,
.mx-8 {
    margin-right: 10rem !important;
}

.mb-8,
.my-8 {
    margin-bottom: 10rem !important;
}

.ml-8,
.mx-8 {
    margin-left: 10rem !important;
}

.m-9 {
    margin: 11rem !important;
}

.mt-9,
.my-9 {
    margin-top: 11rem !important;
}

.mr-9,
.mx-9 {
    margin-right: 11rem !important;
}

.mb-9,
.my-9 {
    margin-bottom: 11rem !important;
}

.ml-9,
.mx-9 {
    margin-left: 11rem !important;
}

.m-10 {
    margin: 15rem !important;
}

.mt-10,
.my-10 {
    margin-top: 15rem !important;
}

.mr-10,
.mx-10 {
    margin-right: 15rem !important;
}

.mb-10,
.my-10 {
    margin-bottom: 15rem !important;
}

.ml-10,
.mx-10 {
    margin-left: 15rem !important;
}

.m-sm {
    margin: 1rem !important;
}

.mt-sm,
.my-sm {
    margin-top: 1rem !important;
}

.mr-sm,
.mx-sm {
    margin-right: 1rem !important;
}

.mb-sm,
.my-sm {
    margin-bottom: 1rem !important;
}

.ml-sm,
.mx-sm {
    margin-left: 1rem !important;
}

.m-md {
    margin: 2rem !important;
}

.mt-md,
.my-md {
    margin-top: 2rem !important;
}

.mr-md,
.mx-md {
    margin-right: 2rem !important;
}

.mb-md,
.my-md {
    margin-bottom: 2rem !important;
}

.ml-md,
.mx-md {
    margin-left: 2rem !important;
}

.m-lg {
    margin: 4rem !important;
}

.mt-lg,
.my-lg {
    margin-top: 4rem !important;
}

.mr-lg,
.mx-lg {
    margin-right: 4rem !important;
}

.mb-lg,
.my-lg {
    margin-bottom: 4rem !important;
}

.ml-lg,
.mx-lg {
    margin-left: 4rem !important;
}

.m-xl {
    margin: 8rem !important;
}

.mt-xl,
.my-xl {
    margin-top: 8rem !important;
}

.mr-xl,
.mx-xl {
    margin-right: 8rem !important;
}

.mb-xl,
.my-xl {
    margin-bottom: 8rem !important;
}

.ml-xl,
.mx-xl {
    margin-left: 8rem !important;
}

.p-0 {
    padding: 0 !important;
}

.pt-0,
.py-0 {
    padding-top: 0 !important;
}

.pr-0,
.px-0 {
    padding-right: 0 !important;
}

.pb-0,
.py-0 {
    padding-bottom: 0 !important;
}

.pl-0,
.px-0 {
    padding-left: 0 !important;
}

.p-1 {
    padding: 0.25rem !important;
}

.pt-1,
.py-1 {
    padding-top: 0.25rem !important;
}

.pr-1,
.px-1 {
    padding-right: 0.25rem !important;
}

.pb-1,
.py-1 {
    padding-bottom: 0.25rem !important;
}

.pl-1,
.px-1 {
    padding-left: 0.25rem !important;
}

.p-2 {
    padding: 0.5rem !important;
}

.pt-2,
.py-2 {
    padding-top: 0.5rem !important;
}

.pr-2,
.px-2 {
    padding-right: 0.5rem !important;
}

.pb-2,
.py-2 {
    padding-bottom: 0.5rem !important;
}

.pl-2,
.px-2 {
    padding-left: 0.5rem !important;
}

.p-3 {
    padding: 1rem !important;
}

.pt-3,
.py-3 {
    padding-top: 1rem !important;
}

.pr-3,
.px-3 {
    padding-right: 1rem !important;
}

.pb-3,
.py-3 {
    padding-bottom: 1rem !important;
}

.pl-3,
.px-3 {
    padding-left: 1rem !important;
}

.p-4 {
    padding: 1.5rem !important;
}

.pt-4,
.py-4 {
    padding-top: 1.5rem !important;
}

.pr-4,
.px-4 {
    padding-right: 1.5rem !important;
}

.pb-4,
.py-4 {
    padding-bottom: 1.5rem !important;
}

.pl-4,
.px-4 {
    padding-left: 1.5rem !important;
}

.p-5 {
    padding: 3rem !important;
}

.pt-5,
.py-5 {
    padding-top: 3rem !important;
}

.pr-5,
.px-5 {
    padding-right: 3rem !important;
}

.pb-5,
.py-5 {
    padding-bottom: 3rem !important;
}

.pl-5,
.px-5 {
    padding-left: 3rem !important;
}

.p-6 {
    padding: 5rem !important;
}

.pt-6,
.py-6 {
    padding-top: 5rem !important;
}

.pr-6,
.px-6 {
    padding-right: 5rem !important;
}

.pb-6,
.py-6 {
    padding-bottom: 5rem !important;
}

.pl-6,
.px-6 {
    padding-left: 5rem !important;
}

.p-7 {
    padding: 8rem !important;
}

.pt-7,
.py-7 {
    padding-top: 8rem !important;
}

.pr-7,
.px-7 {
    padding-right: 8rem !important;
}

.pb-7,
.py-7 {
    padding-bottom: 8rem !important;
}

.pl-7,
.px-7 {
    padding-left: 8rem !important;
}

.p-8 {
    padding: 10rem !important;
}

.pt-8,
.py-8 {
    padding-top: 10rem !important;
}

.pr-8,
.px-8 {
    padding-right: 10rem !important;
}

.pb-8,
.py-8 {
    padding-bottom: 10rem !important;
}

.pl-8,
.px-8 {
    padding-left: 10rem !important;
}

.p-9 {
    padding: 11rem !important;
}

.pt-9,
.py-9 {
    padding-top: 11rem !important;
}

.pr-9,
.px-9 {
    padding-right: 11rem !important;
}

.pb-9,
.py-9 {
    padding-bottom: 11rem !important;
}

.pl-9,
.px-9 {
    padding-left: 11rem !important;
}

.p-10 {
    padding: 15rem !important;
}

.pt-10,
.py-10 {
    padding-top: 15rem !important;
}

.pr-10,
.px-10 {
    padding-right: 15rem !important;
}

.pb-10,
.py-10 {
    padding-bottom: 15rem !important;
}

.pl-10,
.px-10 {
    padding-left: 15rem !important;
}

.p-sm {
    padding: 1rem !important;
}

.pt-sm,
.py-sm {
    padding-top: 1rem !important;
}

.pr-sm,
.px-sm {
    padding-right: 1rem !important;
}

.pb-sm,
.py-sm {
    padding-bottom: 1rem !important;
}

.pl-sm,
.px-sm {
    padding-left: 1rem !important;
}

.p-md {
    padding: 2rem !important;
}

.pt-md,
.py-md {
    padding-top: 2rem !important;
}

.pr-md,
.px-md {
    padding-right: 2rem !important;
}

.pb-md,
.py-md {
    padding-bottom: 2rem !important;
}

.pl-md,
.px-md {
    padding-left: 2rem !important;
}

.p-lg {
    padding: 4rem !important;
}

.pt-lg,
.py-lg {
    padding-top: 4rem !important;
}

.pr-lg,
.px-lg {
    padding-right: 4rem !important;
}

.pb-lg,
.py-lg {
    padding-bottom: 4rem !important;
}

.pl-lg,
.px-lg {
    padding-left: 4rem !important;
}

.p-xl {
    padding: 8rem !important;
}

.pt-xl,
.py-xl {
    padding-top: 8rem !important;
}

.pr-xl,
.px-xl {
    padding-right: 8rem !important;
}

.pb-xl,
.py-xl {
    padding-bottom: 8rem !important;
}

.pl-xl,
.px-xl {
    padding-left: 8rem !important;
}

.m-n1 {
    margin: -0.25rem !important;
}

.mt-n1,
.my-n1 {
    margin-top: -0.25rem !important;
}

.mr-n1,
.mx-n1 {
    margin-right: -0.25rem !important;
}

.mb-n1,
.my-n1 {
    margin-bottom: -0.25rem !important;
}

.ml-n1,
.mx-n1 {
    margin-left: -0.25rem !important;
}

.m-n2 {
    margin: -0.5rem !important;
}

.mt-n2,
.my-n2 {
    margin-top: -0.5rem !important;
}

.mr-n2,
.mx-n2 {
    margin-right: -0.5rem !important;
}

.mb-n2,
.my-n2 {
    margin-bottom: -0.5rem !important;
}

.ml-n2,
.mx-n2 {
    margin-left: -0.5rem !important;
}

.m-n3 {
    margin: -1rem !important;
}

.mt-n3,
.my-n3 {
    margin-top: -1rem !important;
}

.mr-n3,
.mx-n3 {
    margin-right: -1rem !important;
}

.mb-n3,
.my-n3 {
    margin-bottom: -1rem !important;
}

.ml-n3,
.mx-n3 {
    margin-left: -1rem !important;
}

.m-n4 {
    margin: -1.5rem !important;
}

.mt-n4,
.my-n4 {
    margin-top: -1.5rem !important;
}

.mr-n4,
.mx-n4 {
    margin-right: -1.5rem !important;
}

.mb-n4,
.my-n4 {
    margin-bottom: -1.5rem !important;
}

.ml-n4,
.mx-n4 {
    margin-left: -1.5rem !important;
}

.m-n5 {
    margin: -3rem !important;
}

.mt-n5,
.my-n5 {
    margin-top: -3rem !important;
}

.mr-n5,
.mx-n5 {
    margin-right: -3rem !important;
}

.mb-n5,
.my-n5 {
    margin-bottom: -3rem !important;
}

.ml-n5,
.mx-n5 {
    margin-left: -3rem !important;
}

.m-n6 {
    margin: -5rem !important;
}

.mt-n6,
.my-n6 {
    margin-top: -5rem !important;
}

.mr-n6,
.mx-n6 {
    margin-right: -5rem !important;
}

.mb-n6,
.my-n6 {
    margin-bottom: -5rem !important;
}

.ml-n6,
.mx-n6 {
    margin-left: -5rem !important;
}

.m-n7 {
    margin: -8rem !important;
}

.mt-n7,
.my-n7 {
    margin-top: -8rem !important;
}

.mr-n7,
.mx-n7 {
    margin-right: -8rem !important;
}

.mb-n7,
.my-n7 {
    margin-bottom: -8rem !important;
}

.ml-n7,
.mx-n7 {
    margin-left: -8rem !important;
}

.m-n8 {
    margin: -10rem !important;
}

.mt-n8,
.my-n8 {
    margin-top: -10rem !important;
}

.mr-n8,
.mx-n8 {
    margin-right: -10rem !important;
}

.mb-n8,
.my-n8 {
    margin-bottom: -10rem !important;
}

.ml-n8,
.mx-n8 {
    margin-left: -10rem !important;
}

.m-n9 {
    margin: -11rem !important;
}

.mt-n9,
.my-n9 {
    margin-top: -11rem !important;
}

.mr-n9,
.mx-n9 {
    margin-right: -11rem !important;
}

.mb-n9,
.my-n9 {
    margin-bottom: -11rem !important;
}

.ml-n9,
.mx-n9 {
    margin-left: -11rem !important;
}

.m-n10 {
    margin: -15rem !important;
}

.mt-n10,
.my-n10 {
    margin-top: -15rem !important;
}

.mr-n10,
.mx-n10 {
    margin-right: -15rem !important;
}

.mb-n10,
.my-n10 {
    margin-bottom: -15rem !important;
}

.ml-n10,
.mx-n10 {
    margin-left: -15rem !important;
}

.m-nsm {
    margin: -1rem !important;
}

.mt-nsm,
.my-nsm {
    margin-top: -1rem !important;
}

.mr-nsm,
.mx-nsm {
    margin-right: -1rem !important;
}

.mb-nsm,
.my-nsm {
    margin-bottom: -1rem !important;
}

.ml-nsm,
.mx-nsm {
    margin-left: -1rem !important;
}

.m-nmd {
    margin: -2rem !important;
}

.mt-nmd,
.my-nmd {
    margin-top: -2rem !important;
}

.mr-nmd,
.mx-nmd {
    margin-right: -2rem !important;
}

.mb-nmd,
.my-nmd {
    margin-bottom: -2rem !important;
}

.ml-nmd,
.mx-nmd {
    margin-left: -2rem !important;
}

.m-nlg {
    margin: -4rem !important;
}

.mt-nlg,
.my-nlg {
    margin-top: -4rem !important;
}

.mr-nlg,
.mx-nlg {
    margin-right: -4rem !important;
}

.mb-nlg,
.my-nlg {
    margin-bottom: -4rem !important;
}

.ml-nlg,
.mx-nlg {
    margin-left: -4rem !important;
}

.m-nxl {
    margin: -8rem !important;
}

.mt-nxl,
.my-nxl {
    margin-top: -8rem !important;
}

.mr-nxl,
.mx-nxl {
    margin-right: -8rem !important;
}

.mb-nxl,
.my-nxl {
    margin-bottom: -8rem !important;
}

.ml-nxl,
.mx-nxl {
    margin-left: -8rem !important;
}

.m-auto {
    margin: auto !important;
}

.mt-auto,
.my-auto {
    margin-top: auto !important;
}

.mr-auto,
.mx-auto {
    margin-right: auto !important;
}

.mb-auto,
.my-auto {
    margin-bottom: auto !important;
}

.ml-auto,
.mx-auto {
    margin-left: auto !important;
}

@media (min-width: 576px) {
    .m-sm-0 {
        margin: 0 !important;
    }

    .mt-sm-0,
  .my-sm-0 {
        margin-top: 0 !important;
    }

    .mr-sm-0,
  .mx-sm-0 {
        margin-right: 0 !important;
    }

    .mb-sm-0,
  .my-sm-0 {
        margin-bottom: 0 !important;
    }

    .ml-sm-0,
  .mx-sm-0 {
        margin-left: 0 !important;
    }

    .m-sm-1 {
        margin: 0.25rem !important;
    }

    .mt-sm-1,
  .my-sm-1 {
        margin-top: 0.25rem !important;
    }

    .mr-sm-1,
  .mx-sm-1 {
        margin-right: 0.25rem !important;
    }

    .mb-sm-1,
  .my-sm-1 {
        margin-bottom: 0.25rem !important;
    }

    .ml-sm-1,
  .mx-sm-1 {
        margin-left: 0.25rem !important;
    }

    .m-sm-2 {
        margin: 0.5rem !important;
    }

    .mt-sm-2,
  .my-sm-2 {
        margin-top: 0.5rem !important;
    }

    .mr-sm-2,
  .mx-sm-2 {
        margin-right: 0.5rem !important;
    }

    .mb-sm-2,
  .my-sm-2 {
        margin-bottom: 0.5rem !important;
    }

    .ml-sm-2,
  .mx-sm-2 {
        margin-left: 0.5rem !important;
    }

    .m-sm-3 {
        margin: 1rem !important;
    }

    .mt-sm-3,
  .my-sm-3 {
        margin-top: 1rem !important;
    }

    .mr-sm-3,
  .mx-sm-3 {
        margin-right: 1rem !important;
    }

    .mb-sm-3,
  .my-sm-3 {
        margin-bottom: 1rem !important;
    }

    .ml-sm-3,
  .mx-sm-3 {
        margin-left: 1rem !important;
    }

    .m-sm-4 {
        margin: 1.5rem !important;
    }

    .mt-sm-4,
  .my-sm-4 {
        margin-top: 1.5rem !important;
    }

    .mr-sm-4,
  .mx-sm-4 {
        margin-right: 1.5rem !important;
    }

    .mb-sm-4,
  .my-sm-4 {
        margin-bottom: 1.5rem !important;
    }

    .ml-sm-4,
  .mx-sm-4 {
        margin-left: 1.5rem !important;
    }

    .m-sm-5 {
        margin: 3rem !important;
    }

    .mt-sm-5,
  .my-sm-5 {
        margin-top: 3rem !important;
    }

    .mr-sm-5,
  .mx-sm-5 {
        margin-right: 3rem !important;
    }

    .mb-sm-5,
  .my-sm-5 {
        margin-bottom: 3rem !important;
    }

    .ml-sm-5,
  .mx-sm-5 {
        margin-left: 3rem !important;
    }

    .m-sm-6 {
        margin: 5rem !important;
    }

    .mt-sm-6,
  .my-sm-6 {
        margin-top: 5rem !important;
    }

    .mr-sm-6,
  .mx-sm-6 {
        margin-right: 5rem !important;
    }

    .mb-sm-6,
  .my-sm-6 {
        margin-bottom: 5rem !important;
    }

    .ml-sm-6,
  .mx-sm-6 {
        margin-left: 5rem !important;
    }

    .m-sm-7 {
        margin: 8rem !important;
    }

    .mt-sm-7,
  .my-sm-7 {
        margin-top: 8rem !important;
    }

    .mr-sm-7,
  .mx-sm-7 {
        margin-right: 8rem !important;
    }

    .mb-sm-7,
  .my-sm-7 {
        margin-bottom: 8rem !important;
    }

    .ml-sm-7,
  .mx-sm-7 {
        margin-left: 8rem !important;
    }

    .m-sm-8 {
        margin: 10rem !important;
    }

    .mt-sm-8,
  .my-sm-8 {
        margin-top: 10rem !important;
    }

    .mr-sm-8,
  .mx-sm-8 {
        margin-right: 10rem !important;
    }

    .mb-sm-8,
  .my-sm-8 {
        margin-bottom: 10rem !important;
    }

    .ml-sm-8,
  .mx-sm-8 {
        margin-left: 10rem !important;
    }

    .m-sm-9 {
        margin: 11rem !important;
    }

    .mt-sm-9,
  .my-sm-9 {
        margin-top: 11rem !important;
    }

    .mr-sm-9,
  .mx-sm-9 {
        margin-right: 11rem !important;
    }

    .mb-sm-9,
  .my-sm-9 {
        margin-bottom: 11rem !important;
    }

    .ml-sm-9,
  .mx-sm-9 {
        margin-left: 11rem !important;
    }

    .m-sm-10 {
        margin: 15rem !important;
    }

    .mt-sm-10,
  .my-sm-10 {
        margin-top: 15rem !important;
    }

    .mr-sm-10,
  .mx-sm-10 {
        margin-right: 15rem !important;
    }

    .mb-sm-10,
  .my-sm-10 {
        margin-bottom: 15rem !important;
    }

    .ml-sm-10,
  .mx-sm-10 {
        margin-left: 15rem !important;
    }

    .m-sm-sm {
        margin: 1rem !important;
    }

    .mt-sm-sm,
  .my-sm-sm {
        margin-top: 1rem !important;
    }

    .mr-sm-sm,
  .mx-sm-sm {
        margin-right: 1rem !important;
    }

    .mb-sm-sm,
  .my-sm-sm {
        margin-bottom: 1rem !important;
    }

    .ml-sm-sm,
  .mx-sm-sm {
        margin-left: 1rem !important;
    }

    .m-sm-md {
        margin: 2rem !important;
    }

    .mt-sm-md,
  .my-sm-md {
        margin-top: 2rem !important;
    }

    .mr-sm-md,
  .mx-sm-md {
        margin-right: 2rem !important;
    }

    .mb-sm-md,
  .my-sm-md {
        margin-bottom: 2rem !important;
    }

    .ml-sm-md,
  .mx-sm-md {
        margin-left: 2rem !important;
    }

    .m-sm-lg {
        margin: 4rem !important;
    }

    .mt-sm-lg,
  .my-sm-lg {
        margin-top: 4rem !important;
    }

    .mr-sm-lg,
  .mx-sm-lg {
        margin-right: 4rem !important;
    }

    .mb-sm-lg,
  .my-sm-lg {
        margin-bottom: 4rem !important;
    }

    .ml-sm-lg,
  .mx-sm-lg {
        margin-left: 4rem !important;
    }

    .m-sm-xl {
        margin: 8rem !important;
    }

    .mt-sm-xl,
  .my-sm-xl {
        margin-top: 8rem !important;
    }

    .mr-sm-xl,
  .mx-sm-xl {
        margin-right: 8rem !important;
    }

    .mb-sm-xl,
  .my-sm-xl {
        margin-bottom: 8rem !important;
    }

    .ml-sm-xl,
  .mx-sm-xl {
        margin-left: 8rem !important;
    }

    .p-sm-0 {
        padding: 0 !important;
    }

    .pt-sm-0,
  .py-sm-0 {
        padding-top: 0 !important;
    }

    .pr-sm-0,
  .px-sm-0 {
        padding-right: 0 !important;
    }

    .pb-sm-0,
  .py-sm-0 {
        padding-bottom: 0 !important;
    }

    .pl-sm-0,
  .px-sm-0 {
        padding-left: 0 !important;
    }

    .p-sm-1 {
        padding: 0.25rem !important;
    }

    .pt-sm-1,
  .py-sm-1 {
        padding-top: 0.25rem !important;
    }

    .pr-sm-1,
  .px-sm-1 {
        padding-right: 0.25rem !important;
    }

    .pb-sm-1,
  .py-sm-1 {
        padding-bottom: 0.25rem !important;
    }

    .pl-sm-1,
  .px-sm-1 {
        padding-left: 0.25rem !important;
    }

    .p-sm-2 {
        padding: 0.5rem !important;
    }

    .pt-sm-2,
  .py-sm-2 {
        padding-top: 0.5rem !important;
    }

    .pr-sm-2,
  .px-sm-2 {
        padding-right: 0.5rem !important;
    }

    .pb-sm-2,
  .py-sm-2 {
        padding-bottom: 0.5rem !important;
    }

    .pl-sm-2,
  .px-sm-2 {
        padding-left: 0.5rem !important;
    }

    .p-sm-3 {
        padding: 1rem !important;
    }

    .pt-sm-3,
  .py-sm-3 {
        padding-top: 1rem !important;
    }

    .pr-sm-3,
  .px-sm-3 {
        padding-right: 1rem !important;
    }

    .pb-sm-3,
  .py-sm-3 {
        padding-bottom: 1rem !important;
    }

    .pl-sm-3,
  .px-sm-3 {
        padding-left: 1rem !important;
    }

    .p-sm-4 {
        padding: 1.5rem !important;
    }

    .pt-sm-4,
  .py-sm-4 {
        padding-top: 1.5rem !important;
    }

    .pr-sm-4,
  .px-sm-4 {
        padding-right: 1.5rem !important;
    }

    .pb-sm-4,
  .py-sm-4 {
        padding-bottom: 1.5rem !important;
    }

    .pl-sm-4,
  .px-sm-4 {
        padding-left: 1.5rem !important;
    }

    .p-sm-5 {
        padding: 3rem !important;
    }

    .pt-sm-5,
  .py-sm-5 {
        padding-top: 3rem !important;
    }

    .pr-sm-5,
  .px-sm-5 {
        padding-right: 3rem !important;
    }

    .pb-sm-5,
  .py-sm-5 {
        padding-bottom: 3rem !important;
    }

    .pl-sm-5,
  .px-sm-5 {
        padding-left: 3rem !important;
    }

    .p-sm-6 {
        padding: 5rem !important;
    }

    .pt-sm-6,
  .py-sm-6 {
        padding-top: 5rem !important;
    }

    .pr-sm-6,
  .px-sm-6 {
        padding-right: 5rem !important;
    }

    .pb-sm-6,
  .py-sm-6 {
        padding-bottom: 5rem !important;
    }

    .pl-sm-6,
  .px-sm-6 {
        padding-left: 5rem !important;
    }

    .p-sm-7 {
        padding: 8rem !important;
    }

    .pt-sm-7,
  .py-sm-7 {
        padding-top: 8rem !important;
    }

    .pr-sm-7,
  .px-sm-7 {
        padding-right: 8rem !important;
    }

    .pb-sm-7,
  .py-sm-7 {
        padding-bottom: 8rem !important;
    }

    .pl-sm-7,
  .px-sm-7 {
        padding-left: 8rem !important;
    }

    .p-sm-8 {
        padding: 10rem !important;
    }

    .pt-sm-8,
  .py-sm-8 {
        padding-top: 10rem !important;
    }

    .pr-sm-8,
  .px-sm-8 {
        padding-right: 10rem !important;
    }

    .pb-sm-8,
  .py-sm-8 {
        padding-bottom: 10rem !important;
    }

    .pl-sm-8,
  .px-sm-8 {
        padding-left: 10rem !important;
    }

    .p-sm-9 {
        padding: 11rem !important;
    }

    .pt-sm-9,
  .py-sm-9 {
        padding-top: 11rem !important;
    }

    .pr-sm-9,
  .px-sm-9 {
        padding-right: 11rem !important;
    }

    .pb-sm-9,
  .py-sm-9 {
        padding-bottom: 11rem !important;
    }

    .pl-sm-9,
  .px-sm-9 {
        padding-left: 11rem !important;
    }

    .p-sm-10 {
        padding: 15rem !important;
    }

    .pt-sm-10,
  .py-sm-10 {
        padding-top: 15rem !important;
    }

    .pr-sm-10,
  .px-sm-10 {
        padding-right: 15rem !important;
    }

    .pb-sm-10,
  .py-sm-10 {
        padding-bottom: 15rem !important;
    }

    .pl-sm-10,
  .px-sm-10 {
        padding-left: 15rem !important;
    }

    .p-sm-sm {
        padding: 1rem !important;
    }

    .pt-sm-sm,
  .py-sm-sm {
        padding-top: 1rem !important;
    }

    .pr-sm-sm,
  .px-sm-sm {
        padding-right: 1rem !important;
    }

    .pb-sm-sm,
  .py-sm-sm {
        padding-bottom: 1rem !important;
    }

    .pl-sm-sm,
  .px-sm-sm {
        padding-left: 1rem !important;
    }

    .p-sm-md {
        padding: 2rem !important;
    }

    .pt-sm-md,
  .py-sm-md {
        padding-top: 2rem !important;
    }

    .pr-sm-md,
  .px-sm-md {
        padding-right: 2rem !important;
    }

    .pb-sm-md,
  .py-sm-md {
        padding-bottom: 2rem !important;
    }

    .pl-sm-md,
  .px-sm-md {
        padding-left: 2rem !important;
    }

    .p-sm-lg {
        padding: 4rem !important;
    }

    .pt-sm-lg,
  .py-sm-lg {
        padding-top: 4rem !important;
    }

    .pr-sm-lg,
  .px-sm-lg {
        padding-right: 4rem !important;
    }

    .pb-sm-lg,
  .py-sm-lg {
        padding-bottom: 4rem !important;
    }

    .pl-sm-lg,
  .px-sm-lg {
        padding-left: 4rem !important;
    }

    .p-sm-xl {
        padding: 8rem !important;
    }

    .pt-sm-xl,
  .py-sm-xl {
        padding-top: 8rem !important;
    }

    .pr-sm-xl,
  .px-sm-xl {
        padding-right: 8rem !important;
    }

    .pb-sm-xl,
  .py-sm-xl {
        padding-bottom: 8rem !important;
    }

    .pl-sm-xl,
  .px-sm-xl {
        padding-left: 8rem !important;
    }

    .m-sm-n1 {
        margin: -0.25rem !important;
    }

    .mt-sm-n1,
  .my-sm-n1 {
        margin-top: -0.25rem !important;
    }

    .mr-sm-n1,
  .mx-sm-n1 {
        margin-right: -0.25rem !important;
    }

    .mb-sm-n1,
  .my-sm-n1 {
        margin-bottom: -0.25rem !important;
    }

    .ml-sm-n1,
  .mx-sm-n1 {
        margin-left: -0.25rem !important;
    }

    .m-sm-n2 {
        margin: -0.5rem !important;
    }

    .mt-sm-n2,
  .my-sm-n2 {
        margin-top: -0.5rem !important;
    }

    .mr-sm-n2,
  .mx-sm-n2 {
        margin-right: -0.5rem !important;
    }

    .mb-sm-n2,
  .my-sm-n2 {
        margin-bottom: -0.5rem !important;
    }

    .ml-sm-n2,
  .mx-sm-n2 {
        margin-left: -0.5rem !important;
    }

    .m-sm-n3 {
        margin: -1rem !important;
    }

    .mt-sm-n3,
  .my-sm-n3 {
        margin-top: -1rem !important;
    }

    .mr-sm-n3,
  .mx-sm-n3 {
        margin-right: -1rem !important;
    }

    .mb-sm-n3,
  .my-sm-n3 {
        margin-bottom: -1rem !important;
    }

    .ml-sm-n3,
  .mx-sm-n3 {
        margin-left: -1rem !important;
    }

    .m-sm-n4 {
        margin: -1.5rem !important;
    }

    .mt-sm-n4,
  .my-sm-n4 {
        margin-top: -1.5rem !important;
    }

    .mr-sm-n4,
  .mx-sm-n4 {
        margin-right: -1.5rem !important;
    }

    .mb-sm-n4,
  .my-sm-n4 {
        margin-bottom: -1.5rem !important;
    }

    .ml-sm-n4,
  .mx-sm-n4 {
        margin-left: -1.5rem !important;
    }

    .m-sm-n5 {
        margin: -3rem !important;
    }

    .mt-sm-n5,
  .my-sm-n5 {
        margin-top: -3rem !important;
    }

    .mr-sm-n5,
  .mx-sm-n5 {
        margin-right: -3rem !important;
    }

    .mb-sm-n5,
  .my-sm-n5 {
        margin-bottom: -3rem !important;
    }

    .ml-sm-n5,
  .mx-sm-n5 {
        margin-left: -3rem !important;
    }

    .m-sm-n6 {
        margin: -5rem !important;
    }

    .mt-sm-n6,
  .my-sm-n6 {
        margin-top: -5rem !important;
    }

    .mr-sm-n6,
  .mx-sm-n6 {
        margin-right: -5rem !important;
    }

    .mb-sm-n6,
  .my-sm-n6 {
        margin-bottom: -5rem !important;
    }

    .ml-sm-n6,
  .mx-sm-n6 {
        margin-left: -5rem !important;
    }

    .m-sm-n7 {
        margin: -8rem !important;
    }

    .mt-sm-n7,
  .my-sm-n7 {
        margin-top: -8rem !important;
    }

    .mr-sm-n7,
  .mx-sm-n7 {
        margin-right: -8rem !important;
    }

    .mb-sm-n7,
  .my-sm-n7 {
        margin-bottom: -8rem !important;
    }

    .ml-sm-n7,
  .mx-sm-n7 {
        margin-left: -8rem !important;
    }

    .m-sm-n8 {
        margin: -10rem !important;
    }

    .mt-sm-n8,
  .my-sm-n8 {
        margin-top: -10rem !important;
    }

    .mr-sm-n8,
  .mx-sm-n8 {
        margin-right: -10rem !important;
    }

    .mb-sm-n8,
  .my-sm-n8 {
        margin-bottom: -10rem !important;
    }

    .ml-sm-n8,
  .mx-sm-n8 {
        margin-left: -10rem !important;
    }

    .m-sm-n9 {
        margin: -11rem !important;
    }

    .mt-sm-n9,
  .my-sm-n9 {
        margin-top: -11rem !important;
    }

    .mr-sm-n9,
  .mx-sm-n9 {
        margin-right: -11rem !important;
    }

    .mb-sm-n9,
  .my-sm-n9 {
        margin-bottom: -11rem !important;
    }

    .ml-sm-n9,
  .mx-sm-n9 {
        margin-left: -11rem !important;
    }

    .m-sm-n10 {
        margin: -15rem !important;
    }

    .mt-sm-n10,
  .my-sm-n10 {
        margin-top: -15rem !important;
    }

    .mr-sm-n10,
  .mx-sm-n10 {
        margin-right: -15rem !important;
    }

    .mb-sm-n10,
  .my-sm-n10 {
        margin-bottom: -15rem !important;
    }

    .ml-sm-n10,
  .mx-sm-n10 {
        margin-left: -15rem !important;
    }

    .m-sm-nsm {
        margin: -1rem !important;
    }

    .mt-sm-nsm,
  .my-sm-nsm {
        margin-top: -1rem !important;
    }

    .mr-sm-nsm,
  .mx-sm-nsm {
        margin-right: -1rem !important;
    }

    .mb-sm-nsm,
  .my-sm-nsm {
        margin-bottom: -1rem !important;
    }

    .ml-sm-nsm,
  .mx-sm-nsm {
        margin-left: -1rem !important;
    }

    .m-sm-nmd {
        margin: -2rem !important;
    }

    .mt-sm-nmd,
  .my-sm-nmd {
        margin-top: -2rem !important;
    }

    .mr-sm-nmd,
  .mx-sm-nmd {
        margin-right: -2rem !important;
    }

    .mb-sm-nmd,
  .my-sm-nmd {
        margin-bottom: -2rem !important;
    }

    .ml-sm-nmd,
  .mx-sm-nmd {
        margin-left: -2rem !important;
    }

    .m-sm-nlg {
        margin: -4rem !important;
    }

    .mt-sm-nlg,
  .my-sm-nlg {
        margin-top: -4rem !important;
    }

    .mr-sm-nlg,
  .mx-sm-nlg {
        margin-right: -4rem !important;
    }

    .mb-sm-nlg,
  .my-sm-nlg {
        margin-bottom: -4rem !important;
    }

    .ml-sm-nlg,
  .mx-sm-nlg {
        margin-left: -4rem !important;
    }

    .m-sm-nxl {
        margin: -8rem !important;
    }

    .mt-sm-nxl,
  .my-sm-nxl {
        margin-top: -8rem !important;
    }

    .mr-sm-nxl,
  .mx-sm-nxl {
        margin-right: -8rem !important;
    }

    .mb-sm-nxl,
  .my-sm-nxl {
        margin-bottom: -8rem !important;
    }

    .ml-sm-nxl,
  .mx-sm-nxl {
        margin-left: -8rem !important;
    }

    .m-sm-auto {
        margin: auto !important;
    }

    .mt-sm-auto,
  .my-sm-auto {
        margin-top: auto !important;
    }

    .mr-sm-auto,
  .mx-sm-auto {
        margin-right: auto !important;
    }

    .mb-sm-auto,
  .my-sm-auto {
        margin-bottom: auto !important;
    }

    .ml-sm-auto,
  .mx-sm-auto {
        margin-left: auto !important;
    }
}

@media (min-width: 768px) {
    .m-md-0 {
        margin: 0 !important;
    }

    .mt-md-0,
  .my-md-0 {
        margin-top: 0 !important;
    }

    .mr-md-0,
  .mx-md-0 {
        margin-right: 0 !important;
    }

    .mb-md-0,
  .my-md-0 {
        margin-bottom: 0 !important;
    }

    .ml-md-0,
  .mx-md-0 {
        margin-left: 0 !important;
    }

    .m-md-1 {
        margin: 0.25rem !important;
    }

    .mt-md-1,
  .my-md-1 {
        margin-top: 0.25rem !important;
    }

    .mr-md-1,
  .mx-md-1 {
        margin-right: 0.25rem !important;
    }

    .mb-md-1,
  .my-md-1 {
        margin-bottom: 0.25rem !important;
    }

    .ml-md-1,
  .mx-md-1 {
        margin-left: 0.25rem !important;
    }

    .m-md-2 {
        margin: 0.5rem !important;
    }

    .mt-md-2,
  .my-md-2 {
        margin-top: 0.5rem !important;
    }

    .mr-md-2,
  .mx-md-2 {
        margin-right: 0.5rem !important;
    }

    .mb-md-2,
  .my-md-2 {
        margin-bottom: 0.5rem !important;
    }

    .ml-md-2,
  .mx-md-2 {
        margin-left: 0.5rem !important;
    }

    .m-md-3 {
        margin: 1rem !important;
    }

    .mt-md-3,
  .my-md-3 {
        margin-top: 1rem !important;
    }

    .mr-md-3,
  .mx-md-3 {
        margin-right: 1rem !important;
    }

    .mb-md-3,
  .my-md-3 {
        margin-bottom: 1rem !important;
    }

    .ml-md-3,
  .mx-md-3 {
        margin-left: 1rem !important;
    }

    .m-md-4 {
        margin: 1.5rem !important;
    }

    .mt-md-4,
  .my-md-4 {
        margin-top: 1.5rem !important;
    }

    .mr-md-4,
  .mx-md-4 {
        margin-right: 1.5rem !important;
    }

    .mb-md-4,
  .my-md-4 {
        margin-bottom: 1.5rem !important;
    }

    .ml-md-4,
  .mx-md-4 {
        margin-left: 1.5rem !important;
    }

    .m-md-5 {
        margin: 3rem !important;
    }

    .mt-md-5,
  .my-md-5 {
        margin-top: 3rem !important;
    }

    .mr-md-5,
  .mx-md-5 {
        margin-right: 3rem !important;
    }

    .mb-md-5,
  .my-md-5 {
        margin-bottom: 3rem !important;
    }

    .ml-md-5,
  .mx-md-5 {
        margin-left: 3rem !important;
    }

    .m-md-6 {
        margin: 5rem !important;
    }

    .mt-md-6,
  .my-md-6 {
        margin-top: 5rem !important;
    }

    .mr-md-6,
  .mx-md-6 {
        margin-right: 5rem !important;
    }

    .mb-md-6,
  .my-md-6 {
        margin-bottom: 5rem !important;
    }

    .ml-md-6,
  .mx-md-6 {
        margin-left: 5rem !important;
    }

    .m-md-7 {
        margin: 8rem !important;
    }

    .mt-md-7,
  .my-md-7 {
        margin-top: 8rem !important;
    }

    .mr-md-7,
  .mx-md-7 {
        margin-right: 8rem !important;
    }

    .mb-md-7,
  .my-md-7 {
        margin-bottom: 8rem !important;
    }

    .ml-md-7,
  .mx-md-7 {
        margin-left: 8rem !important;
    }

    .m-md-8 {
        margin: 10rem !important;
    }

    .mt-md-8,
  .my-md-8 {
        margin-top: 10rem !important;
    }

    .mr-md-8,
  .mx-md-8 {
        margin-right: 10rem !important;
    }

    .mb-md-8,
  .my-md-8 {
        margin-bottom: 10rem !important;
    }

    .ml-md-8,
  .mx-md-8 {
        margin-left: 10rem !important;
    }

    .m-md-9 {
        margin: 11rem !important;
    }

    .mt-md-9,
  .my-md-9 {
        margin-top: 11rem !important;
    }

    .mr-md-9,
  .mx-md-9 {
        margin-right: 11rem !important;
    }

    .mb-md-9,
  .my-md-9 {
        margin-bottom: 11rem !important;
    }

    .ml-md-9,
  .mx-md-9 {
        margin-left: 11rem !important;
    }

    .m-md-10 {
        margin: 15rem !important;
    }

    .mt-md-10,
  .my-md-10 {
        margin-top: 15rem !important;
    }

    .mr-md-10,
  .mx-md-10 {
        margin-right: 15rem !important;
    }

    .mb-md-10,
  .my-md-10 {
        margin-bottom: 15rem !important;
    }

    .ml-md-10,
  .mx-md-10 {
        margin-left: 15rem !important;
    }

    .m-md-sm {
        margin: 1rem !important;
    }

    .mt-md-sm,
  .my-md-sm {
        margin-top: 1rem !important;
    }

    .mr-md-sm,
  .mx-md-sm {
        margin-right: 1rem !important;
    }

    .mb-md-sm,
  .my-md-sm {
        margin-bottom: 1rem !important;
    }

    .ml-md-sm,
  .mx-md-sm {
        margin-left: 1rem !important;
    }

    .m-md-md {
        margin: 2rem !important;
    }

    .mt-md-md,
  .my-md-md {
        margin-top: 2rem !important;
    }

    .mr-md-md,
  .mx-md-md {
        margin-right: 2rem !important;
    }

    .mb-md-md,
  .my-md-md {
        margin-bottom: 2rem !important;
    }

    .ml-md-md,
  .mx-md-md {
        margin-left: 2rem !important;
    }

    .m-md-lg {
        margin: 4rem !important;
    }

    .mt-md-lg,
  .my-md-lg {
        margin-top: 4rem !important;
    }

    .mr-md-lg,
  .mx-md-lg {
        margin-right: 4rem !important;
    }

    .mb-md-lg,
  .my-md-lg {
        margin-bottom: 4rem !important;
    }

    .ml-md-lg,
  .mx-md-lg {
        margin-left: 4rem !important;
    }

    .m-md-xl {
        margin: 8rem !important;
    }

    .mt-md-xl,
  .my-md-xl {
        margin-top: 8rem !important;
    }

    .mr-md-xl,
  .mx-md-xl {
        margin-right: 8rem !important;
    }

    .mb-md-xl,
  .my-md-xl {
        margin-bottom: 8rem !important;
    }

    .ml-md-xl,
  .mx-md-xl {
        margin-left: 8rem !important;
    }

    .p-md-0 {
        padding: 0 !important;
    }

    .pt-md-0,
  .py-md-0 {
        padding-top: 0 !important;
    }

    .pr-md-0,
  .px-md-0 {
        padding-right: 0 !important;
    }

    .pb-md-0,
  .py-md-0 {
        padding-bottom: 0 !important;
    }

    .pl-md-0,
  .px-md-0 {
        padding-left: 0 !important;
    }

    .p-md-1 {
        padding: 0.25rem !important;
    }

    .pt-md-1,
  .py-md-1 {
        padding-top: 0.25rem !important;
    }

    .pr-md-1,
  .px-md-1 {
        padding-right: 0.25rem !important;
    }

    .pb-md-1,
  .py-md-1 {
        padding-bottom: 0.25rem !important;
    }

    .pl-md-1,
  .px-md-1 {
        padding-left: 0.25rem !important;
    }

    .p-md-2 {
        padding: 0.5rem !important;
    }

    .pt-md-2,
  .py-md-2 {
        padding-top: 0.5rem !important;
    }

    .pr-md-2,
  .px-md-2 {
        padding-right: 0.5rem !important;
    }

    .pb-md-2,
  .py-md-2 {
        padding-bottom: 0.5rem !important;
    }

    .pl-md-2,
  .px-md-2 {
        padding-left: 0.5rem !important;
    }

    .p-md-3 {
        padding: 1rem !important;
    }

    .pt-md-3,
  .py-md-3 {
        padding-top: 1rem !important;
    }

    .pr-md-3,
  .px-md-3 {
        padding-right: 1rem !important;
    }

    .pb-md-3,
  .py-md-3 {
        padding-bottom: 1rem !important;
    }

    .pl-md-3,
  .px-md-3 {
        padding-left: 1rem !important;
    }

    .p-md-4 {
        padding: 1.5rem !important;
    }

    .pt-md-4,
  .py-md-4 {
        padding-top: 1.5rem !important;
    }

    .pr-md-4,
  .px-md-4 {
        padding-right: 1.5rem !important;
    }

    .pb-md-4,
  .py-md-4 {
        padding-bottom: 1.5rem !important;
    }

    .pl-md-4,
  .px-md-4 {
        padding-left: 1.5rem !important;
    }

    .p-md-5 {
        padding: 3rem !important;
    }

    .pt-md-5,
  .py-md-5 {
        padding-top: 3rem !important;
    }

    .pr-md-5,
  .px-md-5 {
        padding-right: 3rem !important;
    }

    .pb-md-5,
  .py-md-5 {
        padding-bottom: 3rem !important;
    }

    .pl-md-5,
  .px-md-5 {
        padding-left: 3rem !important;
    }

    .p-md-6 {
        padding: 5rem !important;
    }

    .pt-md-6,
  .py-md-6 {
        padding-top: 5rem !important;
    }

    .pr-md-6,
  .px-md-6 {
        padding-right: 5rem !important;
    }

    .pb-md-6,
  .py-md-6 {
        padding-bottom: 5rem !important;
    }

    .pl-md-6,
  .px-md-6 {
        padding-left: 5rem !important;
    }

    .p-md-7 {
        padding: 8rem !important;
    }

    .pt-md-7,
  .py-md-7 {
        padding-top: 8rem !important;
    }

    .pr-md-7,
  .px-md-7 {
        padding-right: 8rem !important;
    }

    .pb-md-7,
  .py-md-7 {
        padding-bottom: 8rem !important;
    }

    .pl-md-7,
  .px-md-7 {
        padding-left: 8rem !important;
    }

    .p-md-8 {
        padding: 10rem !important;
    }

    .pt-md-8,
  .py-md-8 {
        padding-top: 10rem !important;
    }

    .pr-md-8,
  .px-md-8 {
        padding-right: 10rem !important;
    }

    .pb-md-8,
  .py-md-8 {
        padding-bottom: 10rem !important;
    }

    .pl-md-8,
  .px-md-8 {
        padding-left: 10rem !important;
    }

    .p-md-9 {
        padding: 11rem !important;
    }

    .pt-md-9,
  .py-md-9 {
        padding-top: 11rem !important;
    }

    .pr-md-9,
  .px-md-9 {
        padding-right: 11rem !important;
    }

    .pb-md-9,
  .py-md-9 {
        padding-bottom: 11rem !important;
    }

    .pl-md-9,
  .px-md-9 {
        padding-left: 11rem !important;
    }

    .p-md-10 {
        padding: 15rem !important;
    }

    .pt-md-10,
  .py-md-10 {
        padding-top: 15rem !important;
    }

    .pr-md-10,
  .px-md-10 {
        padding-right: 15rem !important;
    }

    .pb-md-10,
  .py-md-10 {
        padding-bottom: 15rem !important;
    }

    .pl-md-10,
  .px-md-10 {
        padding-left: 15rem !important;
    }

    .p-md-sm {
        padding: 1rem !important;
    }

    .pt-md-sm,
  .py-md-sm {
        padding-top: 1rem !important;
    }

    .pr-md-sm,
  .px-md-sm {
        padding-right: 1rem !important;
    }

    .pb-md-sm,
  .py-md-sm {
        padding-bottom: 1rem !important;
    }

    .pl-md-sm,
  .px-md-sm {
        padding-left: 1rem !important;
    }

    .p-md-md {
        padding: 2rem !important;
    }

    .pt-md-md,
  .py-md-md {
        padding-top: 2rem !important;
    }

    .pr-md-md,
  .px-md-md {
        padding-right: 2rem !important;
    }

    .pb-md-md,
  .py-md-md {
        padding-bottom: 2rem !important;
    }

    .pl-md-md,
  .px-md-md {
        padding-left: 2rem !important;
    }

    .p-md-lg {
        padding: 4rem !important;
    }

    .pt-md-lg,
  .py-md-lg {
        padding-top: 4rem !important;
    }

    .pr-md-lg,
  .px-md-lg {
        padding-right: 4rem !important;
    }

    .pb-md-lg,
  .py-md-lg {
        padding-bottom: 4rem !important;
    }

    .pl-md-lg,
  .px-md-lg {
        padding-left: 4rem !important;
    }

    .p-md-xl {
        padding: 8rem !important;
    }

    .pt-md-xl,
  .py-md-xl {
        padding-top: 8rem !important;
    }

    .pr-md-xl,
  .px-md-xl {
        padding-right: 8rem !important;
    }

    .pb-md-xl,
  .py-md-xl {
        padding-bottom: 8rem !important;
    }

    .pl-md-xl,
  .px-md-xl {
        padding-left: 8rem !important;
    }

    .m-md-n1 {
        margin: -0.25rem !important;
    }

    .mt-md-n1,
  .my-md-n1 {
        margin-top: -0.25rem !important;
    }

    .mr-md-n1,
  .mx-md-n1 {
        margin-right: -0.25rem !important;
    }

    .mb-md-n1,
  .my-md-n1 {
        margin-bottom: -0.25rem !important;
    }

    .ml-md-n1,
  .mx-md-n1 {
        margin-left: -0.25rem !important;
    }

    .m-md-n2 {
        margin: -0.5rem !important;
    }

    .mt-md-n2,
  .my-md-n2 {
        margin-top: -0.5rem !important;
    }

    .mr-md-n2,
  .mx-md-n2 {
        margin-right: -0.5rem !important;
    }

    .mb-md-n2,
  .my-md-n2 {
        margin-bottom: -0.5rem !important;
    }

    .ml-md-n2,
  .mx-md-n2 {
        margin-left: -0.5rem !important;
    }

    .m-md-n3 {
        margin: -1rem !important;
    }

    .mt-md-n3,
  .my-md-n3 {
        margin-top: -1rem !important;
    }

    .mr-md-n3,
  .mx-md-n3 {
        margin-right: -1rem !important;
    }

    .mb-md-n3,
  .my-md-n3 {
        margin-bottom: -1rem !important;
    }

    .ml-md-n3,
  .mx-md-n3 {
        margin-left: -1rem !important;
    }

    .m-md-n4 {
        margin: -1.5rem !important;
    }

    .mt-md-n4,
  .my-md-n4 {
        margin-top: -1.5rem !important;
    }

    .mr-md-n4,
  .mx-md-n4 {
        margin-right: -1.5rem !important;
    }

    .mb-md-n4,
  .my-md-n4 {
        margin-bottom: -1.5rem !important;
    }

    .ml-md-n4,
  .mx-md-n4 {
        margin-left: -1.5rem !important;
    }

    .m-md-n5 {
        margin: -3rem !important;
    }

    .mt-md-n5,
  .my-md-n5 {
        margin-top: -3rem !important;
    }

    .mr-md-n5,
  .mx-md-n5 {
        margin-right: -3rem !important;
    }

    .mb-md-n5,
  .my-md-n5 {
        margin-bottom: -3rem !important;
    }

    .ml-md-n5,
  .mx-md-n5 {
        margin-left: -3rem !important;
    }

    .m-md-n6 {
        margin: -5rem !important;
    }

    .mt-md-n6,
  .my-md-n6 {
        margin-top: -5rem !important;
    }

    .mr-md-n6,
  .mx-md-n6 {
        margin-right: -5rem !important;
    }

    .mb-md-n6,
  .my-md-n6 {
        margin-bottom: -5rem !important;
    }

    .ml-md-n6,
  .mx-md-n6 {
        margin-left: -5rem !important;
    }

    .m-md-n7 {
        margin: -8rem !important;
    }

    .mt-md-n7,
  .my-md-n7 {
        margin-top: -8rem !important;
    }

    .mr-md-n7,
  .mx-md-n7 {
        margin-right: -8rem !important;
    }

    .mb-md-n7,
  .my-md-n7 {
        margin-bottom: -8rem !important;
    }

    .ml-md-n7,
  .mx-md-n7 {
        margin-left: -8rem !important;
    }

    .m-md-n8 {
        margin: -10rem !important;
    }

    .mt-md-n8,
  .my-md-n8 {
        margin-top: -10rem !important;
    }

    .mr-md-n8,
  .mx-md-n8 {
        margin-right: -10rem !important;
    }

    .mb-md-n8,
  .my-md-n8 {
        margin-bottom: -10rem !important;
    }

    .ml-md-n8,
  .mx-md-n8 {
        margin-left: -10rem !important;
    }

    .m-md-n9 {
        margin: -11rem !important;
    }

    .mt-md-n9,
  .my-md-n9 {
        margin-top: -11rem !important;
    }

    .mr-md-n9,
  .mx-md-n9 {
        margin-right: -11rem !important;
    }

    .mb-md-n9,
  .my-md-n9 {
        margin-bottom: -11rem !important;
    }

    .ml-md-n9,
  .mx-md-n9 {
        margin-left: -11rem !important;
    }

    .m-md-n10 {
        margin: -15rem !important;
    }

    .mt-md-n10,
  .my-md-n10 {
        margin-top: -15rem !important;
    }

    .mr-md-n10,
  .mx-md-n10 {
        margin-right: -15rem !important;
    }

    .mb-md-n10,
  .my-md-n10 {
        margin-bottom: -15rem !important;
    }

    .ml-md-n10,
  .mx-md-n10 {
        margin-left: -15rem !important;
    }

    .m-md-nsm {
        margin: -1rem !important;
    }

    .mt-md-nsm,
  .my-md-nsm {
        margin-top: -1rem !important;
    }

    .mr-md-nsm,
  .mx-md-nsm {
        margin-right: -1rem !important;
    }

    .mb-md-nsm,
  .my-md-nsm {
        margin-bottom: -1rem !important;
    }

    .ml-md-nsm,
  .mx-md-nsm {
        margin-left: -1rem !important;
    }

    .m-md-nmd {
        margin: -2rem !important;
    }

    .mt-md-nmd,
  .my-md-nmd {
        margin-top: -2rem !important;
    }

    .mr-md-nmd,
  .mx-md-nmd {
        margin-right: -2rem !important;
    }

    .mb-md-nmd,
  .my-md-nmd {
        margin-bottom: -2rem !important;
    }

    .ml-md-nmd,
  .mx-md-nmd {
        margin-left: -2rem !important;
    }

    .m-md-nlg {
        margin: -4rem !important;
    }

    .mt-md-nlg,
  .my-md-nlg {
        margin-top: -4rem !important;
    }

    .mr-md-nlg,
  .mx-md-nlg {
        margin-right: -4rem !important;
    }

    .mb-md-nlg,
  .my-md-nlg {
        margin-bottom: -4rem !important;
    }

    .ml-md-nlg,
  .mx-md-nlg {
        margin-left: -4rem !important;
    }

    .m-md-nxl {
        margin: -8rem !important;
    }

    .mt-md-nxl,
  .my-md-nxl {
        margin-top: -8rem !important;
    }

    .mr-md-nxl,
  .mx-md-nxl {
        margin-right: -8rem !important;
    }

    .mb-md-nxl,
  .my-md-nxl {
        margin-bottom: -8rem !important;
    }

    .ml-md-nxl,
  .mx-md-nxl {
        margin-left: -8rem !important;
    }

    .m-md-auto {
        margin: auto !important;
    }

    .mt-md-auto,
  .my-md-auto {
        margin-top: auto !important;
    }

    .mr-md-auto,
  .mx-md-auto {
        margin-right: auto !important;
    }

    .mb-md-auto,
  .my-md-auto {
        margin-bottom: auto !important;
    }

    .ml-md-auto,
  .mx-md-auto {
        margin-left: auto !important;
    }
}

@media (min-width: 992px) {
    .m-lg-0 {
        margin: 0 !important;
    }

    .mt-lg-0,
  .my-lg-0 {
        margin-top: 0 !important;
    }

    .mr-lg-0,
  .mx-lg-0 {
        margin-right: 0 !important;
    }

    .mb-lg-0,
  .my-lg-0 {
        margin-bottom: 0 !important;
    }

    .ml-lg-0,
  .mx-lg-0 {
        margin-left: 0 !important;
    }

    .m-lg-1 {
        margin: 0.25rem !important;
    }

    .mt-lg-1,
  .my-lg-1 {
        margin-top: 0.25rem !important;
    }

    .mr-lg-1,
  .mx-lg-1 {
        margin-right: 0.25rem !important;
    }

    .mb-lg-1,
  .my-lg-1 {
        margin-bottom: 0.25rem !important;
    }

    .ml-lg-1,
  .mx-lg-1 {
        margin-left: 0.25rem !important;
    }

    .m-lg-2 {
        margin: 0.5rem !important;
    }

    .mt-lg-2,
  .my-lg-2 {
        margin-top: 0.5rem !important;
    }

    .mr-lg-2,
  .mx-lg-2 {
        margin-right: 0.5rem !important;
    }

    .mb-lg-2,
  .my-lg-2 {
        margin-bottom: 0.5rem !important;
    }

    .ml-lg-2,
  .mx-lg-2 {
        margin-left: 0.5rem !important;
    }

    .m-lg-3 {
        margin: 1rem !important;
    }

    .mt-lg-3,
  .my-lg-3 {
        margin-top: 1rem !important;
    }

    .mr-lg-3,
  .mx-lg-3 {
        margin-right: 1rem !important;
    }

    .mb-lg-3,
  .my-lg-3 {
        margin-bottom: 1rem !important;
    }

    .ml-lg-3,
  .mx-lg-3 {
        margin-left: 1rem !important;
    }

    .m-lg-4 {
        margin: 1.5rem !important;
    }

    .mt-lg-4,
  .my-lg-4 {
        margin-top: 1.5rem !important;
    }

    .mr-lg-4,
  .mx-lg-4 {
        margin-right: 1.5rem !important;
    }

    .mb-lg-4,
  .my-lg-4 {
        margin-bottom: 1.5rem !important;
    }

    .ml-lg-4,
  .mx-lg-4 {
        margin-left: 1.5rem !important;
    }

    .m-lg-5 {
        margin: 3rem !important;
    }

    .mt-lg-5,
  .my-lg-5 {
        margin-top: 3rem !important;
    }

    .mr-lg-5,
  .mx-lg-5 {
        margin-right: 3rem !important;
    }

    .mb-lg-5,
  .my-lg-5 {
        margin-bottom: 3rem !important;
    }

    .ml-lg-5,
  .mx-lg-5 {
        margin-left: 3rem !important;
    }

    .m-lg-6 {
        margin: 5rem !important;
    }

    .mt-lg-6,
  .my-lg-6 {
        margin-top: 5rem !important;
    }

    .mr-lg-6,
  .mx-lg-6 {
        margin-right: 5rem !important;
    }

    .mb-lg-6,
  .my-lg-6 {
        margin-bottom: 5rem !important;
    }

    .ml-lg-6,
  .mx-lg-6 {
        margin-left: 5rem !important;
    }

    .m-lg-7 {
        margin: 8rem !important;
    }

    .mt-lg-7,
  .my-lg-7 {
        margin-top: 8rem !important;
    }

    .mr-lg-7,
  .mx-lg-7 {
        margin-right: 8rem !important;
    }

    .mb-lg-7,
  .my-lg-7 {
        margin-bottom: 8rem !important;
    }

    .ml-lg-7,
  .mx-lg-7 {
        margin-left: 8rem !important;
    }

    .m-lg-8 {
        margin: 10rem !important;
    }

    .mt-lg-8,
  .my-lg-8 {
        margin-top: 10rem !important;
    }

    .mr-lg-8,
  .mx-lg-8 {
        margin-right: 10rem !important;
    }

    .mb-lg-8,
  .my-lg-8 {
        margin-bottom: 10rem !important;
    }

    .ml-lg-8,
  .mx-lg-8 {
        margin-left: 10rem !important;
    }

    .m-lg-9 {
        margin: 11rem !important;
    }

    .mt-lg-9,
  .my-lg-9 {
        margin-top: 11rem !important;
    }

    .mr-lg-9,
  .mx-lg-9 {
        margin-right: 11rem !important;
    }

    .mb-lg-9,
  .my-lg-9 {
        margin-bottom: 11rem !important;
    }

    .ml-lg-9,
  .mx-lg-9 {
        margin-left: 11rem !important;
    }

    .m-lg-10 {
        margin: 15rem !important;
    }

    .mt-lg-10,
  .my-lg-10 {
        margin-top: 15rem !important;
    }

    .mr-lg-10,
  .mx-lg-10 {
        margin-right: 15rem !important;
    }

    .mb-lg-10,
  .my-lg-10 {
        margin-bottom: 15rem !important;
    }

    .ml-lg-10,
  .mx-lg-10 {
        margin-left: 15rem !important;
    }

    .m-lg-sm {
        margin: 1rem !important;
    }

    .mt-lg-sm,
  .my-lg-sm {
        margin-top: 1rem !important;
    }

    .mr-lg-sm,
  .mx-lg-sm {
        margin-right: 1rem !important;
    }

    .mb-lg-sm,
  .my-lg-sm {
        margin-bottom: 1rem !important;
    }

    .ml-lg-sm,
  .mx-lg-sm {
        margin-left: 1rem !important;
    }

    .m-lg-md {
        margin: 2rem !important;
    }

    .mt-lg-md,
  .my-lg-md {
        margin-top: 2rem !important;
    }

    .mr-lg-md,
  .mx-lg-md {
        margin-right: 2rem !important;
    }

    .mb-lg-md,
  .my-lg-md {
        margin-bottom: 2rem !important;
    }

    .ml-lg-md,
  .mx-lg-md {
        margin-left: 2rem !important;
    }

    .m-lg-lg {
        margin: 4rem !important;
    }

    .mt-lg-lg,
  .my-lg-lg {
        margin-top: 4rem !important;
    }

    .mr-lg-lg,
  .mx-lg-lg {
        margin-right: 4rem !important;
    }

    .mb-lg-lg,
  .my-lg-lg {
        margin-bottom: 4rem !important;
    }

    .ml-lg-lg,
  .mx-lg-lg {
        margin-left: 4rem !important;
    }

    .m-lg-xl {
        margin: 8rem !important;
    }

    .mt-lg-xl,
  .my-lg-xl {
        margin-top: 8rem !important;
    }

    .mr-lg-xl,
  .mx-lg-xl {
        margin-right: 8rem !important;
    }

    .mb-lg-xl,
  .my-lg-xl {
        margin-bottom: 8rem !important;
    }

    .ml-lg-xl,
  .mx-lg-xl {
        margin-left: 8rem !important;
    }

    .p-lg-0 {
        padding: 0 !important;
    }

    .pt-lg-0,
  .py-lg-0 {
        padding-top: 0 !important;
    }

    .pr-lg-0,
  .px-lg-0 {
        padding-right: 0 !important;
    }

    .pb-lg-0,
  .py-lg-0 {
        padding-bottom: 0 !important;
    }

    .pl-lg-0,
  .px-lg-0 {
        padding-left: 0 !important;
    }

    .p-lg-1 {
        padding: 0.25rem !important;
    }

    .pt-lg-1,
  .py-lg-1 {
        padding-top: 0.25rem !important;
    }

    .pr-lg-1,
  .px-lg-1 {
        padding-right: 0.25rem !important;
    }

    .pb-lg-1,
  .py-lg-1 {
        padding-bottom: 0.25rem !important;
    }

    .pl-lg-1,
  .px-lg-1 {
        padding-left: 0.25rem !important;
    }

    .p-lg-2 {
        padding: 0.5rem !important;
    }

    .pt-lg-2,
  .py-lg-2 {
        padding-top: 0.5rem !important;
    }

    .pr-lg-2,
  .px-lg-2 {
        padding-right: 0.5rem !important;
    }

    .pb-lg-2,
  .py-lg-2 {
        padding-bottom: 0.5rem !important;
    }

    .pl-lg-2,
  .px-lg-2 {
        padding-left: 0.5rem !important;
    }

    .p-lg-3 {
        padding: 1rem !important;
    }

    .pt-lg-3,
  .py-lg-3 {
        padding-top: 1rem !important;
    }

    .pr-lg-3,
  .px-lg-3 {
        padding-right: 1rem !important;
    }

    .pb-lg-3,
  .py-lg-3 {
        padding-bottom: 1rem !important;
    }

    .pl-lg-3,
  .px-lg-3 {
        padding-left: 1rem !important;
    }

    .p-lg-4 {
        padding: 1.5rem !important;
    }

    .pt-lg-4,
  .py-lg-4 {
        padding-top: 1.5rem !important;
    }

    .pr-lg-4,
  .px-lg-4 {
        padding-right: 1.5rem !important;
    }

    .pb-lg-4,
  .py-lg-4 {
        padding-bottom: 1.5rem !important;
    }

    .pl-lg-4,
  .px-lg-4 {
        padding-left: 1.5rem !important;
    }

    .p-lg-5 {
        padding: 3rem !important;
    }

    .pt-lg-5,
  .py-lg-5 {
        padding-top: 3rem !important;
    }

    .pr-lg-5,
  .px-lg-5 {
        padding-right: 3rem !important;
    }

    .pb-lg-5,
  .py-lg-5 {
        padding-bottom: 3rem !important;
    }

    .pl-lg-5,
  .px-lg-5 {
        padding-left: 3rem !important;
    }

    .p-lg-6 {
        padding: 5rem !important;
    }

    .pt-lg-6,
  .py-lg-6 {
        padding-top: 5rem !important;
    }

    .pr-lg-6,
  .px-lg-6 {
        padding-right: 5rem !important;
    }

    .pb-lg-6,
  .py-lg-6 {
        padding-bottom: 5rem !important;
    }

    .pl-lg-6,
  .px-lg-6 {
        padding-left: 5rem !important;
    }

    .p-lg-7 {
        padding: 8rem !important;
    }

    .pt-lg-7,
  .py-lg-7 {
        padding-top: 8rem !important;
    }

    .pr-lg-7,
  .px-lg-7 {
        padding-right: 8rem !important;
    }

    .pb-lg-7,
  .py-lg-7 {
        padding-bottom: 8rem !important;
    }

    .pl-lg-7,
  .px-lg-7 {
        padding-left: 8rem !important;
    }

    .p-lg-8 {
        padding: 10rem !important;
    }

    .pt-lg-8,
  .py-lg-8 {
        padding-top: 10rem !important;
    }

    .pr-lg-8,
  .px-lg-8 {
        padding-right: 10rem !important;
    }

    .pb-lg-8,
  .py-lg-8 {
        padding-bottom: 10rem !important;
    }

    .pl-lg-8,
  .px-lg-8 {
        padding-left: 10rem !important;
    }

    .p-lg-9 {
        padding: 11rem !important;
    }

    .pt-lg-9,
  .py-lg-9 {
        padding-top: 11rem !important;
    }

    .pr-lg-9,
  .px-lg-9 {
        padding-right: 11rem !important;
    }

    .pb-lg-9,
  .py-lg-9 {
        padding-bottom: 11rem !important;
    }

    .pl-lg-9,
  .px-lg-9 {
        padding-left: 11rem !important;
    }

    .p-lg-10 {
        padding: 15rem !important;
    }

    .pt-lg-10,
  .py-lg-10 {
        padding-top: 15rem !important;
    }

    .pr-lg-10,
  .px-lg-10 {
        padding-right: 15rem !important;
    }

    .pb-lg-10,
  .py-lg-10 {
        padding-bottom: 15rem !important;
    }

    .pl-lg-10,
  .px-lg-10 {
        padding-left: 15rem !important;
    }

    .p-lg-sm {
        padding: 1rem !important;
    }

    .pt-lg-sm,
  .py-lg-sm {
        padding-top: 1rem !important;
    }

    .pr-lg-sm,
  .px-lg-sm {
        padding-right: 1rem !important;
    }

    .pb-lg-sm,
  .py-lg-sm {
        padding-bottom: 1rem !important;
    }

    .pl-lg-sm,
  .px-lg-sm {
        padding-left: 1rem !important;
    }

    .p-lg-md {
        padding: 2rem !important;
    }

    .pt-lg-md,
  .py-lg-md {
        padding-top: 2rem !important;
    }

    .pr-lg-md,
  .px-lg-md {
        padding-right: 2rem !important;
    }

    .pb-lg-md,
  .py-lg-md {
        padding-bottom: 2rem !important;
    }

    .pl-lg-md,
  .px-lg-md {
        padding-left: 2rem !important;
    }

    .p-lg-lg {
        padding: 4rem !important;
    }

    .pt-lg-lg,
  .py-lg-lg {
        padding-top: 4rem !important;
    }

    .pr-lg-lg,
  .px-lg-lg {
        padding-right: 4rem !important;
    }

    .pb-lg-lg,
  .py-lg-lg {
        padding-bottom: 4rem !important;
    }

    .pl-lg-lg,
  .px-lg-lg {
        padding-left: 4rem !important;
    }

    .p-lg-xl {
        padding: 8rem !important;
    }

    .pt-lg-xl,
  .py-lg-xl {
        padding-top: 8rem !important;
    }

    .pr-lg-xl,
  .px-lg-xl {
        padding-right: 8rem !important;
    }

    .pb-lg-xl,
  .py-lg-xl {
        padding-bottom: 8rem !important;
    }

    .pl-lg-xl,
  .px-lg-xl {
        padding-left: 8rem !important;
    }

    .m-lg-n1 {
        margin: -0.25rem !important;
    }

    .mt-lg-n1,
  .my-lg-n1 {
        margin-top: -0.25rem !important;
    }

    .mr-lg-n1,
  .mx-lg-n1 {
        margin-right: -0.25rem !important;
    }

    .mb-lg-n1,
  .my-lg-n1 {
        margin-bottom: -0.25rem !important;
    }

    .ml-lg-n1,
  .mx-lg-n1 {
        margin-left: -0.25rem !important;
    }

    .m-lg-n2 {
        margin: -0.5rem !important;
    }

    .mt-lg-n2,
  .my-lg-n2 {
        margin-top: -0.5rem !important;
    }

    .mr-lg-n2,
  .mx-lg-n2 {
        margin-right: -0.5rem !important;
    }

    .mb-lg-n2,
  .my-lg-n2 {
        margin-bottom: -0.5rem !important;
    }

    .ml-lg-n2,
  .mx-lg-n2 {
        margin-left: -0.5rem !important;
    }

    .m-lg-n3 {
        margin: -1rem !important;
    }

    .mt-lg-n3,
  .my-lg-n3 {
        margin-top: -1rem !important;
    }

    .mr-lg-n3,
  .mx-lg-n3 {
        margin-right: -1rem !important;
    }

    .mb-lg-n3,
  .my-lg-n3 {
        margin-bottom: -1rem !important;
    }

    .ml-lg-n3,
  .mx-lg-n3 {
        margin-left: -1rem !important;
    }

    .m-lg-n4 {
        margin: -1.5rem !important;
    }

    .mt-lg-n4,
  .my-lg-n4 {
        margin-top: -1.5rem !important;
    }

    .mr-lg-n4,
  .mx-lg-n4 {
        margin-right: -1.5rem !important;
    }

    .mb-lg-n4,
  .my-lg-n4 {
        margin-bottom: -1.5rem !important;
    }

    .ml-lg-n4,
  .mx-lg-n4 {
        margin-left: -1.5rem !important;
    }

    .m-lg-n5 {
        margin: -3rem !important;
    }

    .mt-lg-n5,
  .my-lg-n5 {
        margin-top: -3rem !important;
    }

    .mr-lg-n5,
  .mx-lg-n5 {
        margin-right: -3rem !important;
    }

    .mb-lg-n5,
  .my-lg-n5 {
        margin-bottom: -3rem !important;
    }

    .ml-lg-n5,
  .mx-lg-n5 {
        margin-left: -3rem !important;
    }

    .m-lg-n6 {
        margin: -5rem !important;
    }

    .mt-lg-n6,
  .my-lg-n6 {
        margin-top: -5rem !important;
    }

    .mr-lg-n6,
  .mx-lg-n6 {
        margin-right: -5rem !important;
    }

    .mb-lg-n6,
  .my-lg-n6 {
        margin-bottom: -5rem !important;
    }

    .ml-lg-n6,
  .mx-lg-n6 {
        margin-left: -5rem !important;
    }

    .m-lg-n7 {
        margin: -8rem !important;
    }

    .mt-lg-n7,
  .my-lg-n7 {
        margin-top: -8rem !important;
    }

    .mr-lg-n7,
  .mx-lg-n7 {
        margin-right: -8rem !important;
    }

    .mb-lg-n7,
  .my-lg-n7 {
        margin-bottom: -8rem !important;
    }

    .ml-lg-n7,
  .mx-lg-n7 {
        margin-left: -8rem !important;
    }

    .m-lg-n8 {
        margin: -10rem !important;
    }

    .mt-lg-n8,
  .my-lg-n8 {
        margin-top: -10rem !important;
    }

    .mr-lg-n8,
  .mx-lg-n8 {
        margin-right: -10rem !important;
    }

    .mb-lg-n8,
  .my-lg-n8 {
        margin-bottom: -10rem !important;
    }

    .ml-lg-n8,
  .mx-lg-n8 {
        margin-left: -10rem !important;
    }

    .m-lg-n9 {
        margin: -11rem !important;
    }

    .mt-lg-n9,
  .my-lg-n9 {
        margin-top: -11rem !important;
    }

    .mr-lg-n9,
  .mx-lg-n9 {
        margin-right: -11rem !important;
    }

    .mb-lg-n9,
  .my-lg-n9 {
        margin-bottom: -11rem !important;
    }

    .ml-lg-n9,
  .mx-lg-n9 {
        margin-left: -11rem !important;
    }

    .m-lg-n10 {
        margin: -15rem !important;
    }

    .mt-lg-n10,
  .my-lg-n10 {
        margin-top: -15rem !important;
    }

    .mr-lg-n10,
  .mx-lg-n10 {
        margin-right: -15rem !important;
    }

    .mb-lg-n10,
  .my-lg-n10 {
        margin-bottom: -15rem !important;
    }

    .ml-lg-n10,
  .mx-lg-n10 {
        margin-left: -15rem !important;
    }

    .m-lg-nsm {
        margin: -1rem !important;
    }

    .mt-lg-nsm,
  .my-lg-nsm {
        margin-top: -1rem !important;
    }

    .mr-lg-nsm,
  .mx-lg-nsm {
        margin-right: -1rem !important;
    }

    .mb-lg-nsm,
  .my-lg-nsm {
        margin-bottom: -1rem !important;
    }

    .ml-lg-nsm,
  .mx-lg-nsm {
        margin-left: -1rem !important;
    }

    .m-lg-nmd {
        margin: -2rem !important;
    }

    .mt-lg-nmd,
  .my-lg-nmd {
        margin-top: -2rem !important;
    }

    .mr-lg-nmd,
  .mx-lg-nmd {
        margin-right: -2rem !important;
    }

    .mb-lg-nmd,
  .my-lg-nmd {
        margin-bottom: -2rem !important;
    }

    .ml-lg-nmd,
  .mx-lg-nmd {
        margin-left: -2rem !important;
    }

    .m-lg-nlg {
        margin: -4rem !important;
    }

    .mt-lg-nlg,
  .my-lg-nlg {
        margin-top: -4rem !important;
    }

    .mr-lg-nlg,
  .mx-lg-nlg {
        margin-right: -4rem !important;
    }

    .mb-lg-nlg,
  .my-lg-nlg {
        margin-bottom: -4rem !important;
    }

    .ml-lg-nlg,
  .mx-lg-nlg {
        margin-left: -4rem !important;
    }

    .m-lg-nxl {
        margin: -8rem !important;
    }

    .mt-lg-nxl,
  .my-lg-nxl {
        margin-top: -8rem !important;
    }

    .mr-lg-nxl,
  .mx-lg-nxl {
        margin-right: -8rem !important;
    }

    .mb-lg-nxl,
  .my-lg-nxl {
        margin-bottom: -8rem !important;
    }

    .ml-lg-nxl,
  .mx-lg-nxl {
        margin-left: -8rem !important;
    }

    .m-lg-auto {
        margin: auto !important;
    }

    .mt-lg-auto,
  .my-lg-auto {
        margin-top: auto !important;
    }

    .mr-lg-auto,
  .mx-lg-auto {
        margin-right: auto !important;
    }

    .mb-lg-auto,
  .my-lg-auto {
        margin-bottom: auto !important;
    }

    .ml-lg-auto,
  .mx-lg-auto {
        margin-left: auto !important;
    }
}

@media (min-width: 1200px) {
    .m-xl-0 {
        margin: 0 !important;
    }

    .mt-xl-0,
  .my-xl-0 {
        margin-top: 0 !important;
    }

    .mr-xl-0,
  .mx-xl-0 {
        margin-right: 0 !important;
    }

    .mb-xl-0,
  .my-xl-0 {
        margin-bottom: 0 !important;
    }

    .ml-xl-0,
  .mx-xl-0 {
        margin-left: 0 !important;
    }

    .m-xl-1 {
        margin: 0.25rem !important;
    }

    .mt-xl-1,
  .my-xl-1 {
        margin-top: 0.25rem !important;
    }

    .mr-xl-1,
  .mx-xl-1 {
        margin-right: 0.25rem !important;
    }

    .mb-xl-1,
  .my-xl-1 {
        margin-bottom: 0.25rem !important;
    }

    .ml-xl-1,
  .mx-xl-1 {
        margin-left: 0.25rem !important;
    }

    .m-xl-2 {
        margin: 0.5rem !important;
    }

    .mt-xl-2,
  .my-xl-2 {
        margin-top: 0.5rem !important;
    }

    .mr-xl-2,
  .mx-xl-2 {
        margin-right: 0.5rem !important;
    }

    .mb-xl-2,
  .my-xl-2 {
        margin-bottom: 0.5rem !important;
    }

    .ml-xl-2,
  .mx-xl-2 {
        margin-left: 0.5rem !important;
    }

    .m-xl-3 {
        margin: 1rem !important;
    }

    .mt-xl-3,
  .my-xl-3 {
        margin-top: 1rem !important;
    }

    .mr-xl-3,
  .mx-xl-3 {
        margin-right: 1rem !important;
    }

    .mb-xl-3,
  .my-xl-3 {
        margin-bottom: 1rem !important;
    }

    .ml-xl-3,
  .mx-xl-3 {
        margin-left: 1rem !important;
    }

    .m-xl-4 {
        margin: 1.5rem !important;
    }

    .mt-xl-4,
  .my-xl-4 {
        margin-top: 1.5rem !important;
    }

    .mr-xl-4,
  .mx-xl-4 {
        margin-right: 1.5rem !important;
    }

    .mb-xl-4,
  .my-xl-4 {
        margin-bottom: 1.5rem !important;
    }

    .ml-xl-4,
  .mx-xl-4 {
        margin-left: 1.5rem !important;
    }

    .m-xl-5 {
        margin: 3rem !important;
    }

    .mt-xl-5,
  .my-xl-5 {
        margin-top: 3rem !important;
    }

    .mr-xl-5,
  .mx-xl-5 {
        margin-right: 3rem !important;
    }

    .mb-xl-5,
  .my-xl-5 {
        margin-bottom: 3rem !important;
    }

    .ml-xl-5,
  .mx-xl-5 {
        margin-left: 3rem !important;
    }

    .m-xl-6 {
        margin: 5rem !important;
    }

    .mt-xl-6,
  .my-xl-6 {
        margin-top: 5rem !important;
    }

    .mr-xl-6,
  .mx-xl-6 {
        margin-right: 5rem !important;
    }

    .mb-xl-6,
  .my-xl-6 {
        margin-bottom: 5rem !important;
    }

    .ml-xl-6,
  .mx-xl-6 {
        margin-left: 5rem !important;
    }

    .m-xl-7 {
        margin: 8rem !important;
    }

    .mt-xl-7,
  .my-xl-7 {
        margin-top: 8rem !important;
    }

    .mr-xl-7,
  .mx-xl-7 {
        margin-right: 8rem !important;
    }

    .mb-xl-7,
  .my-xl-7 {
        margin-bottom: 8rem !important;
    }

    .ml-xl-7,
  .mx-xl-7 {
        margin-left: 8rem !important;
    }

    .m-xl-8 {
        margin: 10rem !important;
    }

    .mt-xl-8,
  .my-xl-8 {
        margin-top: 10rem !important;
    }

    .mr-xl-8,
  .mx-xl-8 {
        margin-right: 10rem !important;
    }

    .mb-xl-8,
  .my-xl-8 {
        margin-bottom: 10rem !important;
    }

    .ml-xl-8,
  .mx-xl-8 {
        margin-left: 10rem !important;
    }

    .m-xl-9 {
        margin: 11rem !important;
    }

    .mt-xl-9,
  .my-xl-9 {
        margin-top: 11rem !important;
    }

    .mr-xl-9,
  .mx-xl-9 {
        margin-right: 11rem !important;
    }

    .mb-xl-9,
  .my-xl-9 {
        margin-bottom: 11rem !important;
    }

    .ml-xl-9,
  .mx-xl-9 {
        margin-left: 11rem !important;
    }

    .m-xl-10 {
        margin: 15rem !important;
    }

    .mt-xl-10,
  .my-xl-10 {
        margin-top: 15rem !important;
    }

    .mr-xl-10,
  .mx-xl-10 {
        margin-right: 15rem !important;
    }

    .mb-xl-10,
  .my-xl-10 {
        margin-bottom: 15rem !important;
    }

    .ml-xl-10,
  .mx-xl-10 {
        margin-left: 15rem !important;
    }

    .m-xl-sm {
        margin: 1rem !important;
    }

    .mt-xl-sm,
  .my-xl-sm {
        margin-top: 1rem !important;
    }

    .mr-xl-sm,
  .mx-xl-sm {
        margin-right: 1rem !important;
    }

    .mb-xl-sm,
  .my-xl-sm {
        margin-bottom: 1rem !important;
    }

    .ml-xl-sm,
  .mx-xl-sm {
        margin-left: 1rem !important;
    }

    .m-xl-md {
        margin: 2rem !important;
    }

    .mt-xl-md,
  .my-xl-md {
        margin-top: 2rem !important;
    }

    .mr-xl-md,
  .mx-xl-md {
        margin-right: 2rem !important;
    }

    .mb-xl-md,
  .my-xl-md {
        margin-bottom: 2rem !important;
    }

    .ml-xl-md,
  .mx-xl-md {
        margin-left: 2rem !important;
    }

    .m-xl-lg {
        margin: 4rem !important;
    }

    .mt-xl-lg,
  .my-xl-lg {
        margin-top: 4rem !important;
    }

    .mr-xl-lg,
  .mx-xl-lg {
        margin-right: 4rem !important;
    }

    .mb-xl-lg,
  .my-xl-lg {
        margin-bottom: 4rem !important;
    }

    .ml-xl-lg,
  .mx-xl-lg {
        margin-left: 4rem !important;
    }

    .m-xl-xl {
        margin: 8rem !important;
    }

    .mt-xl-xl,
  .my-xl-xl {
        margin-top: 8rem !important;
    }

    .mr-xl-xl,
  .mx-xl-xl {
        margin-right: 8rem !important;
    }

    .mb-xl-xl,
  .my-xl-xl {
        margin-bottom: 8rem !important;
    }

    .ml-xl-xl,
  .mx-xl-xl {
        margin-left: 8rem !important;
    }

    .p-xl-0 {
        padding: 0 !important;
    }

    .pt-xl-0,
  .py-xl-0 {
        padding-top: 0 !important;
    }

    .pr-xl-0,
  .px-xl-0 {
        padding-right: 0 !important;
    }

    .pb-xl-0,
  .py-xl-0 {
        padding-bottom: 0 !important;
    }

    .pl-xl-0,
  .px-xl-0 {
        padding-left: 0 !important;
    }

    .p-xl-1 {
        padding: 0.25rem !important;
    }

    .pt-xl-1,
  .py-xl-1 {
        padding-top: 0.25rem !important;
    }

    .pr-xl-1,
  .px-xl-1 {
        padding-right: 0.25rem !important;
    }

    .pb-xl-1,
  .py-xl-1 {
        padding-bottom: 0.25rem !important;
    }

    .pl-xl-1,
  .px-xl-1 {
        padding-left: 0.25rem !important;
    }

    .p-xl-2 {
        padding: 0.5rem !important;
    }

    .pt-xl-2,
  .py-xl-2 {
        padding-top: 0.5rem !important;
    }

    .pr-xl-2,
  .px-xl-2 {
        padding-right: 0.5rem !important;
    }

    .pb-xl-2,
  .py-xl-2 {
        padding-bottom: 0.5rem !important;
    }

    .pl-xl-2,
  .px-xl-2 {
        padding-left: 0.5rem !important;
    }

    .p-xl-3 {
        padding: 1rem !important;
    }

    .pt-xl-3,
  .py-xl-3 {
        padding-top: 1rem !important;
    }

    .pr-xl-3,
  .px-xl-3 {
        padding-right: 1rem !important;
    }

    .pb-xl-3,
  .py-xl-3 {
        padding-bottom: 1rem !important;
    }

    .pl-xl-3,
  .px-xl-3 {
        padding-left: 1rem !important;
    }

    .p-xl-4 {
        padding: 1.5rem !important;
    }

    .pt-xl-4,
  .py-xl-4 {
        padding-top: 1.5rem !important;
    }

    .pr-xl-4,
  .px-xl-4 {
        padding-right: 1.5rem !important;
    }

    .pb-xl-4,
  .py-xl-4 {
        padding-bottom: 1.5rem !important;
    }

    .pl-xl-4,
  .px-xl-4 {
        padding-left: 1.5rem !important;
    }

    .p-xl-5 {
        padding: 3rem !important;
    }

    .pt-xl-5,
  .py-xl-5 {
        padding-top: 3rem !important;
    }

    .pr-xl-5,
  .px-xl-5 {
        padding-right: 3rem !important;
    }

    .pb-xl-5,
  .py-xl-5 {
        padding-bottom: 3rem !important;
    }

    .pl-xl-5,
  .px-xl-5 {
        padding-left: 3rem !important;
    }

    .p-xl-6 {
        padding: 5rem !important;
    }

    .pt-xl-6,
  .py-xl-6 {
        padding-top: 5rem !important;
    }

    .pr-xl-6,
  .px-xl-6 {
        padding-right: 5rem !important;
    }

    .pb-xl-6,
  .py-xl-6 {
        padding-bottom: 5rem !important;
    }

    .pl-xl-6,
  .px-xl-6 {
        padding-left: 5rem !important;
    }

    .p-xl-7 {
        padding: 8rem !important;
    }

    .pt-xl-7,
  .py-xl-7 {
        padding-top: 8rem !important;
    }

    .pr-xl-7,
  .px-xl-7 {
        padding-right: 8rem !important;
    }

    .pb-xl-7,
  .py-xl-7 {
        padding-bottom: 8rem !important;
    }

    .pl-xl-7,
  .px-xl-7 {
        padding-left: 8rem !important;
    }

    .p-xl-8 {
        padding: 10rem !important;
    }

    .pt-xl-8,
  .py-xl-8 {
        padding-top: 10rem !important;
    }

    .pr-xl-8,
  .px-xl-8 {
        padding-right: 10rem !important;
    }

    .pb-xl-8,
  .py-xl-8 {
        padding-bottom: 10rem !important;
    }

    .pl-xl-8,
  .px-xl-8 {
        padding-left: 10rem !important;
    }

    .p-xl-9 {
        padding: 11rem !important;
    }

    .pt-xl-9,
  .py-xl-9 {
        padding-top: 11rem !important;
    }

    .pr-xl-9,
  .px-xl-9 {
        padding-right: 11rem !important;
    }

    .pb-xl-9,
  .py-xl-9 {
        padding-bottom: 11rem !important;
    }

    .pl-xl-9,
  .px-xl-9 {
        padding-left: 11rem !important;
    }

    .p-xl-10 {
        padding: 15rem !important;
    }

    .pt-xl-10,
  .py-xl-10 {
        padding-top: 15rem !important;
    }

    .pr-xl-10,
  .px-xl-10 {
        padding-right: 15rem !important;
    }

    .pb-xl-10,
  .py-xl-10 {
        padding-bottom: 15rem !important;
    }

    .pl-xl-10,
  .px-xl-10 {
        padding-left: 15rem !important;
    }

    .p-xl-sm {
        padding: 1rem !important;
    }

    .pt-xl-sm,
  .py-xl-sm {
        padding-top: 1rem !important;
    }

    .pr-xl-sm,
  .px-xl-sm {
        padding-right: 1rem !important;
    }

    .pb-xl-sm,
  .py-xl-sm {
        padding-bottom: 1rem !important;
    }

    .pl-xl-sm,
  .px-xl-sm {
        padding-left: 1rem !important;
    }

    .p-xl-md {
        padding: 2rem !important;
    }

    .pt-xl-md,
  .py-xl-md {
        padding-top: 2rem !important;
    }

    .pr-xl-md,
  .px-xl-md {
        padding-right: 2rem !important;
    }

    .pb-xl-md,
  .py-xl-md {
        padding-bottom: 2rem !important;
    }

    .pl-xl-md,
  .px-xl-md {
        padding-left: 2rem !important;
    }

    .p-xl-lg {
        padding: 4rem !important;
    }

    .pt-xl-lg,
  .py-xl-lg {
        padding-top: 4rem !important;
    }

    .pr-xl-lg,
  .px-xl-lg {
        padding-right: 4rem !important;
    }

    .pb-xl-lg,
  .py-xl-lg {
        padding-bottom: 4rem !important;
    }

    .pl-xl-lg,
  .px-xl-lg {
        padding-left: 4rem !important;
    }

    .p-xl-xl {
        padding: 8rem !important;
    }

    .pt-xl-xl,
  .py-xl-xl {
        padding-top: 8rem !important;
    }

    .pr-xl-xl,
  .px-xl-xl {
        padding-right: 8rem !important;
    }

    .pb-xl-xl,
  .py-xl-xl {
        padding-bottom: 8rem !important;
    }

    .pl-xl-xl,
  .px-xl-xl {
        padding-left: 8rem !important;
    }

    .m-xl-n1 {
        margin: -0.25rem !important;
    }

    .mt-xl-n1,
  .my-xl-n1 {
        margin-top: -0.25rem !important;
    }

    .mr-xl-n1,
  .mx-xl-n1 {
        margin-right: -0.25rem !important;
    }

    .mb-xl-n1,
  .my-xl-n1 {
        margin-bottom: -0.25rem !important;
    }

    .ml-xl-n1,
  .mx-xl-n1 {
        margin-left: -0.25rem !important;
    }

    .m-xl-n2 {
        margin: -0.5rem !important;
    }

    .mt-xl-n2,
  .my-xl-n2 {
        margin-top: -0.5rem !important;
    }

    .mr-xl-n2,
  .mx-xl-n2 {
        margin-right: -0.5rem !important;
    }

    .mb-xl-n2,
  .my-xl-n2 {
        margin-bottom: -0.5rem !important;
    }

    .ml-xl-n2,
  .mx-xl-n2 {
        margin-left: -0.5rem !important;
    }

    .m-xl-n3 {
        margin: -1rem !important;
    }

    .mt-xl-n3,
  .my-xl-n3 {
        margin-top: -1rem !important;
    }

    .mr-xl-n3,
  .mx-xl-n3 {
        margin-right: -1rem !important;
    }

    .mb-xl-n3,
  .my-xl-n3 {
        margin-bottom: -1rem !important;
    }

    .ml-xl-n3,
  .mx-xl-n3 {
        margin-left: -1rem !important;
    }

    .m-xl-n4 {
        margin: -1.5rem !important;
    }

    .mt-xl-n4,
  .my-xl-n4 {
        margin-top: -1.5rem !important;
    }

    .mr-xl-n4,
  .mx-xl-n4 {
        margin-right: -1.5rem !important;
    }

    .mb-xl-n4,
  .my-xl-n4 {
        margin-bottom: -1.5rem !important;
    }

    .ml-xl-n4,
  .mx-xl-n4 {
        margin-left: -1.5rem !important;
    }

    .m-xl-n5 {
        margin: -3rem !important;
    }

    .mt-xl-n5,
  .my-xl-n5 {
        margin-top: -3rem !important;
    }

    .mr-xl-n5,
  .mx-xl-n5 {
        margin-right: -3rem !important;
    }

    .mb-xl-n5,
  .my-xl-n5 {
        margin-bottom: -3rem !important;
    }

    .ml-xl-n5,
  .mx-xl-n5 {
        margin-left: -3rem !important;
    }

    .m-xl-n6 {
        margin: -5rem !important;
    }

    .mt-xl-n6,
  .my-xl-n6 {
        margin-top: -5rem !important;
    }

    .mr-xl-n6,
  .mx-xl-n6 {
        margin-right: -5rem !important;
    }

    .mb-xl-n6,
  .my-xl-n6 {
        margin-bottom: -5rem !important;
    }

    .ml-xl-n6,
  .mx-xl-n6 {
        margin-left: -5rem !important;
    }

    .m-xl-n7 {
        margin: -8rem !important;
    }

    .mt-xl-n7,
  .my-xl-n7 {
        margin-top: -8rem !important;
    }

    .mr-xl-n7,
  .mx-xl-n7 {
        margin-right: -8rem !important;
    }

    .mb-xl-n7,
  .my-xl-n7 {
        margin-bottom: -8rem !important;
    }

    .ml-xl-n7,
  .mx-xl-n7 {
        margin-left: -8rem !important;
    }

    .m-xl-n8 {
        margin: -10rem !important;
    }

    .mt-xl-n8,
  .my-xl-n8 {
        margin-top: -10rem !important;
    }

    .mr-xl-n8,
  .mx-xl-n8 {
        margin-right: -10rem !important;
    }

    .mb-xl-n8,
  .my-xl-n8 {
        margin-bottom: -10rem !important;
    }

    .ml-xl-n8,
  .mx-xl-n8 {
        margin-left: -10rem !important;
    }

    .m-xl-n9 {
        margin: -11rem !important;
    }

    .mt-xl-n9,
  .my-xl-n9 {
        margin-top: -11rem !important;
    }

    .mr-xl-n9,
  .mx-xl-n9 {
        margin-right: -11rem !important;
    }

    .mb-xl-n9,
  .my-xl-n9 {
        margin-bottom: -11rem !important;
    }

    .ml-xl-n9,
  .mx-xl-n9 {
        margin-left: -11rem !important;
    }

    .m-xl-n10 {
        margin: -15rem !important;
    }

    .mt-xl-n10,
  .my-xl-n10 {
        margin-top: -15rem !important;
    }

    .mr-xl-n10,
  .mx-xl-n10 {
        margin-right: -15rem !important;
    }

    .mb-xl-n10,
  .my-xl-n10 {
        margin-bottom: -15rem !important;
    }

    .ml-xl-n10,
  .mx-xl-n10 {
        margin-left: -15rem !important;
    }

    .m-xl-nsm {
        margin: -1rem !important;
    }

    .mt-xl-nsm,
  .my-xl-nsm {
        margin-top: -1rem !important;
    }

    .mr-xl-nsm,
  .mx-xl-nsm {
        margin-right: -1rem !important;
    }

    .mb-xl-nsm,
  .my-xl-nsm {
        margin-bottom: -1rem !important;
    }

    .ml-xl-nsm,
  .mx-xl-nsm {
        margin-left: -1rem !important;
    }

    .m-xl-nmd {
        margin: -2rem !important;
    }

    .mt-xl-nmd,
  .my-xl-nmd {
        margin-top: -2rem !important;
    }

    .mr-xl-nmd,
  .mx-xl-nmd {
        margin-right: -2rem !important;
    }

    .mb-xl-nmd,
  .my-xl-nmd {
        margin-bottom: -2rem !important;
    }

    .ml-xl-nmd,
  .mx-xl-nmd {
        margin-left: -2rem !important;
    }

    .m-xl-nlg {
        margin: -4rem !important;
    }

    .mt-xl-nlg,
  .my-xl-nlg {
        margin-top: -4rem !important;
    }

    .mr-xl-nlg,
  .mx-xl-nlg {
        margin-right: -4rem !important;
    }

    .mb-xl-nlg,
  .my-xl-nlg {
        margin-bottom: -4rem !important;
    }

    .ml-xl-nlg,
  .mx-xl-nlg {
        margin-left: -4rem !important;
    }

    .m-xl-nxl {
        margin: -8rem !important;
    }

    .mt-xl-nxl,
  .my-xl-nxl {
        margin-top: -8rem !important;
    }

    .mr-xl-nxl,
  .mx-xl-nxl {
        margin-right: -8rem !important;
    }

    .mb-xl-nxl,
  .my-xl-nxl {
        margin-bottom: -8rem !important;
    }

    .ml-xl-nxl,
  .mx-xl-nxl {
        margin-left: -8rem !important;
    }

    .m-xl-auto {
        margin: auto !important;
    }

    .mt-xl-auto,
  .my-xl-auto {
        margin-top: auto !important;
    }

    .mr-xl-auto,
  .mx-xl-auto {
        margin-right: auto !important;
    }

    .mb-xl-auto,
  .my-xl-auto {
        margin-bottom: auto !important;
    }

    .ml-xl-auto,
  .mx-xl-auto {
        margin-left: auto !important;
    }
}

.text-monospace {
    font-family: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace !important;
}

.text-justify {
    text-align: justify !important;
}

.text-wrap {
    white-space: normal !important;
}

.text-nowrap {
    white-space: nowrap !important;
}

.text-truncate {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.text-left {
    text-align: left !important;
}

.text-right {
    text-align: right !important;
}

.text-center {
    text-align: center !important;
}

@media (min-width: 576px) {
    .text-sm-left {
        text-align: left !important;
    }

    .text-sm-right {
        text-align: right !important;
    }

    .text-sm-center {
        text-align: center !important;
    }
}

@media (min-width: 768px) {
    .text-md-left {
        text-align: left !important;
    }

    .text-md-right {
        text-align: right !important;
    }

    .text-md-center {
        text-align: center !important;
    }
}

@media (min-width: 992px) {
    .text-lg-left {
        text-align: left !important;
    }

    .text-lg-right {
        text-align: right !important;
    }

    .text-lg-center {
        text-align: center !important;
    }
}

@media (min-width: 1200px) {
    .text-xl-left {
        text-align: left !important;
    }

    .text-xl-right {
        text-align: right !important;
    }

    .text-xl-center {
        text-align: center !important;
    }
}

.text-lowercase {
    text-transform: lowercase !important;
}

.text-uppercase {
    text-transform: uppercase !important;
}

.text-capitalize {
    text-transform: capitalize !important;
}

.font-weight-light {
    font-weight: 300 !important;
}

.font-weight-lighter {
    font-weight: lighter !important;
}

.font-weight-normal {
    font-weight: 400 !important;
}

.font-weight-bold {
    font-weight: 600 !important;
}

.font-weight-bolder {
    font-weight: 700 !important;
}

.font-italic {
    font-style: italic !important;
}

.text-primary {
    color: #e6e7ee !important;
}

a.text-primary:hover, a.text-primary:focus {
    color: #b8bbcf !important;
}

.text-secondary {
    color: #2D4CC8 !important;
}

a.text-secondary:hover, a.text-secondary:focus {
    color: #1f348a !important;
}

.text-success {
    color: #18634B !important;
}

a.text-success:hover, a.text-success:focus {
    color: #09251c !important;
}

.text-info {
    color: #0056B3 !important;
}

a.text-info:hover, a.text-info:focus {
    color: #003167 !important;
}

.text-warning {
    color: #F0B400 !important;
}

a.text-warning:hover, a.text-warning:focus {
    color: #a47b00 !important;
}

.text-danger {
    color: #A91E2C !important;
}

a.text-danger:hover, a.text-danger:focus {
    color: #68121b !important;
}

.text-light {
    color: #D1D9E6 !important;
}

a.text-light:hover, a.text-light:focus {
    color: #9fb0cb !important;
}

.text-dark {
    color: #31344b !important;
}

a.text-dark:hover, a.text-dark:focus {
    color: #13141d !important;
}

.text-default {
    color: #262833 !important;
}

a.text-default:hover, a.text-default:focus {
    color: #050607 !important;
}

.text-white {
    color: #ECF0F3 !important;
}

a.text-white:hover, a.text-white:focus {
    color: #bdcbd5 !important;
}

.text-gray {
    color: #44476A !important;
}

a.text-gray:hover, a.text-gray:focus {
    color: #26283b !important;
}

.text-neutral {
    color: #ECF0F3 !important;
}

a.text-neutral:hover, a.text-neutral:focus {
    color: #bdcbd5 !important;
}

.text-soft {
    color: #e6e7ee !important;
}

a.text-soft:hover, a.text-soft:focus {
    color: #b8bbcf !important;
}

.text-black {
    color: #262833 !important;
}

a.text-black:hover, a.text-black:focus {
    color: #050607 !important;
}

.text-purple {
    color: #6f42c1 !important;
}

a.text-purple:hover, a.text-purple:focus {
    color: #4e2d89 !important;
}

.text-gray-100 {
    color: #f3f7fa !important;
}

a.text-gray-100:hover, a.text-gray-100:focus {
    color: #bdd3e4 !important;
}

.text-gray-200 {
    color: #fafbfe !important;
}

a.text-gray-200:hover, a.text-gray-200:focus {
    color: #bac8f1 !important;
}

.text-gray-300 {
    color: #e6e7ee !important;
}

a.text-gray-300:hover, a.text-gray-300:focus {
    color: #b8bbcf !important;
}

.text-gray-400 {
    color: #D1D9E6 !important;
}

a.text-gray-400:hover, a.text-gray-400:focus {
    color: #9fb0cb !important;
}

.text-gray-500 {
    color: #b1bcce !important;
}

a.text-gray-500:hover, a.text-gray-500:focus {
    color: #8294b0 !important;
}

.text-gray-600 {
    color: #93a5be !important;
}

a.text-gray-600:hover, a.text-gray-600:focus {
    color: #637da1 !important;
}

.text-gray-700 {
    color: #66799e !important;
}

a.text-gray-700:hover, a.text-gray-700:focus {
    color: #475570 !important;
}

.text-gray-800 {
    color: #525480 !important;
}

a.text-gray-800:hover, a.text-gray-800:focus {
    color: #343551 !important;
}

.text-facebook {
    color: #3b5999 !important;
}

a.text-facebook:hover, a.text-facebook:focus {
    color: #263962 !important;
}

.text-dribbble {
    color: #ea4c89 !important;
}

a.text-dribbble:hover, a.text-dribbble:focus {
    color: #d11960 !important;
}

.text-github {
    color: #222222 !important;
}

a.text-github:hover, a.text-github:focus {
    color: black !important;
}

.text-behance {
    color: #0057ff !important;
}

a.text-behance:hover, a.text-behance:focus {
    color: #003db3 !important;
}

.text-twitter {
    color: #1da1f2 !important;
}

a.text-twitter:hover, a.text-twitter:focus {
    color: #0b76b8 !important;
}

.text-slack {
    color: #3aaf85 !important;
}

a.text-slack:hover, a.text-slack:focus {
    color: #277659 !important;
}

.text-body {
    color: #44476A !important;
}

.text-muted {
    color: #525480 !important;
}

.text-black-50 {
    color: rgba(38, 40, 51, 0.5) !important;
}

.text-white-50 {
    color: rgba(236, 240, 243, 0.5) !important;
}

.text-hide {
    font: 0/0 a;
    color: transparent;
    text-shadow: none;
    background-color: transparent;
    border: 0;
}

.text-decoration-none {
    text-decoration: none !important;
}

.text-break {
    word-break: break-word !important;
    overflow-wrap: break-word !important;
}

.text-reset {
    color: inherit !important;
}

.visible {
    visibility: visible !important;
}

.invisible {
    visibility: hidden !important;
}

@media print {
    *,
  *::before,
  *::after {
        text-shadow: none !important;
        box-shadow: none !important;
    }

    a:not(.btn) {
        text-decoration: underline;
    }

    abbr[title]::after {
        content: " (" attr(title) ")";
    }

    pre {
        white-space: pre-wrap !important;
    }

    pre,
  blockquote {
        border: 0.0625rem solid #b1bcce;
        page-break-inside: avoid;
    }

    thead {
        display: table-header-group;
    }

    tr,
  img {
        page-break-inside: avoid;
    }

    p,
  h2,
  h3 {
        orphans: 3;
        widows: 3;
    }

    h2,
  h3 {
        page-break-after: avoid;
    }
  @    page {
        size: a3;
    }

    body {
        min-width: 992px !important;
    }

    .container {
        min-width: 992px !important;
    }

    .navbar {
        display: none;
    }

    .badge {
        border: 0.0625rem solid #262833;
    }

    .table {
        border-collapse: collapse !important;
    }

    .table td,
    .table th {
        background-color: #ECF0F3 !important;
    }

    .table-bordered th,
  .table-bordered td {
        border: 1px solid #e6e7ee !important;
    }

    .table-dark {
        color: inherit;
    }

    .table-dark th,
    .table-dark td,
    .table-dark thead th,
    .table-dark tbody + tbody {
        border-color: #D1D9E6;
    }

    .table .thead-dark th {
        color: inherit;
        border-color: #D1D9E6;
    }
}

.datepicker {
    border-radius: 4px;
    direction: ltr;
}

.datepicker-inline {
    width: 220px;
}

.datepicker-rtl {
    direction: rtl;
}

.datepicker-rtl.dropdown-menu {
    left: auto;
}

.datepicker-rtl table tr td span {
    float: right;
}

.datepicker-dropdown {
    top: 0;
    left: 0;
    padding: 20px 22px;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.datepicker-dropdown.datepicker-orient-left:before {
    left: 6px;
}

.datepicker-dropdown.datepicker-orient-left:after {
    left: 7px;
}

.datepicker-dropdown.datepicker-orient-right:before {
    right: 6px;
}

.datepicker-dropdown.datepicker-orient-right:after {
    right: 7px;
}

.datepicker-dropdown.datepicker-orient-bottom:before {
    top: -7px;
}

.datepicker-dropdown.datepicker-orient-bottom:after {
    top: -6px;
}

.datepicker-dropdown.datepicker-orient-top:before {
    bottom: -7px;
    border-bottom: 0;
    border-top: 7px solid white;
}

.datepicker-dropdown.datepicker-orient-top:after {
    bottom: -6px;
    border-bottom: 0;
    border-top: 6px solid #ECF0F3;
}

.datepicker table {
    margin: 0;
    -webkit-touch-callout: none;
    -webkit-user-select: none;
    user-select: none;
}

.datepicker table tr td {
    border-radius: 4px;
}

.datepicker table tr th {
    border-radius: 4px;
    font-weight: 700;
}

.datepicker table tr td,
    .datepicker table tr th {
    transition: all 0.2s ease;
    width: 36px;
    height: 36px;
    border: none;
    text-align: center;
    font-size: 0.875rem;
}

.table-striped .datepicker table tr td,
  .table-striped .datepicker table tr th {
    background-color: transparent;
}

.datepicker table tr td.old, .datepicker table tr td.new {
    color: #b1bcce;
}

.datepicker table tr td.day:hover, .datepicker table tr td.focused {
    background: #e6e7ee;
    cursor: pointer;
}

.datepicker table tr td.disabled, .datepicker table tr td.disabled:hover {
    background: none;
    color: #e6e7ee;
    cursor: default;
}

.datepicker table tr td.highlighted {
    border-radius: 0;
}

.datepicker table tr td.highlighted.focused {
    background: #31344b;
}

.datepicker table tr td.highlighted.disabled, .datepicker table tr td.highlighted.disabled:active {
    background: #31344b;
    color: #D1D9E6;
}

.datepicker table tr td.today {
    background: #a0a4c1;
}

.datepicker table tr td.today.focused {
    background: white;
}

.datepicker table tr td.today.disabled, .datepicker table tr td.today.disabled:active {
    background: white;
    color: #93a5be;
}

.datepicker table tr td.range {
    background: #31344b;
    color: #ECF0F3;
    border-radius: 0;
}

.datepicker table tr td.range.focused {
    background: #212332;
}

.datepicker table tr td.range.disabled, .datepicker table tr td.range.disabled:active, .datepicker table tr td.range.day.disabled:hover {
    background: #1d1f2c;
    color: #45496a;
}

.datepicker table tr td.range.highlighted.focused {
    background: #d0d9f6;
}

.datepicker table tr td.range.highlighted.disabled, .datepicker table tr td.range.highlighted.disabled:active {
    background: #fafbfe;
    color: #e6e7ee;
}

.datepicker table tr td.range.today.disabled, .datepicker table tr td.range.today.disabled:active {
    background: #0056B3;
    color: #ECF0F3;
}

.datepicker table tr td.day.range-start {
    border-top-right-radius: 0;
    border-bottom-right-radius: 0;
}

.datepicker table tr td.day.range-end {
    border-top-left-radius: 0;
    border-bottom-left-radius: 0;
}

.datepicker table tr td.day.range-start.range-end {
    border-radius: 4px;
}

.datepicker table tr td.selected, .datepicker table tr td.selected.highlighted, .datepicker table tr td.selected:hover, .datepicker table tr td.selected.highlighted:hover, .datepicker table tr td.day.range:hover {
    background: #31344b;
    color: #ECF0F3;
}

.datepicker table tr td.active, .datepicker table tr td.active.highlighted, .datepicker table tr td.active:hover, .datepicker table tr td.active.highlighted:hover {
    background: #31344b;
    color: #ECF0F3;
    box-shadow: none;
}

.datepicker table tr td span {
    display: block;
    width: 23%;
    height: 54px;
    line-height: 54px;
    float: left;
    margin: 1%;
    cursor: pointer;
    border-radius: 4px;
}

.datepicker table tr td span:hover, .datepicker table tr td span.focused {
    background: #fafbfe;
}

.datepicker table tr td span.disabled, .datepicker table tr td span.disabled:hover {
    background: none;
    color: #e6e7ee;
    cursor: default;
}

.datepicker table tr td span.active, .datepicker table tr td span.active:hover, .datepicker table tr td span.active.disabled, .datepicker table tr td span.active.disabled:hover {
    text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25);
}

.datepicker table tr td span.old, .datepicker table tr td span.new {
    color: #93a5be;
}

.datepicker .datepicker-switch {
    width: 145px;
}

.datepicker .datepicker-switch,
  .datepicker .prev,
  .datepicker .next,
  .datepicker tfoot tr th {
    cursor: pointer;
}

.datepicker .datepicker-switch:hover,
    .datepicker .prev:hover,
    .datepicker .next:hover,
    .datepicker tfoot tr th:hover {
    background: #fafbfe;
}

.datepicker .prev.disabled,
  .datepicker .next.disabled {
    visibility: hidden;
}

.datepicker .cw {
    font-size: 10px;
    width: 12px;
    padding: 0 2px 0 5px;
    vertical-align: middle;
}

.headroom {
    will-change: transform;
    background-color: inherit;
    transition: all 0.2s ease;
}

@media (prefers-reduced-motion: reduce) {
    .headroom {
        transition: none;
    }
}

.headroom--pinned {
    transform: translateY(0%);
}

.headroom--unpinned {
    transform: translateY(-100%);
}

.headroom--not-top {
    padding-top: 1rem;
    padding-bottom: 1rem;
    box-shadow: 6px 6px 12px #b8b9be, -6px -6px 12px #ffffff;
}

.headroom--not-top.navbar-theme-primary {
    background-color: #e6e7ee;
}

.headroom--not-top.navbar-theme-primary .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-primary .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-primary .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-primary .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-secondary {
    background-color: #2D4CC8;
}

.headroom--not-top.navbar-theme-secondary .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-secondary .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-secondary .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-secondary .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-success {
    background-color: #18634B;
}

.headroom--not-top.navbar-theme-success .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-success .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-success .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-success .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-info {
    background-color: #0056B3;
}

.headroom--not-top.navbar-theme-info .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-info .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-info .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-info .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-warning {
    background-color: #F0B400;
}

.headroom--not-top.navbar-theme-warning .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-warning .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-warning .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-warning .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-danger {
    background-color: #A91E2C;
}

.headroom--not-top.navbar-theme-danger .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-danger .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-danger .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-danger .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-light {
    background-color: #D1D9E6;
}

.headroom--not-top.navbar-theme-light .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-light .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-light .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-light .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-dark {
    background-color: #31344b;
}

.headroom--not-top.navbar-theme-dark .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-dark .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-dark .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-dark .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-default {
    background-color: #262833;
}

.headroom--not-top.navbar-theme-default .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-default .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-default .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-default .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-white {
    background-color: #ECF0F3;
}

.headroom--not-top.navbar-theme-white .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-white .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-white .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-white .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-gray {
    background-color: #44476A;
}

.headroom--not-top.navbar-theme-gray .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-gray .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-gray .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-gray .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-neutral {
    background-color: #ECF0F3;
}

.headroom--not-top.navbar-theme-neutral .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-neutral .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-neutral .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-neutral .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-soft {
    background-color: #e6e7ee;
}

.headroom--not-top.navbar-theme-soft .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-soft .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-soft .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-soft .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-black {
    background-color: #262833;
}

.headroom--not-top.navbar-theme-black .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-black .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-black .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-black .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-purple {
    background-color: #6f42c1;
}

.headroom--not-top.navbar-theme-purple .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-purple .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-purple .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-purple .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-gray-100 {
    background-color: #f3f7fa;
}

.headroom--not-top.navbar-theme-gray-100 .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-gray-100 .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-gray-100 .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-gray-100 .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-gray-200 {
    background-color: #fafbfe;
}

.headroom--not-top.navbar-theme-gray-200 .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-gray-200 .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-gray-200 .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-gray-200 .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-gray-300 {
    background-color: #e6e7ee;
}

.headroom--not-top.navbar-theme-gray-300 .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-gray-300 .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-gray-300 .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-gray-300 .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-gray-400 {
    background-color: #D1D9E6;
}

.headroom--not-top.navbar-theme-gray-400 .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-gray-400 .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-gray-400 .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-gray-400 .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-gray-500 {
    background-color: #b1bcce;
}

.headroom--not-top.navbar-theme-gray-500 .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-gray-500 .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-gray-500 .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-gray-500 .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-gray-600 {
    background-color: #93a5be;
}

.headroom--not-top.navbar-theme-gray-600 .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-gray-600 .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-gray-600 .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-gray-600 .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-gray-700 {
    background-color: #66799e;
}

.headroom--not-top.navbar-theme-gray-700 .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-gray-700 .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-gray-700 .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-gray-700 .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-gray-800 {
    background-color: #525480;
}

.headroom--not-top.navbar-theme-gray-800 .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-gray-800 .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-gray-800 .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-gray-800 .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-facebook {
    background-color: #3b5999;
}

.headroom--not-top.navbar-theme-facebook .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-facebook .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-facebook .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-facebook .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-dribbble {
    background-color: #ea4c89;
}

.headroom--not-top.navbar-theme-dribbble .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-dribbble .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-dribbble .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-dribbble .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-github {
    background-color: #222222;
}

.headroom--not-top.navbar-theme-github .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-github .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-github .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-github .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-behance {
    background-color: #0057ff;
}

.headroom--not-top.navbar-theme-behance .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-behance .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-behance .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-behance .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-twitter {
    background-color: #1da1f2;
}

.headroom--not-top.navbar-theme-twitter .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-twitter .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-twitter .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-twitter .nav-link:hover {
    color: #262833;
}

.headroom--not-top.navbar-theme-slack {
    background-color: #3aaf85;
}

.headroom--not-top.navbar-theme-slack .navbar-brand-light {
    display: none;
}

.headroom--not-top.navbar-theme-slack .navbar-brand-dark {
    display: block;
}

.headroom--not-top.navbar-theme-slack .nav-link {
    color: #31344b;
}

.headroom--not-top.navbar-theme-slack .nav-link:hover {
    color: #262833;
}

.noUi-target,
.noUi-target * {
    -webkit-touch-callout: none;
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
    -webkit-user-select: none;
    touch-action: none;
    user-select: none;
    box-sizing: border-box;
}

.noUi-target {
    position: relative;
    direction: ltr;
}

.noUi-base,
.noUi-connects {
    width: 100%;
    height: 100%;
    position: relative;
    z-index: 1;
}

/* Wrapper for all connect elements.
 */
.noUi-connects {
    overflow: hidden;
    z-index: 0;
}

.noUi-connect,
.noUi-origin {
    will-change: transform;
    position: absolute;
    z-index: 1;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    transform-origin: 0 0;
}

html:not([dir="rtl"]) .noUi-horizontal .noUi-origin {
    left: auto;
    right: 0;
}

.noUi-vertical .noUi-origin {
    width: 0;
}

.noUi-horizontal .noUi-origin {
    height: 0;
}

.noUi-handle {
    position: absolute;
}

.noUi-state-tap .noUi-connect,
.noUi-state-tap .noUi-origin {
    transition: transform .3s;
}

.noUi-state-drag * {
    cursor: inherit !important;
}

.noUi-horizontal {
    height: 5px;
}

.noUi-horizontal .noUi-handle {
    left: -17px;
    top: -10px;
}

.noUi-vertical {
    width: 5px;
    height: 340px;
}

.noUi-vertical .noUi-handle {
    width: 18px;
    height: 34px;
    left: -6px;
    top: -17px;
}

html:not([dir="rtl"]) .noUi-horizontal .noUi-handle {
    right: -17px;
    left: auto;
}

.noUi-connects {
    border-radius: 3px;
}

.noUi-connect {
    background: #e6e7ee;
}

.noUi-draggable {
    cursor: ew-resize;
}

.noUi-vertical .noUi-draggable {
    cursor: ns-resize;
}

.noUi-handle {
    border: 1px solid #f3f7fa;
    border-radius: 3px;
    background: #ECF0F3;
    cursor: default;
    box-shadow: 3px 3px 6px #b8b9be, -3px -3px 6px #ffffff;
    outline: none;
}

.noUi-handle:hover {
    cursor: grab;
    cursor: -moz-grab;
}

.noUi-handle:active {
    cursor: grabbing;
    cursor: -moz-grabbing;
}

.noUi-active {
    outline: none;
}

/* Disabled state;
 */
[disabled] .noUi-connect {
    background: #D1D9E6;
}

[disabled].noUi-target,
[disabled].noUi-handle,
[disabled] .noUi-handle {
    cursor: not-allowed;
}

/* Base;
 *
 */
.noUi-pips,
.noUi-pips * {
    box-sizing: border-box;
}

.noUi-pips {
    position: absolute;
    color: #44476A;
    font-size: 0.75rem;
}

/* Values;
 *
 */
.noUi-value {
    margin-top: 5px;
    position: absolute;
    white-space: nowrap;
    text-align: center;
}

.noUi-value-sub {
    color: #44476A;
    font-size: 0.75rem;
}

/* Markings;
 *
 */
.noUi-marker {
    position: absolute;
    background: #44476A;
}

.noUi-marker-sub {
    background: #44476A;
}

.noUi-marker-large {
    background: #44476A;
}

/* Horizontal layout;
 *
 */
.noUi-pips-horizontal {
    padding: 25px 0;
    height: auto;
    top: 100%;
    left: 0;
    width: 100%;
}

.noUi-value-horizontal {
    transform: translate(-50%, 50%);
}

.noUi-rtl .noUi-value-horizontal {
    transform: translate(50%, 50%);
}

.noUi-marker-horizontal.noUi-marker {
    margin-left: -1px;
    width: 2px;
    height: 5px;
}

.noUi-marker-horizontal.noUi-marker-sub {
    height: 10px;
}

.noUi-marker-horizontal.noUi-marker-large {
    height: 12px;
}

/* Vertical layout;
 *
 */
.noUi-pips-vertical {
    padding: 0 10px;
    height: 100%;
    top: 0;
    left: 100%;
}

.noUi-value-vertical {
    transform: translate(0, -50%, 0);
    padding-left: 25px;
}

.noUi-rtl .noUi-value-vertical {
    transform: translate(0, 50%);
}

.noUi-marker-vertical.noUi-marker {
    width: 5px;
    height: 2px;
    margin-top: -1px;
}

.noUi-marker-vertical.noUi-marker-sub {
    width: 10px;
}

.noUi-marker-vertical.noUi-marker-large {
    width: 15px;
}

.noUi-tooltip {
    font-size: 0.75rem;
    display: block;
    position: absolute;
    color: #44476A;
    border: 0.0625rem solid #D1D9E6;
    padding: 5px 10px;
    text-align: center;
    white-space: nowrap;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    border-radius: 0.55rem;
}

.noUi-horizontal .noUi-tooltip {
    transform: translate(-50%, 0);
    left: 50%;
    bottom: 30px;
}

.noUi-vertical .noUi-tooltip {
    transform: translate(0, -50%);
    top: 50%;
    right: 120%;
}

.noUi-target {
    background: #31344b;
    border-radius: 5px;
    border: 0;
    margin: 15px 0;
    cursor: pointer;
}

.noUi-horizontal {
    height: 5px;
}

html:not([dir="rtl"]) .noUi-horizontal .noUi-handle {
    right: -10px;
}

.noUi-vertical {
    width: 5px;
}

.noUi-connect {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.noUi-handle {
    position: absolute;
    border: 1px solid #D1D9E6;
    border-radius: 50%;
    width: 23px;
    height: 23px;
    background: #e6e7ee;
    transition: all 250ms cubic-bezier(0.27, 0.01, 0.38, 1.06);
    box-shadow: 2px 2px 4px #b8b9be, -2px -2px 4px #ffffff;
}

.noUi-vertical .noUi-handle {
    border: 1px solid #D1D9E6;
    border-radius: 3px;
    background: #e6e7ee;
    cursor: default;
    outline: none;
    box-shadow: 2px 2px 4px #b8b9be, -2px -2px 4px #ffffff;
}

.noUi-vertical .noUi-handle:hover {
    cursor: grab;
    cursor: -moz-grab;
}

.noUi-vertical .noUi-handle:active {
    cursor: grabbing;
    cursor: -moz-grabbing;
}

.noUi-horizontal .noUi-handle.noUi-active,
.noUi-vertical .noUi-handle.noUi-active {
    transform: scale(1.2);
}

.input-slider--cyan .noUi-connect {
    background: #17a2b8;
}

.input-slider--cyan.noUi-horizontal .noUi-handle,
.input-slider--cyan.noUi-vertical .noUi-handle {
    background-color: #17a2b8;
}

.input-slider--red .noUi-connect {
    background: #A91E2C;
}

.input-slider--red.noUi-horizontal .noUi-handle,
.input-slider--red.noUi-vertical .noUi-handle {
    background-color: #A91E2C;
}

.input-slider--green .noUi-connect {
    background: #18634B;
}

.input-slider--green.noUi-horizontal .noUi-handle,
.input-slider--green.noUi-vertical .noUi-handle {
    background-color: #18634B;
}

.input-slider--yellow .noUi-connect {
    background: #F0B400;
}

.input-slider--yellow.noUi-horizontal .noUi-handle,
.input-slider--yellow.noUi-vertical .noUi-handle {
    background-color: #F0B400;
}

.input-slider--pink .noUi-connect {
    background: #e83e8c;
}

.input-slider--pink.noUi-horizontal .noUi-handle,
.input-slider--pink.noUi-vertical .noUi-handle {
    background-color: #e83e8c;
}

/* Disabled state */
[disabled] .noUi-connect,
[disabled].noUi-connect {
    background: #fafbfe;
}

[disabled] .noUi-handle,
[disabled].noUi-origin {
    cursor: not-allowed;
}

/* Range slider value labels */
.range-slider-value {
    font-size: 0.75rem;
    font-weight: 500;
    background-color: rgba(49, 52, 75, 0.7);
    color: #ECF0F3;
    border-radius: 10px;
    padding: .4em .8em .3em .85em;
}

.range-slider-wrapper .upper-info {
    font-weight: 400;
    margin-bottom: 5px;
}

.input-slider-value-output {
    background: #31344b;
    color: #ECF0F3;
    padding: 4px 8px;
    position: relative;
    top: 12px;
    font-size: 11px;
    border-radius: 2px;
}

.input-slider-value-output:after {
    bottom: 100%;
    left: 10px;
    border: solid transparent;
    content: " ";
    height: 0;
    width: 0;
    position: absolute;
    pointer-events: none;
    border-color: #31344b;
    border-bottom-color: #333;
    border-width: 4px;
    margin-left: -4px;
}

.input-slider-value-output.left:after {
    left: 10px;
    right: auto;
}

.input-slider-value-output.right:after {
    right: 10px;
    left: auto;
}

/**
 * prism.js default theme for JavaScript, CSS and HTML
 * Based on dabblet (http://dabblet.com)
 * @author Lea Verou
 */
code[class*="language-"],
pre[class*="language-"] {
    color: black;
    background: none;
    text-shadow: 0 1px white;
    font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
    font-size: 1em;
    text-align: left;
    white-space: pre;
    word-spacing: normal;
    word-break: normal;
    word-wrap: normal;
    line-height: 1.5;
    -moz-tab-size: 4;
    -o-tab-size: 4;
    tab-size: 4;
    -webkit-hyphens: none;
    hyphens: none;
}

pre[class*="language-"]::selection, pre[class*="language-"] ::selection,
code[class*="language-"]::selection, code[class*="language-"] ::selection {
    text-shadow: none;
    background: #b3d4fc;
}

@media print {
    code[class*="language-"],
  pre[class*="language-"] {
        text-shadow: none;
    }
}

/* Code blocks */
pre[class*="language-"] {
    padding: 1em;
    margin: .5em 0;
    overflow: auto;
}

:not(pre) > code[class*="language-"],
pre[class*="language-"] {
    background: #f5f2f0;
}

/* Inline code */
:not(pre) > code[class*="language-"] {
    padding: .1em;
    border-radius: .3em;
    white-space: normal;
}

.token.comment,
.token.prolog,
.token.doctype,
.token.cdata {
    color: slategray;
}

.token.punctuation {
    color: #999;
}

.namespace {
    opacity: .7;
}

.token.property,
.token.tag,
.token.boolean,
.token.number,
.token.constant,
.token.symbol,
.token.deleted {
    color: #905;
}

.token.selector,
.token.attr-name,
.token.string,
.token.char,
.token.builtin,
.token.inserted {
    color: #690;
}

.token.operator,
.token.entity,
.token.url,
.language-css .token.string,
.style .token.string {
    color: #9a6e3a;
    background: rgba(255, 255, 255, 0.5);
}

.token.atrule,
.token.attr-value,
.token.keyword {
    color: #07a;
}

.token.function,
.token.class-name {
    color: #DD4A68;
}

.token.regex,
.token.important,
.token.variable {
    color: #e90;
}

.token.important,
.token.bold {
    font-weight: bold;
}

.token.italic {
    font-style: italic;
}

.token.entity {
    cursor: help;
}

iframe {
    border: 0;
}

figcaption,
figure,
main {
    display: block;
    margin: 0;
}

img {
    max-width: 100%;
}

strong {
    font-weight: 600;
}

button:focus {
    outline: 0;
}

/**
 * = Backgrounds
 */
.bg-blue {
    background-color: #0056B3 !important;
}

a.bg-blue:hover, a.bg-blue:focus,
button.bg-blue:hover,
button.bg-blue:focus {
    background-color: #003d80 !important;
}

.bg-indigo {
    background-color: #6610f2 !important;
}

a.bg-indigo:hover, a.bg-indigo:focus,
button.bg-indigo:hover,
button.bg-indigo:focus {
    background-color: #510bc4 !important;
}

.bg-purple {
    background-color: #6f42c1 !important;
}

a.bg-purple:hover, a.bg-purple:focus,
button.bg-purple:hover,
button.bg-purple:focus {
    background-color: #59339d !important;
}

.bg-pink {
    background-color: #e83e8c !important;
}

a.bg-pink:hover, a.bg-pink:focus,
button.bg-pink:hover,
button.bg-pink:focus {
    background-color: #d91a72 !important;
}

.bg-red {
    background-color: #A91E2C !important;
}

a.bg-red:hover, a.bg-red:focus,
button.bg-red:hover,
button.bg-red:focus {
    background-color: #7e1621 !important;
}

.bg-orange {
    background-color: #fd7e14 !important;
}

a.bg-orange:hover, a.bg-orange:focus,
button.bg-orange:hover,
button.bg-orange:focus {
    background-color: #dc6502 !important;
}

.bg-yellow {
    background-color: #F0B400 !important;
}

a.bg-yellow:hover, a.bg-yellow:focus,
button.bg-yellow:hover,
button.bg-yellow:focus {
    background-color: #bd8e00 !important;
}

.bg-green {
    background-color: #18634B !important;
}

a.bg-green:hover, a.bg-green:focus,
button.bg-green:hover,
button.bg-green:focus {
    background-color: #0e3a2c !important;
}

.bg-teal {
    background-color: #0056B3 !important;
}

a.bg-teal:hover, a.bg-teal:focus,
button.bg-teal:hover,
button.bg-teal:focus {
    background-color: #003d80 !important;
}

.bg-cyan {
    background-color: #17a2b8 !important;
}

a.bg-cyan:hover, a.bg-cyan:focus,
button.bg-cyan:hover,
button.bg-cyan:focus {
    background-color: #117a8b !important;
}

.bg-white {
    background-color: #ECF0F3 !important;
}

a.bg-white:hover, a.bg-white:focus,
button.bg-white:hover,
button.bg-white:focus {
    background-color: #cdd7df !important;
}

.bg-gray {
    background-color: #93a5be !important;
}

a.bg-gray:hover, a.bg-gray:focus,
button.bg-gray:hover,
button.bg-gray:focus {
    background-color: #738aab !important;
}

.bg-gray-dark {
    background-color: #525480 !important;
}

a.bg-gray-dark:hover, a.bg-gray-dark:focus,
button.bg-gray-dark:hover,
button.bg-gray-dark:focus {
    background-color: #3e4061 !important;
}

.bg-gradient-primary {
    background: linear-gradient(87deg, #e6e7ee 0, #e4e5f0 100%) !important;
}

.bg-gradient-secondary {
    background: linear-gradient(87deg, #2D4CC8 0, #2145d4 100%) !important;
}

.bg-gradient-success {
    background: linear-gradient(87deg, #18634B 0, #12694d 100%) !important;
}

.bg-gradient-info {
    background: linear-gradient(87deg, #0056B3 0, #0056b3 100%) !important;
}

.bg-gradient-warning {
    background: linear-gradient(87deg, #F0B400 0, #f0b400 100%) !important;
}

.bg-gradient-danger {
    background: linear-gradient(87deg, #A91E2C 0, #b31424 100%) !important;
}

.bg-gradient-light {
    background: linear-gradient(87deg, #D1D9E6 0, #cdd8ea 100%) !important;
}

.bg-gradient-dark {
    background: linear-gradient(87deg, #31344b 0, #2b2f51 100%) !important;
}

.bg-gradient-default {
    background: linear-gradient(87deg, #262833 0, #222537 100%) !important;
}

.bg-gradient-white {
    background: linear-gradient(87deg, #ECF0F3 0, #eaf0f5 100%) !important;
}

.bg-gradient-gray {
    background: linear-gradient(87deg, #44476A 0, #3b4073 100%) !important;
}

.bg-gradient-neutral {
    background: linear-gradient(87deg, #ECF0F3 0, #eaf0f5 100%) !important;
}

.bg-gradient-soft {
    background: linear-gradient(87deg, #e6e7ee 0, #e4e5f0 100%) !important;
}

.bg-gradient-black {
    background: linear-gradient(87deg, #262833 0, #222537 100%) !important;
}

.bg-gradient-purple {
    background: linear-gradient(87deg, #6f42c1 0, #6b35ce 100%) !important;
}

.bg-gradient-gray-100 {
    background: linear-gradient(87deg, #f3f7fa 0, #f2f7fb 100%) !important;
}

.bg-gradient-gray-200 {
    background: linear-gradient(87deg, #fafbfe 0, #fafbfe 100%) !important;
}

.bg-gradient-gray-300 {
    background: linear-gradient(87deg, #e6e7ee 0, #e4e5f0 100%) !important;
}

.bg-gradient-gray-400 {
    background: linear-gradient(87deg, #D1D9E6 0, #cdd8ea 100%) !important;
}

.bg-gradient-gray-500 {
    background: linear-gradient(87deg, #b1bcce 0, #abbad4 100%) !important;
}

.bg-gradient-gray-600 {
    background: linear-gradient(87deg, #93a5be 0, #8aa4c7 100%) !important;
}

.bg-gradient-gray-700 {
    background: linear-gradient(87deg, #66799e 0, #5a75ab 100%) !important;
}

.bg-gradient-gray-800 {
    background: linear-gradient(87deg, #525480 0, #484a8b 100%) !important;
}

.bg-gradient-facebook {
    background: linear-gradient(87deg, #3b5999 0, #3055a4 100%) !important;
}

.bg-gradient-dribbble {
    background: linear-gradient(87deg, #ea4c89 0, #f44287 100%) !important;
}

.bg-gradient-github {
    background: linear-gradient(87deg, #222222 0, #251f1f 100%) !important;
}

.bg-gradient-behance {
    background: linear-gradient(87deg, #0057ff 0, #0057ff 100%) !important;
}

.bg-gradient-twitter {
    background: linear-gradient(87deg, #1da1f2 0, #11a4fe 100%) !important;
}

.bg-gradient-slack {
    background: linear-gradient(87deg, #3aaf85 0, #2ebb88 100%) !important;
}

.bg-gradient-primary {
    background: linear-gradient(87deg, #e6e7ee 0, #e4e5f0 100%) !important;
}

.bg-gradient-secondary {
    background: linear-gradient(87deg, #2D4CC8 0, #2145d4 100%) !important;
}

.bg-gradient-success {
    background: linear-gradient(87deg, #18634B 0, #12694d 100%) !important;
}

.bg-gradient-info {
    background: linear-gradient(87deg, #0056B3 0, #0056b3 100%) !important;
}

.bg-gradient-warning {
    background: linear-gradient(87deg, #F0B400 0, #f0b400 100%) !important;
}

.bg-gradient-danger {
    background: linear-gradient(87deg, #A91E2C 0, #b31424 100%) !important;
}

.bg-gradient-light {
    background: linear-gradient(87deg, #D1D9E6 0, #cdd8ea 100%) !important;
}

.bg-gradient-dark {
    background: linear-gradient(87deg, #31344b 0, #2b2f51 100%) !important;
}

.bg-gradient-default {
    background: linear-gradient(87deg, #262833 0, #222537 100%) !important;
}

.bg-gradient-white {
    background: linear-gradient(87deg, #ECF0F3 0, #eaf0f5 100%) !important;
}

.bg-gradient-gray {
    background: linear-gradient(87deg, #44476A 0, #3b4073 100%) !important;
}

.bg-gradient-neutral {
    background: linear-gradient(87deg, #ECF0F3 0, #eaf0f5 100%) !important;
}

.bg-gradient-soft {
    background: linear-gradient(87deg, #e6e7ee 0, #e4e5f0 100%) !important;
}

.bg-gradient-black {
    background: linear-gradient(87deg, #262833 0, #222537 100%) !important;
}

.bg-gradient-purple {
    background: linear-gradient(87deg, #6f42c1 0, #6b35ce 100%) !important;
}

.bg-gradient-gray-100 {
    background: linear-gradient(87deg, #f3f7fa 0, #f2f7fb 100%) !important;
}

.bg-gradient-gray-200 {
    background: linear-gradient(87deg, #fafbfe 0, #fafbfe 100%) !important;
}

.bg-gradient-gray-300 {
    background: linear-gradient(87deg, #e6e7ee 0, #e4e5f0 100%) !important;
}

.bg-gradient-gray-400 {
    background: linear-gradient(87deg, #D1D9E6 0, #cdd8ea 100%) !important;
}

.bg-gradient-gray-500 {
    background: linear-gradient(87deg, #b1bcce 0, #abbad4 100%) !important;
}

.bg-gradient-gray-600 {
    background: linear-gradient(87deg, #93a5be 0, #8aa4c7 100%) !important;
}

.bg-gradient-gray-700 {
    background: linear-gradient(87deg, #66799e 0, #5a75ab 100%) !important;
}

.bg-gradient-gray-800 {
    background: linear-gradient(87deg, #525480 0, #484a8b 100%) !important;
}

.bg-gradient-facebook {
    background: linear-gradient(87deg, #3b5999 0, #3055a4 100%) !important;
}

.bg-gradient-dribbble {
    background: linear-gradient(87deg, #ea4c89 0, #f44287 100%) !important;
}

.bg-gradient-github {
    background: linear-gradient(87deg, #222222 0, #251f1f 100%) !important;
}

.bg-gradient-behance {
    background: linear-gradient(87deg, #0057ff 0, #0057ff 100%) !important;
}

.bg-gradient-twitter {
    background: linear-gradient(87deg, #1da1f2 0, #11a4fe 100%) !important;
}

.bg-gradient-slack {
    background: linear-gradient(87deg, #3aaf85 0, #2ebb88 100%) !important;
}

.overlay-primary:before {
    position: absolute;
    content: "";
    background: #e6e7ee;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-primary:before {
    position: absolute;
    content: "";
    background: #e6e7ee;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-secondary:before {
    position: absolute;
    content: "";
    background: #2D4CC8;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-secondary:before {
    position: absolute;
    content: "";
    background: #2D4CC8;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-success:before {
    position: absolute;
    content: "";
    background: #18634B;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-success:before {
    position: absolute;
    content: "";
    background: #18634B;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-info:before {
    position: absolute;
    content: "";
    background: #0056B3;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-info:before {
    position: absolute;
    content: "";
    background: #0056B3;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-warning:before {
    position: absolute;
    content: "";
    background: #F0B400;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-warning:before {
    position: absolute;
    content: "";
    background: #F0B400;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-danger:before {
    position: absolute;
    content: "";
    background: #A91E2C;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-danger:before {
    position: absolute;
    content: "";
    background: #A91E2C;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-light:before {
    position: absolute;
    content: "";
    background: #D1D9E6;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-light:before {
    position: absolute;
    content: "";
    background: #D1D9E6;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-dark:before {
    position: absolute;
    content: "";
    background: #31344b;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-dark:before {
    position: absolute;
    content: "";
    background: #31344b;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-default:before {
    position: absolute;
    content: "";
    background: #262833;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-default:before {
    position: absolute;
    content: "";
    background: #262833;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-white:before {
    position: absolute;
    content: "";
    background: #ECF0F3;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-white:before {
    position: absolute;
    content: "";
    background: #ECF0F3;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-gray:before {
    position: absolute;
    content: "";
    background: #44476A;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-gray:before {
    position: absolute;
    content: "";
    background: #44476A;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-neutral:before {
    position: absolute;
    content: "";
    background: #ECF0F3;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-neutral:before {
    position: absolute;
    content: "";
    background: #ECF0F3;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-soft:before {
    position: absolute;
    content: "";
    background: #e6e7ee;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-soft:before {
    position: absolute;
    content: "";
    background: #e6e7ee;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-black:before {
    position: absolute;
    content: "";
    background: #262833;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-black:before {
    position: absolute;
    content: "";
    background: #262833;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-purple:before {
    position: absolute;
    content: "";
    background: #6f42c1;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-purple:before {
    position: absolute;
    content: "";
    background: #6f42c1;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-gray-100:before {
    position: absolute;
    content: "";
    background: #f3f7fa;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-gray-100:before {
    position: absolute;
    content: "";
    background: #f3f7fa;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-gray-200:before {
    position: absolute;
    content: "";
    background: #fafbfe;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-gray-200:before {
    position: absolute;
    content: "";
    background: #fafbfe;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-gray-300:before {
    position: absolute;
    content: "";
    background: #e6e7ee;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-gray-300:before {
    position: absolute;
    content: "";
    background: #e6e7ee;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-gray-400:before {
    position: absolute;
    content: "";
    background: #D1D9E6;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-gray-400:before {
    position: absolute;
    content: "";
    background: #D1D9E6;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-gray-500:before {
    position: absolute;
    content: "";
    background: #b1bcce;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-gray-500:before {
    position: absolute;
    content: "";
    background: #b1bcce;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-gray-600:before {
    position: absolute;
    content: "";
    background: #93a5be;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-gray-600:before {
    position: absolute;
    content: "";
    background: #93a5be;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-gray-700:before {
    position: absolute;
    content: "";
    background: #66799e;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-gray-700:before {
    position: absolute;
    content: "";
    background: #66799e;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-gray-800:before {
    position: absolute;
    content: "";
    background: #525480;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-gray-800:before {
    position: absolute;
    content: "";
    background: #525480;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-facebook:before {
    position: absolute;
    content: "";
    background: #3b5999;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-facebook:before {
    position: absolute;
    content: "";
    background: #3b5999;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-dribbble:before {
    position: absolute;
    content: "";
    background: #ea4c89;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-dribbble:before {
    position: absolute;
    content: "";
    background: #ea4c89;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-github:before {
    position: absolute;
    content: "";
    background: #222222;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-github:before {
    position: absolute;
    content: "";
    background: #222222;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-behance:before {
    position: absolute;
    content: "";
    background: #0057ff;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-behance:before {
    position: absolute;
    content: "";
    background: #0057ff;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-twitter:before {
    position: absolute;
    content: "";
    background: #1da1f2;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-twitter:before {
    position: absolute;
    content: "";
    background: #1da1f2;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.overlay-slack:before {
    position: absolute;
    content: "";
    background: #3aaf85;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.5;
    z-index: 0;
}

.overlay-soft-slack:before {
    position: absolute;
    content: "";
    background: #3aaf85;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0.3;
    z-index: 0;
}

.section-primary {
    background-color: #e6e7ee !important;
}

a.section-primary:hover, a.section-primary:focus,
button.section-primary:hover,
button.section-primary:focus {
    background-color: #c8cad9 !important;
}

.section-secondary {
    background-color: #2D4CC8 !important;
}

a.section-secondary:hover, a.section-secondary:focus,
button.section-secondary:hover,
button.section-secondary:focus {
    background-color: #243c9e !important;
}

.section-success {
    background-color: #18634B !important;
}

a.section-success:hover, a.section-success:focus,
button.section-success:hover,
button.section-success:focus {
    background-color: #0e3a2c !important;
}

.section-info {
    background-color: #0056B3 !important;
}

a.section-info:hover, a.section-info:focus,
button.section-info:hover,
button.section-info:focus {
    background-color: #003d80 !important;
}

.section-warning {
    background-color: #F0B400 !important;
}

a.section-warning:hover, a.section-warning:focus,
button.section-warning:hover,
button.section-warning:focus {
    background-color: #bd8e00 !important;
}

.section-danger {
    background-color: #A91E2C !important;
}

a.section-danger:hover, a.section-danger:focus,
button.section-danger:hover,
button.section-danger:focus {
    background-color: #7e1621 !important;
}

.section-light {
    background-color: #D1D9E6 !important;
}

a.section-light:hover, a.section-light:focus,
button.section-light:hover,
button.section-light:focus {
    background-color: #b0bed4 !important;
}

.section-dark {
    background-color: #31344b !important;
}

a.section-dark:hover, a.section-dark:focus,
button.section-dark:hover,
button.section-dark:focus {
    background-color: #1d1f2c !important;
}

.section-default {
    background-color: #262833 !important;
}

a.section-default:hover, a.section-default:focus,
button.section-default:hover,
button.section-default:focus {
    background-color: #101116 !important;
}

.section-white {
    background-color: #ECF0F3 !important;
}

a.section-white:hover, a.section-white:focus,
button.section-white:hover,
button.section-white:focus {
    background-color: #cdd7df !important;
}

.section-gray {
    background-color: #44476A !important;
}

a.section-gray:hover, a.section-gray:focus,
button.section-gray:hover,
button.section-gray:focus {
    background-color: #30324b !important;
}

.section-neutral {
    background-color: #ECF0F3 !important;
}

a.section-neutral:hover, a.section-neutral:focus,
button.section-neutral:hover,
button.section-neutral:focus {
    background-color: #cdd7df !important;
}

.section-soft {
    background-color: #e6e7ee !important;
}

a.section-soft:hover, a.section-soft:focus,
button.section-soft:hover,
button.section-soft:focus {
    background-color: #c8cad9 !important;
}

.section-black {
    background-color: #262833 !important;
}

a.section-black:hover, a.section-black:focus,
button.section-black:hover,
button.section-black:focus {
    background-color: #101116 !important;
}

.section-purple {
    background-color: #6f42c1 !important;
}

a.section-purple:hover, a.section-purple:focus,
button.section-purple:hover,
button.section-purple:focus {
    background-color: #59339d !important;
}

.section-gray-100 {
    background-color: #f3f7fa !important;
}

a.section-gray-100:hover, a.section-gray-100:focus,
button.section-gray-100:hover,
button.section-gray-100:focus {
    background-color: #cfdfeb !important;
}

.section-gray-200 {
    background-color: #fafbfe !important;
}

a.section-gray-200:hover, a.section-gray-200:focus,
button.section-gray-200:hover,
button.section-gray-200:focus {
    background-color: #d0d9f6 !important;
}

.section-gray-300 {
    background-color: #e6e7ee !important;
}

a.section-gray-300:hover, a.section-gray-300:focus,
button.section-gray-300:hover,
button.section-gray-300:focus {
    background-color: #c8cad9 !important;
}

.section-gray-400 {
    background-color: #D1D9E6 !important;
}

a.section-gray-400:hover, a.section-gray-400:focus,
button.section-gray-400:hover,
button.section-gray-400:focus {
    background-color: #b0bed4 !important;
}

.section-gray-500 {
    background-color: #b1bcce !important;
}

a.section-gray-500:hover, a.section-gray-500:focus,
button.section-gray-500:hover,
button.section-gray-500:focus {
    background-color: #92a1ba !important;
}

.section-gray-600 {
    background-color: #93a5be !important;
}

a.section-gray-600:hover, a.section-gray-600:focus,
button.section-gray-600:hover,
button.section-gray-600:focus {
    background-color: #738aab !important;
}

.section-gray-700 {
    background-color: #66799e !important;
}

a.section-gray-700:hover, a.section-gray-700:focus,
button.section-gray-700:hover,
button.section-gray-700:focus {
    background-color: #516180 !important;
}

.section-gray-800 {
    background-color: #525480 !important;
}

a.section-gray-800:hover, a.section-gray-800:focus,
button.section-gray-800:hover,
button.section-gray-800:focus {
    background-color: #3e4061 !important;
}

.section-facebook {
    background-color: #3b5999 !important;
}

a.section-facebook:hover, a.section-facebook:focus,
button.section-facebook:hover,
button.section-facebook:focus {
    background-color: #2d4474 !important;
}

.section-dribbble {
    background-color: #ea4c89 !important;
}

a.section-dribbble:hover, a.section-dribbble:focus,
button.section-dribbble:hover,
button.section-dribbble:focus {
    background-color: #e51e6b !important;
}

.section-github {
    background-color: #222222 !important;
}

a.section-github:hover, a.section-github:focus,
button.section-github:hover,
button.section-github:focus {
    background-color: #090909 !important;
}

.section-behance {
    background-color: #0057ff !important;
}

a.section-behance:hover, a.section-behance:focus,
button.section-behance:hover,
button.section-behance:focus {
    background-color: #0046cc !important;
}

.section-twitter {
    background-color: #1da1f2 !important;
}

a.section-twitter:hover, a.section-twitter:focus,
button.section-twitter:hover,
button.section-twitter:focus {
    background-color: #0c85d0 !important;
}

.section-slack {
    background-color: #3aaf85 !important;
}

a.section-slack:hover, a.section-slack:focus,
button.section-slack:hover,
button.section-slack:focus {
    background-color: #2d8968 !important;
}

.section-image {
    background-repeat: no-repeat;
    background-position: top center;
    background-size: cover;
}

.bg-img-holder {
    position: absolute;
    height: 100%;
    min-height: 20rem;
    background-repeat: no-repeat;
    z-index: -1;
}

/**
 * = Floating animations
 */
.floating-xs {
    animation: floating-xs 3s ease infinite;
    will-change: transform;
}

.floating-xs:hover {
    animation-play-state: paused;
}

@media (min-width: 576px) {
    .floating-sm {
        animation: floating-sm 3s ease infinite;
        will-change: transform;
    }

    .floating-sm:hover {
        animation-play-state: paused;
    }
}

@media (min-width: 768px) {
    .floating-md {
        animation: floating-md 3s ease infinite;
        will-change: transform;
    }

    .floating-md:hover {
        animation-play-state: paused;
    }
}

@media (min-width: 992px) {
    .floating-lg {
        animation: floating-lg 3s ease infinite;
        will-change: transform;
    }

    .floating-lg:hover {
        animation-play-state: paused;
    }
}

@media (min-width: 1200px) {
    .floating-xl {
        animation: floating-xl 3s ease infinite;
        will-change: transform;
    }

    .floating-xl:hover {
        animation-play-state: paused;
    }
}

@keyframes floating-lg {
    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(15px);
    }

    100% {
        transform: translateY(0px);
    }
}

@keyframes floating-md {
    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(10px);
    }

    100% {
        transform: translateY(0px);
    }
}

@keyframes floating-sm {
    0% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(5px);
    }

    100% {
        transform: translateY(0px);
    }
}

/**
* = Helper classes
*/
.overflow-visible {
    overflow: visible !important;
}

.opacity-0 {
    opacity: 0 !important;
}

.opacity-1 {
    opacity: 0.1 !important;
}

.opacity-2 {
    opacity: 0.2 !important;
}

.opacity-3 {
    opacity: 0.3 !important;
}

.opacity-4 {
    opacity: 0.4 !important;
}

.opacity-5 {
    opacity: 0.5 !important;
}

.opacity-6 {
    opacity: 0.6 !important;
}

.opacity-7 {
    opacity: 0.7 !important;
}

.opacity-8 {
    opacity: 0.8 !important;
}

.opacity-9 {
    opacity: 0.9 !important;
}

.fill-opacity-0 {
    fill-opacity: 0 !important;
}

.fill-opacity-1 {
    fill-opacity: 0.1 !important;
}

.fill-opacity-2 {
    fill-opacity: 0.2 !important;
}

.fill-opacity-3 {
    fill-opacity: 0.3 !important;
}

.fill-opacity-4 {
    fill-opacity: 0.4 !important;
}

.fill-opacity-5 {
    fill-opacity: 0.5 !important;
}

.fill-opacity-6 {
    fill-opacity: 0.6 !important;
}

.fill-opacity-7 {
    fill-opacity: 0.7 !important;
}

.fill-opacity-8 {
    fill-opacity: 0.8 !important;
}

.fill-opacity-9 {
    fill-opacity: 0.9 !important;
}

.z-0 {
    position: relative;
    z-index: 0 !important;
}

.z-1 {
    position: relative;
    z-index: 1 !important;
}

.z-2 {
    position: relative;
    z-index: 2 !important;
}

.z-3 {
    position: relative;
    z-index: 3 !important;
}

.z-4 {
    position: relative;
    z-index: 4 !important;
}

.z-5 {
    position: relative;
    z-index: 5 !important;
}

.z-6 {
    position: relative;
    z-index: 6 !important;
}

.z-7 {
    position: relative;
    z-index: 7 !important;
}

.z-8 {
    position: relative;
    z-index: 8 !important;
}

.z-9 {
    position: relative;
    z-index: 9 !important;
}

.bw-md {
    border-width: 0.125rem !important;
}

.bw-lg {
    border-width: 0.25rem !important;
}

.bw-xl {
    border-width: 0.375rem !important;
}

.rounded-xl {
    border-radius: 0.95rem !important;
}

/**
 * = Spacing
 */
.top-0 {
    top: 0;
}

.right-0 {
    right: 0;
}

.bottom-0 {
    bottom: 0;
}

.left-0 {
    left: 0;
}

.top-1 {
    top: 0.25rem;
}

.right-1 {
    right: 0.25rem;
}

.bottom-1 {
    bottom: 0.25rem;
}

.left-1 {
    left: 0.25rem;
}

.top-2 {
    top: 0.5rem;
}

.right-2 {
    right: 0.5rem;
}

.bottom-2 {
    bottom: 0.5rem;
}

.left-2 {
    left: 0.5rem;
}

.top-3 {
    top: 1rem;
}

.right-3 {
    right: 1rem;
}

.bottom-3 {
    bottom: 1rem;
}

.left-3 {
    left: 1rem;
}

.top-4 {
    top: 1.5rem;
}

.right-4 {
    right: 1.5rem;
}

.bottom-4 {
    bottom: 1.5rem;
}

.left-4 {
    left: 1.5rem;
}

.top-5 {
    top: 3rem;
}

.right-5 {
    right: 3rem;
}

.bottom-5 {
    bottom: 3rem;
}

.left-5 {
    left: 3rem;
}

.top-6 {
    top: 5rem;
}

.right-6 {
    right: 5rem;
}

.bottom-6 {
    bottom: 5rem;
}

.left-6 {
    left: 5rem;
}

.top-7 {
    top: 8rem;
}

.right-7 {
    right: 8rem;
}

.bottom-7 {
    bottom: 8rem;
}

.left-7 {
    left: 8rem;
}

.top-8 {
    top: 10rem;
}

.right-8 {
    right: 10rem;
}

.bottom-8 {
    bottom: 10rem;
}

.left-8 {
    left: 10rem;
}

.top-9 {
    top: 11rem;
}

.right-9 {
    right: 11rem;
}

.bottom-9 {
    bottom: 11rem;
}

.left-9 {
    left: 11rem;
}

.top-10 {
    top: 15rem;
}

.right-10 {
    right: 15rem;
}

.bottom-10 {
    bottom: 15rem;
}

.left-10 {
    left: 15rem;
}

.top-sm {
    top: 1rem;
}

.right-sm {
    right: 1rem;
}

.bottom-sm {
    bottom: 1rem;
}

.left-sm {
    left: 1rem;
}

.top-md {
    top: 2rem;
}

.right-md {
    right: 2rem;
}

.bottom-md {
    bottom: 2rem;
}

.left-md {
    left: 2rem;
}

.top-lg {
    top: 4rem;
}

.right-lg {
    right: 4rem;
}

.bottom-lg {
    bottom: 4rem;
}

.left-lg {
    left: 4rem;
}

.top-xl {
    top: 8rem;
}

.right-xl {
    right: 8rem;
}

.bottom-xl {
    bottom: 8rem;
}

.left-xl {
    left: 8rem;
}

.center-vertical-absolute,
.center-horizontal-absolute {
    position: absolute;
}

.center-vertical-absolute {
    top: 50%;
    transform: translateY(-50%);
}

.center-horizontal-absolute {
    left: 50%;
    transform: translateX(-50%);
}

/**
 * = Sizing
 */
.h-100vh {
    height: 100vh !important;
}

.fh-50 {
    height: 50px !important;
}

.fh-100 {
    height: 100px !important;
}

.fh-150 {
    height: 150px !important;
}

.fh-200 {
    height: 200px !important;
}

.fh-250 {
    height: 250px !important;
}

.fh-300 {
    height: 300px !important;
}

.fh-350 {
    height: 350px !important;
}

.fh-400 {
    height: 400px !important;
}

.fh-450 {
    height: 450px !important;
}

.fh-500 {
    height: 500px !important;
}

.fh-550 {
    height: 550px !important;
}

.fh-600 {
    height: 600px !important;
}

.fh-650 {
    height: 650px !important;
}

.fh-700 {
    height: 700px !important;
}

.fh-750 {
    height: 750px !important;
}

.fh-800 {
    height: 800px !important;
}

.fh-850 {
    height: 850px !important;
}

.fh-900 {
    height: 900px !important;
}

.fh-950 {
    height: 950px !important;
}

.fh-1000 {
    height: 1000px !important;
}

.fh-1050 {
    height: 1050px !important;
}

.fh-1100 {
    height: 1100px !important;
}

.fh-1150 {
    height: 1150px !important;
}

.fh-1200 {
    height: 1200px !important;
}

.fh-1250 {
    height: 1250px !important;
}

.fh-1300 {
    height: 1300px !important;
}

.fh-1350 {
    height: 1350px !important;
}

.fh-1400 {
    height: 1400px !important;
}

.fh-1450 {
    height: 1450px !important;
}

.fh-1500 {
    height: 1500px !important;
}

.fh-1550 {
    height: 1550px !important;
}

.fh-1600 {
    height: 1600px !important;
}

.fh-1650 {
    height: 1650px !important;
}

.fh-1700 {
    height: 1700px !important;
}

.fh-1750 {
    height: 1750px !important;
}

.fh-1800 {
    height: 1800px !important;
}

.fh-1850 {
    height: 1850px !important;
}

.fh-1900 {
    height: 1900px !important;
}

.fh-1950 {
    height: 1950px !important;
}

.fw-50 {
    width: 50px !important;
}

.fw-100 {
    width: 100px !important;
}

.fw-150 {
    width: 150px !important;
}

.fw-200 {
    width: 200px !important;
}

.fw-250 {
    width: 250px !important;
}

.fw-300 {
    width: 300px !important;
}

.fw-350 {
    width: 350px !important;
}

.fw-400 {
    width: 400px !important;
}

.fw-450 {
    width: 450px !important;
}

.fw-500 {
    width: 500px !important;
}

.fw-550 {
    width: 550px !important;
}

.fw-600 {
    width: 600px !important;
}

.fw-650 {
    width: 650px !important;
}

.fw-700 {
    width: 700px !important;
}

.fw-750 {
    width: 750px !important;
}

.fw-800 {
    width: 800px !important;
}

.fw-850 {
    width: 850px !important;
}

.fw-900 {
    width: 900px !important;
}

.fw-950 {
    width: 950px !important;
}

.fw-1000 {
    width: 1000px !important;
}

.fw-1050 {
    width: 1050px !important;
}

.fw-1100 {
    width: 1100px !important;
}

.fw-1150 {
    width: 1150px !important;
}

.fw-1200 {
    width: 1200px !important;
}

.fw-1250 {
    width: 1250px !important;
}

.fw-1300 {
    width: 1300px !important;
}

.fw-1350 {
    width: 1350px !important;
}

.fw-1400 {
    width: 1400px !important;
}

.fw-1450 {
    width: 1450px !important;
}

.fw-1500 {
    width: 1500px !important;
}

.fw-1550 {
    width: 1550px !important;
}

.fw-1600 {
    width: 1600px !important;
}

.fw-1650 {
    width: 1650px !important;
}

.fw-1700 {
    width: 1700px !important;
}

.fw-1750 {
    width: 1750px !important;
}

.fw-1800 {
    width: 1800px !important;
}

.fw-1850 {
    width: 1850px !important;
}

.fw-1900 {
    width: 1900px !important;
}

.fw-1950 {
    width: 1950px !important;
}

.fmh-50 {
    min-height: 50px !important;
}

.fmh-100 {
    min-height: 100px !important;
}

.fmh-150 {
    min-height: 150px !important;
}

.fmh-200 {
    min-height: 200px !important;
}

.fmh-250 {
    min-height: 250px !important;
}

.fmh-300 {
    min-height: 300px !important;
}

.fmh-350 {
    min-height: 350px !important;
}

.fmh-400 {
    min-height: 400px !important;
}

.fmh-450 {
    min-height: 450px !important;
}

.fmh-500 {
    min-height: 500px !important;
}

.fmh-550 {
    min-height: 550px !important;
}

.fmh-600 {
    min-height: 600px !important;
}

.fmh-650 {
    min-height: 650px !important;
}

.fmh-700 {
    min-height: 700px !important;
}

.fmh-750 {
    min-height: 750px !important;
}

.fmh-800 {
    min-height: 800px !important;
}

.fmh-850 {
    min-height: 850px !important;
}

.fmh-900 {
    min-height: 900px !important;
}

.fmh-950 {
    min-height: 950px !important;
}

.fmh-1000 {
    min-height: 1000px !important;
}

.fmh-1050 {
    min-height: 1050px !important;
}

.fmh-1100 {
    min-height: 1100px !important;
}

.fmh-1150 {
    min-height: 1150px !important;
}

.fmh-1200 {
    min-height: 1200px !important;
}

.fmh-1250 {
    min-height: 1250px !important;
}

.fmh-1300 {
    min-height: 1300px !important;
}

.fmh-1350 {
    min-height: 1350px !important;
}

.fmh-1400 {
    min-height: 1400px !important;
}

.fmh-1450 {
    min-height: 1450px !important;
}

.fmh-1500 {
    min-height: 1500px !important;
}

.fmh-1550 {
    min-height: 1550px !important;
}

.fmh-1600 {
    min-height: 1600px !important;
}

.fmh-1650 {
    min-height: 1650px !important;
}

.fmh-1700 {
    min-height: 1700px !important;
}

.fmh-1750 {
    min-height: 1750px !important;
}

.fmh-1800 {
    min-height: 1800px !important;
}

.fmh-1850 {
    min-height: 1850px !important;
}

.fmh-1900 {
    min-height: 1900px !important;
}

.fmh-1950 {
    min-height: 1950px !important;
}

.fmw-50 {
    min-width: 50px !important;
}

.fmw-100 {
    min-width: 100px !important;
}

.fmw-150 {
    min-width: 150px !important;
}

.fmw-200 {
    min-width: 200px !important;
}

.fmw-250 {
    min-width: 250px !important;
}

.fmw-300 {
    min-width: 300px !important;
}

.fmw-350 {
    min-width: 350px !important;
}

.fmw-400 {
    min-width: 400px !important;
}

.fmw-450 {
    min-width: 450px !important;
}

.fmw-500 {
    min-width: 500px !important;
}

.fmw-550 {
    min-width: 550px !important;
}

.fmw-600 {
    min-width: 600px !important;
}

.fmw-650 {
    min-width: 650px !important;
}

.fmw-700 {
    min-width: 700px !important;
}

.fmw-750 {
    min-width: 750px !important;
}

.fmw-800 {
    min-width: 800px !important;
}

.fmw-850 {
    min-width: 850px !important;
}

.fmw-900 {
    min-width: 900px !important;
}

.fmw-950 {
    min-width: 950px !important;
}

.fmw-1000 {
    min-width: 1000px !important;
}

.fmw-1050 {
    min-width: 1050px !important;
}

.fmw-1100 {
    min-width: 1100px !important;
}

.fmw-1150 {
    min-width: 1150px !important;
}

.fmw-1200 {
    min-width: 1200px !important;
}

.fmw-1250 {
    min-width: 1250px !important;
}

.fmw-1300 {
    min-width: 1300px !important;
}

.fmw-1350 {
    min-width: 1350px !important;
}

.fmw-1400 {
    min-width: 1400px !important;
}

.fmw-1450 {
    min-width: 1450px !important;
}

.fmw-1500 {
    min-width: 1500px !important;
}

.fmw-1550 {
    min-width: 1550px !important;
}

.fmw-1600 {
    min-width: 1600px !important;
}

.fmw-1650 {
    min-width: 1650px !important;
}

.fmw-1700 {
    min-width: 1700px !important;
}

.fmw-1750 {
    min-width: 1750px !important;
}

.fmw-1800 {
    min-width: 1800px !important;
}

.fmw-1850 {
    min-width: 1850px !important;
}

.fmw-1900 {
    min-width: 1900px !important;
}

.fmw-1950 {
    min-width: 1950px !important;
}

.fmxh-50 {
    max-height: 50px !important;
}

.fmxh-100 {
    max-height: 100px !important;
}

.fmxh-150 {
    max-height: 150px !important;
}

.fmxh-200 {
    max-height: 200px !important;
}

.fmxh-250 {
    max-height: 250px !important;
}

.fmxh-300 {
    max-height: 300px !important;
}

.fmxh-350 {
    max-height: 350px !important;
}

.fmxh-400 {
    max-height: 400px !important;
}

.fmxh-450 {
    max-height: 450px !important;
}

.fmxh-500 {
    max-height: 500px !important;
}

.fmxh-550 {
    max-height: 550px !important;
}

.fmxh-600 {
    max-height: 600px !important;
}

.fmxh-650 {
    max-height: 650px !important;
}

.fmxh-700 {
    max-height: 700px !important;
}

.fmxh-750 {
    max-height: 750px !important;
}

.fmxh-800 {
    max-height: 800px !important;
}

.fmxh-850 {
    max-height: 850px !important;
}

.fmxh-900 {
    max-height: 900px !important;
}

.fmxh-950 {
    max-height: 950px !important;
}

.fmxh-1000 {
    max-height: 1000px !important;
}

.fmxh-1050 {
    max-height: 1050px !important;
}

.fmxh-1100 {
    max-height: 1100px !important;
}

.fmxh-1150 {
    max-height: 1150px !important;
}

.fmxh-1200 {
    max-height: 1200px !important;
}

.fmxh-1250 {
    max-height: 1250px !important;
}

.fmxh-1300 {
    max-height: 1300px !important;
}

.fmxh-1350 {
    max-height: 1350px !important;
}

.fmxh-1400 {
    max-height: 1400px !important;
}

.fmxh-1450 {
    max-height: 1450px !important;
}

.fmxh-1500 {
    max-height: 1500px !important;
}

.fmxh-1550 {
    max-height: 1550px !important;
}

.fmxh-1600 {
    max-height: 1600px !important;
}

.fmxh-1650 {
    max-height: 1650px !important;
}

.fmxh-1700 {
    max-height: 1700px !important;
}

.fmxh-1750 {
    max-height: 1750px !important;
}

.fmxh-1800 {
    max-height: 1800px !important;
}

.fmxh-1850 {
    max-height: 1850px !important;
}

.fmxh-1900 {
    max-height: 1900px !important;
}

.fmxh-1950 {
    max-height: 1950px !important;
}

.fmxw-50 {
    max-width: 50px !important;
}

.fmxw-100 {
    max-width: 100px !important;
}

.fmxw-150 {
    max-width: 150px !important;
}

.fmxw-200 {
    max-width: 200px !important;
}

.fmxw-250 {
    max-width: 250px !important;
}

.fmxw-300 {
    max-width: 300px !important;
}

.fmxw-350 {
    max-width: 350px !important;
}

.fmxw-400 {
    max-width: 400px !important;
}

.fmxw-450 {
    max-width: 450px !important;
}

.fmxw-500 {
    max-width: 500px !important;
}

.fmxw-550 {
    max-width: 550px !important;
}

.fmxw-600 {
    max-width: 600px !important;
}

.fmxw-650 {
    max-width: 650px !important;
}

.fmxw-700 {
    max-width: 700px !important;
}

.fmxw-750 {
    max-width: 750px !important;
}

.fmxw-800 {
    max-width: 800px !important;
}

.fmxw-850 {
    max-width: 850px !important;
}

.fmxw-900 {
    max-width: 900px !important;
}

.fmxw-950 {
    max-width: 950px !important;
}

.fmxw-1000 {
    max-width: 1000px !important;
}

.fmxw-1050 {
    max-width: 1050px !important;
}

.fmxw-1100 {
    max-width: 1100px !important;
}

.fmxw-1150 {
    max-width: 1150px !important;
}

.fmxw-1200 {
    max-width: 1200px !important;
}

.fmxw-1250 {
    max-width: 1250px !important;
}

.fmxw-1300 {
    max-width: 1300px !important;
}

.fmxw-1350 {
    max-width: 1350px !important;
}

.fmxw-1400 {
    max-width: 1400px !important;
}

.fmxw-1450 {
    max-width: 1450px !important;
}

.fmxw-1500 {
    max-width: 1500px !important;
}

.fmxw-1550 {
    max-width: 1550px !important;
}

.fmxw-1600 {
    max-width: 1600px !important;
}

.fmxw-1650 {
    max-width: 1650px !important;
}

.fmxw-1700 {
    max-width: 1700px !important;
}

.fmxw-1750 {
    max-width: 1750px !important;
}

.fmxw-1800 {
    max-width: 1800px !important;
}

.fmxw-1850 {
    max-width: 1850px !important;
}

.fmxw-1900 {
    max-width: 1900px !important;
}

.fmxw-1950 {
    max-width: 1950px !important;
}

/**
 * = Spacing grids
 */
.row.row-grid > [class*="col-"] + [class*="col-"] {
    margin-top: 3rem;
}

.row.row-grid > [class*="col-xs-"] + [class*="col-xs-"] {
    margin-top: 0;
}

@media (min-width: 576px) {
    .row.row-grid > [class*="col-sm-"] + [class*="col-sm-"] {
        margin-top: 0;
    }
}

@media (min-width: 768px) {
    .row.row-grid > [class*="col-md-"] + [class*="col-md-"] {
        margin-top: 0;
    }
}

@media (min-width: 992px) {
    .row.row-grid > [class*="col-lg-"] + [class*="col-lg-"] {
        margin-top: 0;
    }
}

@media (min-width: 1200px) {
    .row.row-grid > [class*="col-xl-"] + [class*="col-xl-"] {
        margin-top: 0;
    }
}

.row-grid + .row-grid {
    margin-top: 3rem;
}

@media (min-width: 992px) {
    [class*="mt--"],
  [class*="mr--"],
  [class*="mb--"],
  [class*="ml--"] {
        position: relative;
        z-index: 5;
    }

    .mt--50 {
        margin-top: -50px !important;
    }

    .mr--50 {
        margin-right: -50px !important;
    }

    .mb--50 {
        margin-bottom: -50px !important;
    }

    .ml--50 {
        margin-left: -50px !important;
    }

    .mt--100 {
        margin-top: -100px !important;
    }

    .mr--100 {
        margin-right: -100px !important;
    }

    .mb--100 {
        margin-bottom: -100px !important;
    }

    .ml--100 {
        margin-left: -100px !important;
    }

    .mt--150 {
        margin-top: -150px !important;
    }

    .mr--150 {
        margin-right: -150px !important;
    }

    .mb--150 {
        margin-bottom: -150px !important;
    }

    .ml--150 {
        margin-left: -150px !important;
    }

    .mt--200 {
        margin-top: -200px !important;
    }

    .mr--200 {
        margin-right: -200px !important;
    }

    .mb--200 {
        margin-bottom: -200px !important;
    }

    .ml--200 {
        margin-left: -200px !important;
    }

    .mt--250 {
        margin-top: -250px !important;
    }

    .mr--250 {
        margin-right: -250px !important;
    }

    .mb--250 {
        margin-bottom: -250px !important;
    }

    .ml--250 {
        margin-left: -250px !important;
    }

    .mt--300 {
        margin-top: -300px !important;
    }

    .mr--300 {
        margin-right: -300px !important;
    }

    .mb--300 {
        margin-bottom: -300px !important;
    }

    .ml--300 {
        margin-left: -300px !important;
    }

    .mt--350 {
        margin-top: -350px !important;
    }

    .mr--350 {
        margin-right: -350px !important;
    }

    .mb--350 {
        margin-bottom: -350px !important;
    }

    .ml--350 {
        margin-left: -350px !important;
    }

    .mt--400 {
        margin-top: -400px !important;
    }

    .mr--400 {
        margin-right: -400px !important;
    }

    .mb--400 {
        margin-bottom: -400px !important;
    }

    .ml--400 {
        margin-left: -400px !important;
    }

    .mt--450 {
        margin-top: -450px !important;
    }

    .mr--450 {
        margin-right: -450px !important;
    }

    .mb--450 {
        margin-bottom: -450px !important;
    }

    .ml--450 {
        margin-left: -450px !important;
    }

    .mt--500 {
        margin-top: -500px !important;
    }

    .mr--500 {
        margin-right: -500px !important;
    }

    .mb--500 {
        margin-bottom: -500px !important;
    }

    .ml--500 {
        margin-left: -500px !important;
    }

    .mt--550 {
        margin-top: -550px !important;
    }

    .mr--550 {
        margin-right: -550px !important;
    }

    .mb--550 {
        margin-bottom: -550px !important;
    }

    .ml--550 {
        margin-left: -550px !important;
    }

    .mt--600 {
        margin-top: -600px !important;
    }

    .mr--600 {
        margin-right: -600px !important;
    }

    .mb--600 {
        margin-bottom: -600px !important;
    }

    .ml--600 {
        margin-left: -600px !important;
    }

    .mt-50 {
        margin-top: 50px !important;
    }

    .mr-50 {
        margin-right: 50px !important;
    }

    .mb-50 {
        margin-bottom: 50px !important;
    }

    .ml-50 {
        margin-left: 50px !important;
    }

    .mt-100 {
        margin-top: 100px !important;
    }

    .mr-100 {
        margin-right: 100px !important;
    }

    .mb-100 {
        margin-bottom: 100px !important;
    }

    .ml-100 {
        margin-left: 100px !important;
    }

    .mt-150 {
        margin-top: 150px !important;
    }

    .mr-150 {
        margin-right: 150px !important;
    }

    .mb-150 {
        margin-bottom: 150px !important;
    }

    .ml-150 {
        margin-left: 150px !important;
    }

    .mt-200 {
        margin-top: 200px !important;
    }

    .mr-200 {
        margin-right: 200px !important;
    }

    .mb-200 {
        margin-bottom: 200px !important;
    }

    .ml-200 {
        margin-left: 200px !important;
    }

    .mt-250 {
        margin-top: 250px !important;
    }

    .mr-250 {
        margin-right: 250px !important;
    }

    .mb-250 {
        margin-bottom: 250px !important;
    }

    .ml-250 {
        margin-left: 250px !important;
    }

    .mt-300 {
        margin-top: 300px !important;
    }

    .mr-300 {
        margin-right: 300px !important;
    }

    .mb-300 {
        margin-bottom: 300px !important;
    }

    .ml-300 {
        margin-left: 300px !important;
    }

    .mt-350 {
        margin-top: 350px !important;
    }

    .mr-350 {
        margin-right: 350px !important;
    }

    .mb-350 {
        margin-bottom: 350px !important;
    }

    .ml-350 {
        margin-left: 350px !important;
    }

    .mt-400 {
        margin-top: 400px !important;
    }

    .mr-400 {
        margin-right: 400px !important;
    }

    .mb-400 {
        margin-bottom: 400px !important;
    }

    .ml-400 {
        margin-left: 400px !important;
    }

    .mt-450 {
        margin-top: 450px !important;
    }

    .mr-450 {
        margin-right: 450px !important;
    }

    .mb-450 {
        margin-bottom: 450px !important;
    }

    .ml-450 {
        margin-left: 450px !important;
    }

    .mt-500 {
        margin-top: 500px !important;
    }

    .mr-500 {
        margin-right: 500px !important;
    }

    .mb-500 {
        margin-bottom: 500px !important;
    }

    .ml-500 {
        margin-left: 500px !important;
    }

    .mt-550 {
        margin-top: 550px !important;
    }

    .mr-550 {
        margin-right: 550px !important;
    }

    .mb-550 {
        margin-bottom: 550px !important;
    }

    .ml-550 {
        margin-left: 550px !important;
    }

    .mt-600 {
        margin-top: 600px !important;
    }

    .mr-600 {
        margin-right: 600px !important;
    }

    .mb-600 {
        margin-bottom: 600px !important;
    }

    .ml-600 {
        margin-left: 600px !important;
    }

    .pt-50 {
        padding-top: 50px !important;
    }

    .pr-50 {
        padding-right: 50px !important;
    }

    .pb-50 {
        padding-bottom: 50px !important;
    }

    .pl-50 {
        padding-left: 50px !important;
    }

    .pt-100 {
        padding-top: 100px !important;
    }

    .pr-100 {
        padding-right: 100px !important;
    }

    .pb-100 {
        padding-bottom: 100px !important;
    }

    .pl-100 {
        padding-left: 100px !important;
    }

    .pt-150 {
        padding-top: 150px !important;
    }

    .pr-150 {
        padding-right: 150px !important;
    }

    .pb-150 {
        padding-bottom: 150px !important;
    }

    .pl-150 {
        padding-left: 150px !important;
    }

    .pt-200 {
        padding-top: 200px !important;
    }

    .pr-200 {
        padding-right: 200px !important;
    }

    .pb-200 {
        padding-bottom: 200px !important;
    }

    .pl-200 {
        padding-left: 200px !important;
    }

    .pt-250 {
        padding-top: 250px !important;
    }

    .pr-250 {
        padding-right: 250px !important;
    }

    .pb-250 {
        padding-bottom: 250px !important;
    }

    .pl-250 {
        padding-left: 250px !important;
    }

    .pt-300 {
        padding-top: 300px !important;
    }

    .pr-300 {
        padding-right: 300px !important;
    }

    .pb-300 {
        padding-bottom: 300px !important;
    }

    .pl-300 {
        padding-left: 300px !important;
    }

    .pt-350 {
        padding-top: 350px !important;
    }

    .pr-350 {
        padding-right: 350px !important;
    }

    .pb-350 {
        padding-bottom: 350px !important;
    }

    .pl-350 {
        padding-left: 350px !important;
    }

    .pt-400 {
        padding-top: 400px !important;
    }

    .pr-400 {
        padding-right: 400px !important;
    }

    .pb-400 {
        padding-bottom: 400px !important;
    }

    .pl-400 {
        padding-left: 400px !important;
    }

    .pt-450 {
        padding-top: 450px !important;
    }

    .pr-450 {
        padding-right: 450px !important;
    }

    .pb-450 {
        padding-bottom: 450px !important;
    }

    .pl-450 {
        padding-left: 450px !important;
    }

    .pt-500 {
        padding-top: 500px !important;
    }

    .pr-500 {
        padding-right: 500px !important;
    }

    .pb-500 {
        padding-bottom: 500px !important;
    }

    .pl-500 {
        padding-left: 500px !important;
    }

    .pt-550 {
        padding-top: 550px !important;
    }

    .pr-550 {
        padding-right: 550px !important;
    }

    .pb-550 {
        padding-bottom: 550px !important;
    }

    .pl-550 {
        padding-left: 550px !important;
    }

    .pt-600 {
        padding-top: 600px !important;
    }

    .pr-600 {
        padding-right: 600px !important;
    }

    .pb-600 {
        padding-bottom: 600px !important;
    }

    .pl-600 {
        padding-left: 600px !important;
    }
}

/**
 * = Shadows
 */
[class*="shadow"] {
    transition: all 0.2s ease;
}

.shadow-soft {
    box-shadow: 6px 6px 12px #b8b9be, -6px -6px 12px #ffffff !important;
}

.shadow-inset {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF !important;
}

/**
 * = Text utility classes
 */
.text-underline {
    text-decoration: underline !important;
}

.text-through {
    text-decoration: line-through !important;
}

.display-1-xs {
    font-size: 5rem;
}

.display-2-xs {
    font-size: 3.5rem;
}

.display-3-xs {
    font-size: 2.5rem;
}

.display-4-xs {
    font-size: 1.875rem;
}

@media (min-width: 576px) {
    .display-1-sm {
        font-size: 5rem;
    }

    .display-2-sm {
        font-size: 3.5rem;
    }

    .display-3-sm {
        font-size: 2.5rem;
    }

    .display-4-sm {
        font-size: 1.875rem;
    }
}

@media (min-width: 768px) {
    .display-1-md {
        font-size: 5rem;
    }

    .display-2-md {
        font-size: 3.5rem;
    }

    .display-3-md {
        font-size: 2.5rem;
    }

    .display-4-md {
        font-size: 1.875rem;
    }
}

@media (min-width: 992px) {
    .display-1-lg {
        font-size: 5rem;
    }

    .display-2-lg {
        font-size: 3.5rem;
    }

    .display-3-lg {
        font-size: 2.5rem;
    }

    .display-4-lg {
        font-size: 1.875rem;
    }
}

@media (min-width: 1200px) {
    .display-1-xl {
        font-size: 5rem;
    }

    .display-2-xl {
        font-size: 3.5rem;
    }

    .display-3-xl {
        font-size: 2.5rem;
    }

    .display-4-xl {
        font-size: 1.875rem;
    }
}

.lh-100 {
    line-height: 1;
}

.lh-110 {
    line-height: 1.1;
}

.lh-120 {
    line-height: 1.2;
}

.lh-130 {
    line-height: 1.3;
}

.lh-140 {
    line-height: 1.4;
}

.lh-150 {
    line-height: 1.5;
}

.lh-160 {
    line-height: 1.6;
}

.lh-170 {
    line-height: 1.7;
}

.lh-180 {
    line-height: 1.8;
}

.lh-190 {
    line-height: 1.9;
}

.lh-200 {
    line-height: 2;
}

.lh-210 {
    line-height: 2.1;
}

.lh-220 {
    line-height: 2.2;
}

.lh-230 {
    line-height: 2.3;
}

.lh-240 {
    line-height: 2.4;
}

.lh-250 {
    line-height: 2.5;
}

.lh-260 {
    line-height: 2.6;
}

.lh-270 {
    line-height: 2.7;
}

.lh-280 {
    line-height: 2.8;
}

.lh-290 {
    line-height: 2.9;
}

.lh-300 {
    line-height: 3;
}

.ls-1 {
    letter-spacing: .0625rem;
}

.ls-2 {
    letter-spacing: .09375rem;
}

.ls-3 {
    letter-spacing: 0.125rem;
}

.text-left {
    text-align: left !important;
}

.text-right {
    text-align: right !important;
}

.text-center {
    text-align: center !important;
}

@media (min-width: 576px) {
    .text-sm-left {
        text-align: left !important;
    }

    .text-sm-right {
        text-align: right !important;
    }

    .text-sm-center {
        text-align: center !important;
    }
}

@media (min-width: 768px) {
    .text-md-left {
        text-align: left !important;
    }

    .text-md-right {
        text-align: right !important;
    }

    .text-md-center {
        text-align: center !important;
    }
}

@media (min-width: 992px) {
    .text-lg-left {
        text-align: left !important;
    }

    .text-lg-right {
        text-align: right !important;
    }

    .text-lg-center {
        text-align: center !important;
    }
}

@media (min-width: 1200px) {
    .text-xl-left {
        text-align: left !important;
    }

    .text-xl-right {
        text-align: right !important;
    }

    .text-xl-center {
        text-align: center !important;
    }
}

.text-body {
    color: #44476A !important;
}

.text-black-50 {
    color: rgba(38, 40, 51, 0.5) !important;
}

.text-white-50 {
    color: rgba(236, 240, 243, 0.5) !important;
}

.text-hide {
    font: 0/0 a;
    color: transparent;
    text-shadow: none;
    background-color: transparent;
    border: 0;
}

.list-style-none {
    margin: 0px;
    padding: 0px;
    list-style: none;
}

/**
 * = Transform
 */
@media (min-width: 992px) {
    .transform-perspective-right {
        transform: scale(1) perspective(1040px) rotateY(-11deg) rotateX(2deg) rotate(2deg);
    }

    .transform-perspective-left {
        transform: scale(1) perspective(900px) rotateY(20deg) rotateX(-2deg) rotate(-2deg);
    }
}

.t-none {
    transform: none !important;
}

/**
 * = Animations
 */
.animate-up-1,
.animate-right-1,
.animate-down-1,
.animate-left-1,
.scale-up-1,
.scale-down-1 {
    transition: all 0.2s ease;
}

.scale-up-1:hover {
    transform: scale(0.55556);
}

.scale-up-hover-1:hover .scale {
    transform: scale(0.55556);
}

.scale-down-1:hover {
    transform: scale(0.4);
}

.animate-up-1:hover,
.animate-hover:hover .animate-up-1 {
    transform: translate(0, -1px);
}

.animate-right-1:hover,
.animate-hover:hover .animate-right-1 {
    transform: translate(1px, 0);
}

.animate-down-1:hover,
.animate-hover:hover .animate-down-1 {
    transform: translate(0, 1px);
}

.animate-left-1:hover,
.animate-hover:hover .animate-left-1 {
    transform: translate(-1px, 0);
}

.animate-up-2,
.animate-right-2,
.animate-down-2,
.animate-left-2,
.scale-up-2,
.scale-down-2 {
    transition: all 0.2s ease;
}

.scale-up-2:hover {
    transform: scale(1.11111);
}

.scale-up-hover-2:hover .scale {
    transform: scale(1.11111);
}

.scale-down-2:hover {
    transform: scale(0.8);
}

.animate-up-2:hover,
.animate-hover:hover .animate-up-2 {
    transform: translate(0, -2px);
}

.animate-right-2:hover,
.animate-hover:hover .animate-right-2 {
    transform: translate(2px, 0);
}

.animate-down-2:hover,
.animate-hover:hover .animate-down-2 {
    transform: translate(0, 2px);
}

.animate-left-2:hover,
.animate-hover:hover .animate-left-2 {
    transform: translate(-2px, 0);
}

.animate-up-3,
.animate-right-3,
.animate-down-3,
.animate-left-3,
.scale-up-3,
.scale-down-3 {
    transition: all 0.2s ease;
}

.scale-up-3:hover {
    transform: scale(1.66667);
}

.scale-up-hover-3:hover .scale {
    transform: scale(1.66667);
}

.scale-down-3:hover {
    transform: scale(1.2);
}

.animate-up-3:hover,
.animate-hover:hover .animate-up-3 {
    transform: translate(0, -3px);
}

.animate-right-3:hover,
.animate-hover:hover .animate-right-3 {
    transform: translate(3px, 0);
}

.animate-down-3:hover,
.animate-hover:hover .animate-down-3 {
    transform: translate(0, 3px);
}

.animate-left-3:hover,
.animate-hover:hover .animate-left-3 {
    transform: translate(-3px, 0);
}

.animate-up-4,
.animate-right-4,
.animate-down-4,
.animate-left-4,
.scale-up-4,
.scale-down-4 {
    transition: all 0.2s ease;
}

.scale-up-4:hover {
    transform: scale(2.22222);
}

.scale-up-hover-4:hover .scale {
    transform: scale(2.22222);
}

.scale-down-4:hover {
    transform: scale(1.6);
}

.animate-up-4:hover,
.animate-hover:hover .animate-up-4 {
    transform: translate(0, -4px);
}

.animate-right-4:hover,
.animate-hover:hover .animate-right-4 {
    transform: translate(4px, 0);
}

.animate-down-4:hover,
.animate-hover:hover .animate-down-4 {
    transform: translate(0, 4px);
}

.animate-left-4:hover,
.animate-hover:hover .animate-left-4 {
    transform: translate(-4px, 0);
}

.animate-up-5,
.animate-right-5,
.animate-down-5,
.animate-left-5,
.scale-up-5,
.scale-down-5 {
    transition: all 0.2s ease;
}

.scale-up-5:hover {
    transform: scale(2.77778);
}

.scale-up-hover-5:hover .scale {
    transform: scale(2.77778);
}

.scale-down-5:hover {
    transform: scale(2);
}

.animate-up-5:hover,
.animate-hover:hover .animate-up-5 {
    transform: translate(0, -5px);
}

.animate-right-5:hover,
.animate-hover:hover .animate-right-5 {
    transform: translate(5px, 0);
}

.animate-down-5:hover,
.animate-hover:hover .animate-down-5 {
    transform: translate(0, 5px);
}

.animate-left-5:hover,
.animate-hover:hover .animate-left-5 {
    transform: translate(-5px, 0);
}

.animate-up-6,
.animate-right-6,
.animate-down-6,
.animate-left-6,
.scale-up-6,
.scale-down-6 {
    transition: all 0.2s ease;
}

.scale-up-6:hover {
    transform: scale(3.33333);
}

.scale-up-hover-6:hover .scale {
    transform: scale(3.33333);
}

.scale-down-6:hover {
    transform: scale(2.4);
}

.animate-up-6:hover,
.animate-hover:hover .animate-up-6 {
    transform: translate(0, -6px);
}

.animate-right-6:hover,
.animate-hover:hover .animate-right-6 {
    transform: translate(6px, 0);
}

.animate-down-6:hover,
.animate-hover:hover .animate-down-6 {
    transform: translate(0, 6px);
}

.animate-left-6:hover,
.animate-hover:hover .animate-left-6 {
    transform: translate(-6px, 0);
}

.animate-up-7,
.animate-right-7,
.animate-down-7,
.animate-left-7,
.scale-up-7,
.scale-down-7 {
    transition: all 0.2s ease;
}

.scale-up-7:hover {
    transform: scale(3.88889);
}

.scale-up-hover-7:hover .scale {
    transform: scale(3.88889);
}

.scale-down-7:hover {
    transform: scale(2.8);
}

.animate-up-7:hover,
.animate-hover:hover .animate-up-7 {
    transform: translate(0, -7px);
}

.animate-right-7:hover,
.animate-hover:hover .animate-right-7 {
    transform: translate(7px, 0);
}

.animate-down-7:hover,
.animate-hover:hover .animate-down-7 {
    transform: translate(0, 7px);
}

.animate-left-7:hover,
.animate-hover:hover .animate-left-7 {
    transform: translate(-7px, 0);
}

.animate-up-8,
.animate-right-8,
.animate-down-8,
.animate-left-8,
.scale-up-8,
.scale-down-8 {
    transition: all 0.2s ease;
}

.scale-up-8:hover {
    transform: scale(4.44444);
}

.scale-up-hover-8:hover .scale {
    transform: scale(4.44444);
}

.scale-down-8:hover {
    transform: scale(3.2);
}

.animate-up-8:hover,
.animate-hover:hover .animate-up-8 {
    transform: translate(0, -8px);
}

.animate-right-8:hover,
.animate-hover:hover .animate-right-8 {
    transform: translate(8px, 0);
}

.animate-down-8:hover,
.animate-hover:hover .animate-down-8 {
    transform: translate(0, 8px);
}

.animate-left-8:hover,
.animate-hover:hover .animate-left-8 {
    transform: translate(-8px, 0);
}

.animate-up-9,
.animate-right-9,
.animate-down-9,
.animate-left-9,
.scale-up-9,
.scale-down-9 {
    transition: all 0.2s ease;
}

.scale-up-9:hover {
    transform: scale(5);
}

.scale-up-hover-9:hover .scale {
    transform: scale(5);
}

.scale-down-9:hover {
    transform: scale(3.6);
}

.animate-up-9:hover,
.animate-hover:hover .animate-up-9 {
    transform: translate(0, -9px);
}

.animate-right-9:hover,
.animate-hover:hover .animate-right-9 {
    transform: translate(9px, 0);
}

.animate-down-9:hover,
.animate-hover:hover .animate-down-9 {
    transform: translate(0, 9px);
}

.animate-left-9:hover,
.animate-hover:hover .animate-left-9 {
    transform: translate(-9px, 0);
}

@keyframes show-navbar-collapse {
    0% {
        opacity: 0;
        transform: scale(0.95);
        transform-origin: 100% 0;
    }

    100% {
        opacity: 1;
        transform: scale(1);
    }
}

@keyframes hide-navbar-collapse {
    from {
        opacity: 1;
        transform: scale(1);
        transform-origin: 100% 0;
    }

    to {
        opacity: 0;
        transform: scale(0.95);
    }
}

@keyframes show-navbar-dropdown {
    0% {
        opacity: 0;
        transform: translate(0, 10px) perspective(200px) rotateX(-2deg);
        transition: visibility 0.45s, opacity 0.45s, transform 0.45s;
    }

    100% {
        transform: translate(0, 0);
        opacity: 1;
    }
}

@keyframes hide-navbar-dropdown {
    from {
        opacity: 1;
    }

    to {
        opacity: 0;
        transform: translate(0, 10px);
    }
}

@keyframes show-dropdown {
    0% {
        opacity: 0;
        transform-origin: perspective(200px) rotateX(-2deg);
        transition: visibility 0.45s, opacity .5s;
    }

    100% {
        opacity: 1;
    }
}

@keyframes hide-dropdown {
    from {
        opacity: 1;
    }

    to {
        opacity: 0;
        transform: translate(0, 10px);
    }
}

/**
 * = Navigation bars
 */
.navbar-main {
    position: absolute;
    top: 0;
    width: 100%;
    z-index: 100;
}

.navbar-main .navbar-toggler-icon {
    background-image: url("data:image/svg+xml,%3csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3e%3cpath stroke='%2331344b' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e");
}

.navbar .navbar-nav .nav-link {
    font-size: 1rem;
    text-transform: normal;
    letter-spacing: 0;
    font-weight: 400;
    transition: all 0.8s cubic-bezier(0.34, 1.45, 0.7, 1);
}

.navbar .navbar-nav .nav-link .nav-link-inner-text {
    margin-left: .25rem;
}

.navbar .navbar-nav .nav-item .media:not(:last-child) {
    margin-bottom: 1.5rem;
}

.navbar .navbar-nav .dropdown .dropdown-item {
    font-weight: 400;
    font-size: .85rem;
}

.navbar .navbar-nav .mega-dropdown {
    position: static;
}

.navbar .navbar-nav .mega-dropdown .dropdown-menu {
    width: calc(100% - 35px);
    left: 20px;
    padding: 20px;
    border-radius: 0.55rem;
    overflow: hidden;
}

.navbar .navbar-nav .mega-dropdown .dropdown-item {
    border-radius: 0.55rem;
}

.navbar .navbar-nav .mega-dropdown .inside-bg {
    margin: -20px 0 -20px -20px;
}

.navbar .navbar-nav .mega-dropdown .inside-bg h3 {
    font-size: 1.5rem;
    font-weight: 600;
}

.navbar .navbar-nav .mega-dropdown .inside-bg-right {
    margin: -20px -20px -20px 0;
}

.navbar .navbar-nav .mega-dropdown .bg-img {
    background-size: cover;
    position: relative;
    background-position: center center;
    height: 100%;
    padding: 20px;
}

.navbar .navbar-nav .mega-dropdown h6 {
    margin: 15px 0;
    font-size: 15px;
    font-weight: 600;
}

.navbar .navbar-nav .dropdown-submenu {
    position: relative;
}

.navbar .navbar-nav .dropdown-submenu .dropdown-menu {
    display: none;
    top: 0;
    left: calc(100% - 1px);
    opacity: 0;
}

.navbar .navbar-nav .dropdown-submenu .dropdown-menu.menu-right {
    left: auto;
    right: 100%;
}

.navbar .navbar-nav .dropdown-submenu.show .dropdown-menu {
    display: block;
    opacity: 1;
    pointer-events: all;
}

.navbar .navbar-nav .nav-link-arrow {
    transition: transform 0.2s ease;
}

.navbar-brand {
    font-size: 0.875rem;
    font-weight: 600;
    text-transform: uppercase;
}

.navbar-brand img {
    height: 20px;
}

.navbar-dark .navbar-brand-light {
    display: none;
}

.navbar-dark .navbar-brand {
    color: #ECF0F3;
}

.navbar-light .navbar-brand-dark {
    display: none;
}

.navbar-light .navbar-brand {
    color: #44476A;
}

.navbar-theme-primary:not(.headroom) {
    background-color: #e6e7ee;
}

.navbar-theme-primary:not(.navbar-transparent) {
    background-color: #e6e7ee;
}

.navbar-theme-primary.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-primary.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-primary.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-primary.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-primary.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-primary.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: #6d729b;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-primary.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-primary.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-primary.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-primary.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-primary.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-primary.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-primary.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-primary.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-primary.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-primary.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-primary.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-primary.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-primary.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-primary.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-primary.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-primary.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-primary .navbar-nav .dropdown-item.active, .navbar-theme-primary .navbar-nav .dropdown-item:hover, .navbar-theme-primary .navbar-nav .dropdown-item:focus,
.navbar-theme-primary .navbar-nav .list-group-item.active,
.navbar-theme-primary .navbar-nav .list-group-item:hover,
.navbar-theme-primary .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(230, 231, 238, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-primary .navbar-nav .nav-link, .navbar-theme-primary .navbar-nav .nav-link:focus, .navbar-theme-primary .navbar-nav .nav-link.active, .navbar-theme-primary .navbar-nav .nav-link:hover,
  .navbar-theme-primary .navbar-nav .show > .nav-link,
  .navbar-theme-primary .navbar-nav .show > .nav-link:focus,
  .navbar-theme-primary .navbar-nav .show > .nav-link.active,
  .navbar-theme-primary .navbar-nav .show > .nav-link:hover,
  .navbar-theme-primary .navbar-nav .dropdown-item,
  .navbar-theme-primary .navbar-nav .dropdown-item:focus,
  .navbar-theme-primary .navbar-nav .dropdown-item.active,
  .navbar-theme-primary .navbar-nav .dropdown-item:hover,
  .navbar-theme-primary .navbar-nav .list-group-item,
  .navbar-theme-primary .navbar-nav .list-group-item:focus,
  .navbar-theme-primary .navbar-nav .list-group-item.active,
  .navbar-theme-primary .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-primary .navbar-nav .nav-link.disabled,
  .navbar-theme-primary .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-primary .navbar-nav .dropdown-item.disabled,
  .navbar-theme-primary .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-primary .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-primary .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-primary .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-secondary:not(.headroom) {
    background-color: #2D4CC8;
}

.navbar-theme-secondary:not(.navbar-transparent) {
    background-color: #2D4CC8;
}

.navbar-theme-secondary.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-secondary.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-secondary.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-secondary.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-secondary.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-secondary.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: #080d21;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-secondary.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-secondary.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-secondary.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-secondary.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-secondary.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-secondary.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-secondary.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-secondary.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-secondary.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-secondary.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-secondary.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-secondary.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-secondary.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-secondary.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-secondary.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-secondary.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-secondary .navbar-nav .dropdown-item.active, .navbar-theme-secondary .navbar-nav .dropdown-item:hover, .navbar-theme-secondary .navbar-nav .dropdown-item:focus,
.navbar-theme-secondary .navbar-nav .list-group-item.active,
.navbar-theme-secondary .navbar-nav .list-group-item:hover,
.navbar-theme-secondary .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(45, 76, 200, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-secondary .navbar-nav .nav-link, .navbar-theme-secondary .navbar-nav .nav-link:focus, .navbar-theme-secondary .navbar-nav .nav-link.active, .navbar-theme-secondary .navbar-nav .nav-link:hover,
  .navbar-theme-secondary .navbar-nav .show > .nav-link,
  .navbar-theme-secondary .navbar-nav .show > .nav-link:focus,
  .navbar-theme-secondary .navbar-nav .show > .nav-link.active,
  .navbar-theme-secondary .navbar-nav .show > .nav-link:hover,
  .navbar-theme-secondary .navbar-nav .dropdown-item,
  .navbar-theme-secondary .navbar-nav .dropdown-item:focus,
  .navbar-theme-secondary .navbar-nav .dropdown-item.active,
  .navbar-theme-secondary .navbar-nav .dropdown-item:hover,
  .navbar-theme-secondary .navbar-nav .list-group-item,
  .navbar-theme-secondary .navbar-nav .list-group-item:focus,
  .navbar-theme-secondary .navbar-nav .list-group-item.active,
  .navbar-theme-secondary .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-secondary .navbar-nav .nav-link.disabled,
  .navbar-theme-secondary .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-secondary .navbar-nav .dropdown-item.disabled,
  .navbar-theme-secondary .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-secondary .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-secondary .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-secondary .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-success:not(.headroom) {
    background-color: #18634B;
}

.navbar-theme-success:not(.navbar-transparent) {
    background-color: #18634B;
}

.navbar-theme-success.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-success.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-success.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-success.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-success.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-success.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: black;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-success.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-success.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-success.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-success.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-success.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-success.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-success.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-success.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-success.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-success.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-success.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-success.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-success.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-success.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-success.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-success.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-success .navbar-nav .dropdown-item.active, .navbar-theme-success .navbar-nav .dropdown-item:hover, .navbar-theme-success .navbar-nav .dropdown-item:focus,
.navbar-theme-success .navbar-nav .list-group-item.active,
.navbar-theme-success .navbar-nav .list-group-item:hover,
.navbar-theme-success .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(24, 99, 75, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-success .navbar-nav .nav-link, .navbar-theme-success .navbar-nav .nav-link:focus, .navbar-theme-success .navbar-nav .nav-link.active, .navbar-theme-success .navbar-nav .nav-link:hover,
  .navbar-theme-success .navbar-nav .show > .nav-link,
  .navbar-theme-success .navbar-nav .show > .nav-link:focus,
  .navbar-theme-success .navbar-nav .show > .nav-link.active,
  .navbar-theme-success .navbar-nav .show > .nav-link:hover,
  .navbar-theme-success .navbar-nav .dropdown-item,
  .navbar-theme-success .navbar-nav .dropdown-item:focus,
  .navbar-theme-success .navbar-nav .dropdown-item.active,
  .navbar-theme-success .navbar-nav .dropdown-item:hover,
  .navbar-theme-success .navbar-nav .list-group-item,
  .navbar-theme-success .navbar-nav .list-group-item:focus,
  .navbar-theme-success .navbar-nav .list-group-item.active,
  .navbar-theme-success .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-success .navbar-nav .nav-link.disabled,
  .navbar-theme-success .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-success .navbar-nav .dropdown-item.disabled,
  .navbar-theme-success .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-success .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-success .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-success .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-info:not(.headroom) {
    background-color: #0056B3;
}

.navbar-theme-info:not(.navbar-transparent) {
    background-color: #0056B3;
}

.navbar-theme-info.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-info.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-info.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-info.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-info.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-info.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: black;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-info.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-info.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-info.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-info.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-info.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-info.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-info.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-info.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-info.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-info.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-info.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-info.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-info.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-info.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-info.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-info.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-info .navbar-nav .dropdown-item.active, .navbar-theme-info .navbar-nav .dropdown-item:hover, .navbar-theme-info .navbar-nav .dropdown-item:focus,
.navbar-theme-info .navbar-nav .list-group-item.active,
.navbar-theme-info .navbar-nav .list-group-item:hover,
.navbar-theme-info .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(0, 86, 179, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-info .navbar-nav .nav-link, .navbar-theme-info .navbar-nav .nav-link:focus, .navbar-theme-info .navbar-nav .nav-link.active, .navbar-theme-info .navbar-nav .nav-link:hover,
  .navbar-theme-info .navbar-nav .show > .nav-link,
  .navbar-theme-info .navbar-nav .show > .nav-link:focus,
  .navbar-theme-info .navbar-nav .show > .nav-link.active,
  .navbar-theme-info .navbar-nav .show > .nav-link:hover,
  .navbar-theme-info .navbar-nav .dropdown-item,
  .navbar-theme-info .navbar-nav .dropdown-item:focus,
  .navbar-theme-info .navbar-nav .dropdown-item.active,
  .navbar-theme-info .navbar-nav .dropdown-item:hover,
  .navbar-theme-info .navbar-nav .list-group-item,
  .navbar-theme-info .navbar-nav .list-group-item:focus,
  .navbar-theme-info .navbar-nav .list-group-item.active,
  .navbar-theme-info .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-info .navbar-nav .nav-link.disabled,
  .navbar-theme-info .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-info .navbar-nav .dropdown-item.disabled,
  .navbar-theme-info .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-info .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-info .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-info .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-warning:not(.headroom) {
    background-color: #F0B400;
}

.navbar-theme-warning:not(.navbar-transparent) {
    background-color: #F0B400;
}

.navbar-theme-warning.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-warning.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-warning.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-warning.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-warning.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-warning.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: #241b00;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-warning.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-warning.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-warning.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-warning.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-warning.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-warning.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-warning.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-warning.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-warning.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-warning.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-warning.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-warning.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-warning.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-warning.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-warning.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-warning.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-warning .navbar-nav .dropdown-item.active, .navbar-theme-warning .navbar-nav .dropdown-item:hover, .navbar-theme-warning .navbar-nav .dropdown-item:focus,
.navbar-theme-warning .navbar-nav .list-group-item.active,
.navbar-theme-warning .navbar-nav .list-group-item:hover,
.navbar-theme-warning .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(240, 180, 0, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-warning .navbar-nav .nav-link, .navbar-theme-warning .navbar-nav .nav-link:focus, .navbar-theme-warning .navbar-nav .nav-link.active, .navbar-theme-warning .navbar-nav .nav-link:hover,
  .navbar-theme-warning .navbar-nav .show > .nav-link,
  .navbar-theme-warning .navbar-nav .show > .nav-link:focus,
  .navbar-theme-warning .navbar-nav .show > .nav-link.active,
  .navbar-theme-warning .navbar-nav .show > .nav-link:hover,
  .navbar-theme-warning .navbar-nav .dropdown-item,
  .navbar-theme-warning .navbar-nav .dropdown-item:focus,
  .navbar-theme-warning .navbar-nav .dropdown-item.active,
  .navbar-theme-warning .navbar-nav .dropdown-item:hover,
  .navbar-theme-warning .navbar-nav .list-group-item,
  .navbar-theme-warning .navbar-nav .list-group-item:focus,
  .navbar-theme-warning .navbar-nav .list-group-item.active,
  .navbar-theme-warning .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-warning .navbar-nav .nav-link.disabled,
  .navbar-theme-warning .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-warning .navbar-nav .dropdown-item.disabled,
  .navbar-theme-warning .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-warning .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-warning .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-warning .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-danger:not(.headroom) {
    background-color: #A91E2C;
}

.navbar-theme-danger:not(.navbar-transparent) {
    background-color: #A91E2C;
}

.navbar-theme-danger.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-danger.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-danger.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-danger.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-danger.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-danger.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: black;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-danger.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-danger.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-danger.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-danger.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-danger.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-danger.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-danger.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-danger.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-danger.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-danger.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-danger.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-danger.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-danger.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-danger.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-danger.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-danger.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-danger .navbar-nav .dropdown-item.active, .navbar-theme-danger .navbar-nav .dropdown-item:hover, .navbar-theme-danger .navbar-nav .dropdown-item:focus,
.navbar-theme-danger .navbar-nav .list-group-item.active,
.navbar-theme-danger .navbar-nav .list-group-item:hover,
.navbar-theme-danger .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(169, 30, 44, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-danger .navbar-nav .nav-link, .navbar-theme-danger .navbar-nav .nav-link:focus, .navbar-theme-danger .navbar-nav .nav-link.active, .navbar-theme-danger .navbar-nav .nav-link:hover,
  .navbar-theme-danger .navbar-nav .show > .nav-link,
  .navbar-theme-danger .navbar-nav .show > .nav-link:focus,
  .navbar-theme-danger .navbar-nav .show > .nav-link.active,
  .navbar-theme-danger .navbar-nav .show > .nav-link:hover,
  .navbar-theme-danger .navbar-nav .dropdown-item,
  .navbar-theme-danger .navbar-nav .dropdown-item:focus,
  .navbar-theme-danger .navbar-nav .dropdown-item.active,
  .navbar-theme-danger .navbar-nav .dropdown-item:hover,
  .navbar-theme-danger .navbar-nav .list-group-item,
  .navbar-theme-danger .navbar-nav .list-group-item:focus,
  .navbar-theme-danger .navbar-nav .list-group-item.active,
  .navbar-theme-danger .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-danger .navbar-nav .nav-link.disabled,
  .navbar-theme-danger .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-danger .navbar-nav .dropdown-item.disabled,
  .navbar-theme-danger .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-danger .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-danger .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-danger .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-light:not(.headroom) {
    background-color: #D1D9E6;
}

.navbar-theme-light:not(.navbar-transparent) {
    background-color: #D1D9E6;
}

.navbar-theme-light.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-light.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-light.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-light.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-light.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-light.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: #536d98;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-light.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-light.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-light.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-light.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-light.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-light.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-light.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-light.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-light.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-light.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-light.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-light.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-light.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-light.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-light.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-light.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-light .navbar-nav .dropdown-item.active, .navbar-theme-light .navbar-nav .dropdown-item:hover, .navbar-theme-light .navbar-nav .dropdown-item:focus,
.navbar-theme-light .navbar-nav .list-group-item.active,
.navbar-theme-light .navbar-nav .list-group-item:hover,
.navbar-theme-light .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(209, 217, 230, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-light .navbar-nav .nav-link, .navbar-theme-light .navbar-nav .nav-link:focus, .navbar-theme-light .navbar-nav .nav-link.active, .navbar-theme-light .navbar-nav .nav-link:hover,
  .navbar-theme-light .navbar-nav .show > .nav-link,
  .navbar-theme-light .navbar-nav .show > .nav-link:focus,
  .navbar-theme-light .navbar-nav .show > .nav-link.active,
  .navbar-theme-light .navbar-nav .show > .nav-link:hover,
  .navbar-theme-light .navbar-nav .dropdown-item,
  .navbar-theme-light .navbar-nav .dropdown-item:focus,
  .navbar-theme-light .navbar-nav .dropdown-item.active,
  .navbar-theme-light .navbar-nav .dropdown-item:hover,
  .navbar-theme-light .navbar-nav .list-group-item,
  .navbar-theme-light .navbar-nav .list-group-item:focus,
  .navbar-theme-light .navbar-nav .list-group-item.active,
  .navbar-theme-light .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-light .navbar-nav .nav-link.disabled,
  .navbar-theme-light .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-light .navbar-nav .dropdown-item.disabled,
  .navbar-theme-light .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-light .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-light .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-light .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-dark:not(.headroom) {
    background-color: #31344b;
}

.navbar-theme-dark:not(.navbar-transparent) {
    background-color: #31344b;
}

.navbar-theme-dark.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-dark.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-dark.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-dark.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-dark.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-dark.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: black;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-dark.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-dark.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-dark.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-dark.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-dark.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-dark.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-dark.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-dark.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-dark.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-dark.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-dark.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-dark.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-dark.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-dark.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-dark.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-dark.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-dark .navbar-nav .dropdown-item.active, .navbar-theme-dark .navbar-nav .dropdown-item:hover, .navbar-theme-dark .navbar-nav .dropdown-item:focus,
.navbar-theme-dark .navbar-nav .list-group-item.active,
.navbar-theme-dark .navbar-nav .list-group-item:hover,
.navbar-theme-dark .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(49, 52, 75, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-dark .navbar-nav .nav-link, .navbar-theme-dark .navbar-nav .nav-link:focus, .navbar-theme-dark .navbar-nav .nav-link.active, .navbar-theme-dark .navbar-nav .nav-link:hover,
  .navbar-theme-dark .navbar-nav .show > .nav-link,
  .navbar-theme-dark .navbar-nav .show > .nav-link:focus,
  .navbar-theme-dark .navbar-nav .show > .nav-link.active,
  .navbar-theme-dark .navbar-nav .show > .nav-link:hover,
  .navbar-theme-dark .navbar-nav .dropdown-item,
  .navbar-theme-dark .navbar-nav .dropdown-item:focus,
  .navbar-theme-dark .navbar-nav .dropdown-item.active,
  .navbar-theme-dark .navbar-nav .dropdown-item:hover,
  .navbar-theme-dark .navbar-nav .list-group-item,
  .navbar-theme-dark .navbar-nav .list-group-item:focus,
  .navbar-theme-dark .navbar-nav .list-group-item.active,
  .navbar-theme-dark .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-dark .navbar-nav .nav-link.disabled,
  .navbar-theme-dark .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-dark .navbar-nav .dropdown-item.disabled,
  .navbar-theme-dark .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-dark .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-dark .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-dark .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-default:not(.headroom) {
    background-color: #262833;
}

.navbar-theme-default:not(.navbar-transparent) {
    background-color: #262833;
}

.navbar-theme-default.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-default.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-default.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-default.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-default.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-default.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: black;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-default.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-default.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-default.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-default.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-default.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-default.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-default.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-default.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-default.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-default.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-default.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-default.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-default.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-default.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-default.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-default.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-default .navbar-nav .dropdown-item.active, .navbar-theme-default .navbar-nav .dropdown-item:hover, .navbar-theme-default .navbar-nav .dropdown-item:focus,
.navbar-theme-default .navbar-nav .list-group-item.active,
.navbar-theme-default .navbar-nav .list-group-item:hover,
.navbar-theme-default .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(38, 40, 51, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-default .navbar-nav .nav-link, .navbar-theme-default .navbar-nav .nav-link:focus, .navbar-theme-default .navbar-nav .nav-link.active, .navbar-theme-default .navbar-nav .nav-link:hover,
  .navbar-theme-default .navbar-nav .show > .nav-link,
  .navbar-theme-default .navbar-nav .show > .nav-link:focus,
  .navbar-theme-default .navbar-nav .show > .nav-link.active,
  .navbar-theme-default .navbar-nav .show > .nav-link:hover,
  .navbar-theme-default .navbar-nav .dropdown-item,
  .navbar-theme-default .navbar-nav .dropdown-item:focus,
  .navbar-theme-default .navbar-nav .dropdown-item.active,
  .navbar-theme-default .navbar-nav .dropdown-item:hover,
  .navbar-theme-default .navbar-nav .list-group-item,
  .navbar-theme-default .navbar-nav .list-group-item:focus,
  .navbar-theme-default .navbar-nav .list-group-item.active,
  .navbar-theme-default .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-default .navbar-nav .nav-link.disabled,
  .navbar-theme-default .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-default .navbar-nav .dropdown-item.disabled,
  .navbar-theme-default .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-default .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-default .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-default .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-white:not(.headroom) {
    background-color: #ECF0F3;
}

.navbar-theme-white:not(.navbar-transparent) {
    background-color: #ECF0F3;
}

.navbar-theme-white.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-white.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-white.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-white.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-white.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-white.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: #6f8da4;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-white.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-white.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-white.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-white.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-white.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-white.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-white.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-white.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-white.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-white.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-white.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-white.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-white.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-white.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-white.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-white.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-white .navbar-nav .dropdown-item.active, .navbar-theme-white .navbar-nav .dropdown-item:hover, .navbar-theme-white .navbar-nav .dropdown-item:focus,
.navbar-theme-white .navbar-nav .list-group-item.active,
.navbar-theme-white .navbar-nav .list-group-item:hover,
.navbar-theme-white .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(236, 240, 243, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-white .navbar-nav .nav-link, .navbar-theme-white .navbar-nav .nav-link:focus, .navbar-theme-white .navbar-nav .nav-link.active, .navbar-theme-white .navbar-nav .nav-link:hover,
  .navbar-theme-white .navbar-nav .show > .nav-link,
  .navbar-theme-white .navbar-nav .show > .nav-link:focus,
  .navbar-theme-white .navbar-nav .show > .nav-link.active,
  .navbar-theme-white .navbar-nav .show > .nav-link:hover,
  .navbar-theme-white .navbar-nav .dropdown-item,
  .navbar-theme-white .navbar-nav .dropdown-item:focus,
  .navbar-theme-white .navbar-nav .dropdown-item.active,
  .navbar-theme-white .navbar-nav .dropdown-item:hover,
  .navbar-theme-white .navbar-nav .list-group-item,
  .navbar-theme-white .navbar-nav .list-group-item:focus,
  .navbar-theme-white .navbar-nav .list-group-item.active,
  .navbar-theme-white .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-white .navbar-nav .nav-link.disabled,
  .navbar-theme-white .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-white .navbar-nav .dropdown-item.disabled,
  .navbar-theme-white .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-white .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-white .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-white .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-gray:not(.headroom) {
    background-color: #44476A;
}

.navbar-theme-gray:not(.navbar-transparent) {
    background-color: #44476A;
}

.navbar-theme-gray.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-gray.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-gray.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-gray.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-gray.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-gray.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: black;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-gray.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-gray.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-gray.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-gray.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-gray.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-gray.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-gray.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-gray.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-gray.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-gray.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-gray.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-gray.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-gray.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-gray.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-gray.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-gray.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-gray .navbar-nav .dropdown-item.active, .navbar-theme-gray .navbar-nav .dropdown-item:hover, .navbar-theme-gray .navbar-nav .dropdown-item:focus,
.navbar-theme-gray .navbar-nav .list-group-item.active,
.navbar-theme-gray .navbar-nav .list-group-item:hover,
.navbar-theme-gray .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(68, 71, 106, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-gray .navbar-nav .nav-link, .navbar-theme-gray .navbar-nav .nav-link:focus, .navbar-theme-gray .navbar-nav .nav-link.active, .navbar-theme-gray .navbar-nav .nav-link:hover,
  .navbar-theme-gray .navbar-nav .show > .nav-link,
  .navbar-theme-gray .navbar-nav .show > .nav-link:focus,
  .navbar-theme-gray .navbar-nav .show > .nav-link.active,
  .navbar-theme-gray .navbar-nav .show > .nav-link:hover,
  .navbar-theme-gray .navbar-nav .dropdown-item,
  .navbar-theme-gray .navbar-nav .dropdown-item:focus,
  .navbar-theme-gray .navbar-nav .dropdown-item.active,
  .navbar-theme-gray .navbar-nav .dropdown-item:hover,
  .navbar-theme-gray .navbar-nav .list-group-item,
  .navbar-theme-gray .navbar-nav .list-group-item:focus,
  .navbar-theme-gray .navbar-nav .list-group-item.active,
  .navbar-theme-gray .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-gray .navbar-nav .nav-link.disabled,
  .navbar-theme-gray .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-gray .navbar-nav .dropdown-item.disabled,
  .navbar-theme-gray .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-gray .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-gray .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-gray .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-neutral:not(.headroom) {
    background-color: #ECF0F3;
}

.navbar-theme-neutral:not(.navbar-transparent) {
    background-color: #ECF0F3;
}

.navbar-theme-neutral.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-neutral.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-neutral.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-neutral.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-neutral.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-neutral.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: #6f8da4;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-neutral.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-neutral.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-neutral.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-neutral.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-neutral.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-neutral.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-neutral.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-neutral.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-neutral.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-neutral.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-neutral.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-neutral.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-neutral.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-neutral.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-neutral.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-neutral.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-neutral .navbar-nav .dropdown-item.active, .navbar-theme-neutral .navbar-nav .dropdown-item:hover, .navbar-theme-neutral .navbar-nav .dropdown-item:focus,
.navbar-theme-neutral .navbar-nav .list-group-item.active,
.navbar-theme-neutral .navbar-nav .list-group-item:hover,
.navbar-theme-neutral .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(236, 240, 243, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-neutral .navbar-nav .nav-link, .navbar-theme-neutral .navbar-nav .nav-link:focus, .navbar-theme-neutral .navbar-nav .nav-link.active, .navbar-theme-neutral .navbar-nav .nav-link:hover,
  .navbar-theme-neutral .navbar-nav .show > .nav-link,
  .navbar-theme-neutral .navbar-nav .show > .nav-link:focus,
  .navbar-theme-neutral .navbar-nav .show > .nav-link.active,
  .navbar-theme-neutral .navbar-nav .show > .nav-link:hover,
  .navbar-theme-neutral .navbar-nav .dropdown-item,
  .navbar-theme-neutral .navbar-nav .dropdown-item:focus,
  .navbar-theme-neutral .navbar-nav .dropdown-item.active,
  .navbar-theme-neutral .navbar-nav .dropdown-item:hover,
  .navbar-theme-neutral .navbar-nav .list-group-item,
  .navbar-theme-neutral .navbar-nav .list-group-item:focus,
  .navbar-theme-neutral .navbar-nav .list-group-item.active,
  .navbar-theme-neutral .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-neutral .navbar-nav .nav-link.disabled,
  .navbar-theme-neutral .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-neutral .navbar-nav .dropdown-item.disabled,
  .navbar-theme-neutral .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-neutral .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-neutral .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-neutral .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-soft:not(.headroom) {
    background-color: #e6e7ee;
}

.navbar-theme-soft:not(.navbar-transparent) {
    background-color: #e6e7ee;
}

.navbar-theme-soft.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-soft.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-soft.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-soft.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-soft.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-soft.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: #6d729b;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-soft.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-soft.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-soft.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-soft.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-soft.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-soft.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-soft.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-soft.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-soft.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-soft.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-soft.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-soft.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-soft.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-soft.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-soft.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-soft.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-soft .navbar-nav .dropdown-item.active, .navbar-theme-soft .navbar-nav .dropdown-item:hover, .navbar-theme-soft .navbar-nav .dropdown-item:focus,
.navbar-theme-soft .navbar-nav .list-group-item.active,
.navbar-theme-soft .navbar-nav .list-group-item:hover,
.navbar-theme-soft .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(230, 231, 238, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-soft .navbar-nav .nav-link, .navbar-theme-soft .navbar-nav .nav-link:focus, .navbar-theme-soft .navbar-nav .nav-link.active, .navbar-theme-soft .navbar-nav .nav-link:hover,
  .navbar-theme-soft .navbar-nav .show > .nav-link,
  .navbar-theme-soft .navbar-nav .show > .nav-link:focus,
  .navbar-theme-soft .navbar-nav .show > .nav-link.active,
  .navbar-theme-soft .navbar-nav .show > .nav-link:hover,
  .navbar-theme-soft .navbar-nav .dropdown-item,
  .navbar-theme-soft .navbar-nav .dropdown-item:focus,
  .navbar-theme-soft .navbar-nav .dropdown-item.active,
  .navbar-theme-soft .navbar-nav .dropdown-item:hover,
  .navbar-theme-soft .navbar-nav .list-group-item,
  .navbar-theme-soft .navbar-nav .list-group-item:focus,
  .navbar-theme-soft .navbar-nav .list-group-item.active,
  .navbar-theme-soft .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-soft .navbar-nav .nav-link.disabled,
  .navbar-theme-soft .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-soft .navbar-nav .dropdown-item.disabled,
  .navbar-theme-soft .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-soft .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-soft .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-soft .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-black:not(.headroom) {
    background-color: #262833;
}

.navbar-theme-black:not(.navbar-transparent) {
    background-color: #262833;
}

.navbar-theme-black.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-black.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-black.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-black.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-black.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-black.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: black;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-black.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-black.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-black.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-black.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-black.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-black.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-black.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-black.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-black.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-black.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-black.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-black.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-black.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-black.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-black.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-black.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-black .navbar-nav .dropdown-item.active, .navbar-theme-black .navbar-nav .dropdown-item:hover, .navbar-theme-black .navbar-nav .dropdown-item:focus,
.navbar-theme-black .navbar-nav .list-group-item.active,
.navbar-theme-black .navbar-nav .list-group-item:hover,
.navbar-theme-black .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(38, 40, 51, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-black .navbar-nav .nav-link, .navbar-theme-black .navbar-nav .nav-link:focus, .navbar-theme-black .navbar-nav .nav-link.active, .navbar-theme-black .navbar-nav .nav-link:hover,
  .navbar-theme-black .navbar-nav .show > .nav-link,
  .navbar-theme-black .navbar-nav .show > .nav-link:focus,
  .navbar-theme-black .navbar-nav .show > .nav-link.active,
  .navbar-theme-black .navbar-nav .show > .nav-link:hover,
  .navbar-theme-black .navbar-nav .dropdown-item,
  .navbar-theme-black .navbar-nav .dropdown-item:focus,
  .navbar-theme-black .navbar-nav .dropdown-item.active,
  .navbar-theme-black .navbar-nav .dropdown-item:hover,
  .navbar-theme-black .navbar-nav .list-group-item,
  .navbar-theme-black .navbar-nav .list-group-item:focus,
  .navbar-theme-black .navbar-nav .list-group-item.active,
  .navbar-theme-black .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-black .navbar-nav .nav-link.disabled,
  .navbar-theme-black .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-black .navbar-nav .dropdown-item.disabled,
  .navbar-theme-black .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-black .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-black .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-black .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-purple:not(.headroom) {
    background-color: #6f42c1;
}

.navbar-theme-purple:not(.navbar-transparent) {
    background-color: #6f42c1;
}

.navbar-theme-purple.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-purple.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-purple.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-purple.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-purple.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-purple.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: #170e29;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-purple.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-purple.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-purple.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-purple.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-purple.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-purple.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-purple.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-purple.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-purple.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-purple.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-purple.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-purple.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-purple.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-purple.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-purple.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-purple.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-purple .navbar-nav .dropdown-item.active, .navbar-theme-purple .navbar-nav .dropdown-item:hover, .navbar-theme-purple .navbar-nav .dropdown-item:focus,
.navbar-theme-purple .navbar-nav .list-group-item.active,
.navbar-theme-purple .navbar-nav .list-group-item:hover,
.navbar-theme-purple .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(111, 66, 193, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-purple .navbar-nav .nav-link, .navbar-theme-purple .navbar-nav .nav-link:focus, .navbar-theme-purple .navbar-nav .nav-link.active, .navbar-theme-purple .navbar-nav .nav-link:hover,
  .navbar-theme-purple .navbar-nav .show > .nav-link,
  .navbar-theme-purple .navbar-nav .show > .nav-link:focus,
  .navbar-theme-purple .navbar-nav .show > .nav-link.active,
  .navbar-theme-purple .navbar-nav .show > .nav-link:hover,
  .navbar-theme-purple .navbar-nav .dropdown-item,
  .navbar-theme-purple .navbar-nav .dropdown-item:focus,
  .navbar-theme-purple .navbar-nav .dropdown-item.active,
  .navbar-theme-purple .navbar-nav .dropdown-item:hover,
  .navbar-theme-purple .navbar-nav .list-group-item,
  .navbar-theme-purple .navbar-nav .list-group-item:focus,
  .navbar-theme-purple .navbar-nav .list-group-item.active,
  .navbar-theme-purple .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-purple .navbar-nav .nav-link.disabled,
  .navbar-theme-purple .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-purple .navbar-nav .dropdown-item.disabled,
  .navbar-theme-purple .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-purple .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-purple .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-purple .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-gray-100:not(.headroom) {
    background-color: #f3f7fa;
}

.navbar-theme-gray-100:not(.navbar-transparent) {
    background-color: #f3f7fa;
}

.navbar-theme-gray-100.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-gray-100.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-gray-100.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-gray-100.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-gray-100.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-gray-100.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: #6397be;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-gray-100.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-gray-100.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-gray-100.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-gray-100.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-gray-100.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-gray-100.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-gray-100.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-gray-100.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-gray-100.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-gray-100.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-gray-100.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-gray-100.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-gray-100.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-gray-100.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-gray-100.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-gray-100.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-gray-100 .navbar-nav .dropdown-item.active, .navbar-theme-gray-100 .navbar-nav .dropdown-item:hover, .navbar-theme-gray-100 .navbar-nav .dropdown-item:focus,
.navbar-theme-gray-100 .navbar-nav .list-group-item.active,
.navbar-theme-gray-100 .navbar-nav .list-group-item:hover,
.navbar-theme-gray-100 .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(243, 247, 250, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-gray-100 .navbar-nav .nav-link, .navbar-theme-gray-100 .navbar-nav .nav-link:focus, .navbar-theme-gray-100 .navbar-nav .nav-link.active, .navbar-theme-gray-100 .navbar-nav .nav-link:hover,
  .navbar-theme-gray-100 .navbar-nav .show > .nav-link,
  .navbar-theme-gray-100 .navbar-nav .show > .nav-link:focus,
  .navbar-theme-gray-100 .navbar-nav .show > .nav-link.active,
  .navbar-theme-gray-100 .navbar-nav .show > .nav-link:hover,
  .navbar-theme-gray-100 .navbar-nav .dropdown-item,
  .navbar-theme-gray-100 .navbar-nav .dropdown-item:focus,
  .navbar-theme-gray-100 .navbar-nav .dropdown-item.active,
  .navbar-theme-gray-100 .navbar-nav .dropdown-item:hover,
  .navbar-theme-gray-100 .navbar-nav .list-group-item,
  .navbar-theme-gray-100 .navbar-nav .list-group-item:focus,
  .navbar-theme-gray-100 .navbar-nav .list-group-item.active,
  .navbar-theme-gray-100 .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-gray-100 .navbar-nav .nav-link.disabled,
  .navbar-theme-gray-100 .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-gray-100 .navbar-nav .dropdown-item.disabled,
  .navbar-theme-gray-100 .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-gray-100 .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-gray-100 .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-gray-100 .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-gray-200:not(.headroom) {
    background-color: #fafbfe;
}

.navbar-theme-gray-200:not(.navbar-transparent) {
    background-color: #fafbfe;
}

.navbar-theme-gray-200.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-gray-200.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-gray-200.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-gray-200.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-gray-200.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-gray-200.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: #5073dc;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-gray-200.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-gray-200.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-gray-200.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-gray-200.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-gray-200.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-gray-200.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-gray-200.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-gray-200.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-gray-200.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-gray-200.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-gray-200.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-gray-200.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-gray-200.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-gray-200.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-gray-200.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-gray-200.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-gray-200 .navbar-nav .dropdown-item.active, .navbar-theme-gray-200 .navbar-nav .dropdown-item:hover, .navbar-theme-gray-200 .navbar-nav .dropdown-item:focus,
.navbar-theme-gray-200 .navbar-nav .list-group-item.active,
.navbar-theme-gray-200 .navbar-nav .list-group-item:hover,
.navbar-theme-gray-200 .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(250, 251, 254, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-gray-200 .navbar-nav .nav-link, .navbar-theme-gray-200 .navbar-nav .nav-link:focus, .navbar-theme-gray-200 .navbar-nav .nav-link.active, .navbar-theme-gray-200 .navbar-nav .nav-link:hover,
  .navbar-theme-gray-200 .navbar-nav .show > .nav-link,
  .navbar-theme-gray-200 .navbar-nav .show > .nav-link:focus,
  .navbar-theme-gray-200 .navbar-nav .show > .nav-link.active,
  .navbar-theme-gray-200 .navbar-nav .show > .nav-link:hover,
  .navbar-theme-gray-200 .navbar-nav .dropdown-item,
  .navbar-theme-gray-200 .navbar-nav .dropdown-item:focus,
  .navbar-theme-gray-200 .navbar-nav .dropdown-item.active,
  .navbar-theme-gray-200 .navbar-nav .dropdown-item:hover,
  .navbar-theme-gray-200 .navbar-nav .list-group-item,
  .navbar-theme-gray-200 .navbar-nav .list-group-item:focus,
  .navbar-theme-gray-200 .navbar-nav .list-group-item.active,
  .navbar-theme-gray-200 .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-gray-200 .navbar-nav .nav-link.disabled,
  .navbar-theme-gray-200 .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-gray-200 .navbar-nav .dropdown-item.disabled,
  .navbar-theme-gray-200 .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-gray-200 .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-gray-200 .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-gray-200 .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-gray-300:not(.headroom) {
    background-color: #e6e7ee;
}

.navbar-theme-gray-300:not(.navbar-transparent) {
    background-color: #e6e7ee;
}

.navbar-theme-gray-300.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-gray-300.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-gray-300.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-gray-300.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-gray-300.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-gray-300.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: #6d729b;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-gray-300.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-gray-300.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-gray-300.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-gray-300.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-gray-300.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-gray-300.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-gray-300.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-gray-300.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-gray-300.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-gray-300.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-gray-300.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-gray-300.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-gray-300.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-gray-300.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-gray-300.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-gray-300.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-gray-300 .navbar-nav .dropdown-item.active, .navbar-theme-gray-300 .navbar-nav .dropdown-item:hover, .navbar-theme-gray-300 .navbar-nav .dropdown-item:focus,
.navbar-theme-gray-300 .navbar-nav .list-group-item.active,
.navbar-theme-gray-300 .navbar-nav .list-group-item:hover,
.navbar-theme-gray-300 .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(230, 231, 238, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-gray-300 .navbar-nav .nav-link, .navbar-theme-gray-300 .navbar-nav .nav-link:focus, .navbar-theme-gray-300 .navbar-nav .nav-link.active, .navbar-theme-gray-300 .navbar-nav .nav-link:hover,
  .navbar-theme-gray-300 .navbar-nav .show > .nav-link,
  .navbar-theme-gray-300 .navbar-nav .show > .nav-link:focus,
  .navbar-theme-gray-300 .navbar-nav .show > .nav-link.active,
  .navbar-theme-gray-300 .navbar-nav .show > .nav-link:hover,
  .navbar-theme-gray-300 .navbar-nav .dropdown-item,
  .navbar-theme-gray-300 .navbar-nav .dropdown-item:focus,
  .navbar-theme-gray-300 .navbar-nav .dropdown-item.active,
  .navbar-theme-gray-300 .navbar-nav .dropdown-item:hover,
  .navbar-theme-gray-300 .navbar-nav .list-group-item,
  .navbar-theme-gray-300 .navbar-nav .list-group-item:focus,
  .navbar-theme-gray-300 .navbar-nav .list-group-item.active,
  .navbar-theme-gray-300 .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-gray-300 .navbar-nav .nav-link.disabled,
  .navbar-theme-gray-300 .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-gray-300 .navbar-nav .dropdown-item.disabled,
  .navbar-theme-gray-300 .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-gray-300 .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-gray-300 .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-gray-300 .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-gray-400:not(.headroom) {
    background-color: #D1D9E6;
}

.navbar-theme-gray-400:not(.navbar-transparent) {
    background-color: #D1D9E6;
}

.navbar-theme-gray-400.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-gray-400.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-gray-400.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-gray-400.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-gray-400.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-gray-400.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: #536d98;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-gray-400.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-gray-400.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-gray-400.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-gray-400.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-gray-400.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-gray-400.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-gray-400.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-gray-400.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-gray-400.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-gray-400.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-gray-400.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-gray-400.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-gray-400.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-gray-400.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-gray-400.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-gray-400.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-gray-400 .navbar-nav .dropdown-item.active, .navbar-theme-gray-400 .navbar-nav .dropdown-item:hover, .navbar-theme-gray-400 .navbar-nav .dropdown-item:focus,
.navbar-theme-gray-400 .navbar-nav .list-group-item.active,
.navbar-theme-gray-400 .navbar-nav .list-group-item:hover,
.navbar-theme-gray-400 .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(209, 217, 230, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-gray-400 .navbar-nav .nav-link, .navbar-theme-gray-400 .navbar-nav .nav-link:focus, .navbar-theme-gray-400 .navbar-nav .nav-link.active, .navbar-theme-gray-400 .navbar-nav .nav-link:hover,
  .navbar-theme-gray-400 .navbar-nav .show > .nav-link,
  .navbar-theme-gray-400 .navbar-nav .show > .nav-link:focus,
  .navbar-theme-gray-400 .navbar-nav .show > .nav-link.active,
  .navbar-theme-gray-400 .navbar-nav .show > .nav-link:hover,
  .navbar-theme-gray-400 .navbar-nav .dropdown-item,
  .navbar-theme-gray-400 .navbar-nav .dropdown-item:focus,
  .navbar-theme-gray-400 .navbar-nav .dropdown-item.active,
  .navbar-theme-gray-400 .navbar-nav .dropdown-item:hover,
  .navbar-theme-gray-400 .navbar-nav .list-group-item,
  .navbar-theme-gray-400 .navbar-nav .list-group-item:focus,
  .navbar-theme-gray-400 .navbar-nav .list-group-item.active,
  .navbar-theme-gray-400 .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-gray-400 .navbar-nav .nav-link.disabled,
  .navbar-theme-gray-400 .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-gray-400 .navbar-nav .dropdown-item.disabled,
  .navbar-theme-gray-400 .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-gray-400 .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-gray-400 .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-gray-400 .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-gray-500:not(.headroom) {
    background-color: #b1bcce;
}

.navbar-theme-gray-500:not(.navbar-transparent) {
    background-color: #b1bcce;
}

.navbar-theme-gray-500.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-gray-500.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-gray-500.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-gray-500.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-gray-500.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-gray-500.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: #45556e;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-gray-500.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-gray-500.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-gray-500.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-gray-500.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-gray-500.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-gray-500.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-gray-500.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-gray-500.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-gray-500.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-gray-500.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-gray-500.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-gray-500.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-gray-500.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-gray-500.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-gray-500.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-gray-500.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-gray-500 .navbar-nav .dropdown-item.active, .navbar-theme-gray-500 .navbar-nav .dropdown-item:hover, .navbar-theme-gray-500 .navbar-nav .dropdown-item:focus,
.navbar-theme-gray-500 .navbar-nav .list-group-item.active,
.navbar-theme-gray-500 .navbar-nav .list-group-item:hover,
.navbar-theme-gray-500 .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(177, 188, 206, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-gray-500 .navbar-nav .nav-link, .navbar-theme-gray-500 .navbar-nav .nav-link:focus, .navbar-theme-gray-500 .navbar-nav .nav-link.active, .navbar-theme-gray-500 .navbar-nav .nav-link:hover,
  .navbar-theme-gray-500 .navbar-nav .show > .nav-link,
  .navbar-theme-gray-500 .navbar-nav .show > .nav-link:focus,
  .navbar-theme-gray-500 .navbar-nav .show > .nav-link.active,
  .navbar-theme-gray-500 .navbar-nav .show > .nav-link:hover,
  .navbar-theme-gray-500 .navbar-nav .dropdown-item,
  .navbar-theme-gray-500 .navbar-nav .dropdown-item:focus,
  .navbar-theme-gray-500 .navbar-nav .dropdown-item.active,
  .navbar-theme-gray-500 .navbar-nav .dropdown-item:hover,
  .navbar-theme-gray-500 .navbar-nav .list-group-item,
  .navbar-theme-gray-500 .navbar-nav .list-group-item:focus,
  .navbar-theme-gray-500 .navbar-nav .list-group-item.active,
  .navbar-theme-gray-500 .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-gray-500 .navbar-nav .nav-link.disabled,
  .navbar-theme-gray-500 .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-gray-500 .navbar-nav .dropdown-item.disabled,
  .navbar-theme-gray-500 .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-gray-500 .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-gray-500 .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-gray-500 .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-gray-600:not(.headroom) {
    background-color: #93a5be;
}

.navbar-theme-gray-600:not(.navbar-transparent) {
    background-color: #93a5be;
}

.navbar-theme-gray-600.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-gray-600.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-gray-600.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-gray-600.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-gray-600.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-gray-600.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: #324053;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-gray-600.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-gray-600.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-gray-600.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-gray-600.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-gray-600.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-gray-600.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-gray-600.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-gray-600.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-gray-600.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-gray-600.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-gray-600.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-gray-600.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-gray-600.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-gray-600.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-gray-600.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-gray-600.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-gray-600 .navbar-nav .dropdown-item.active, .navbar-theme-gray-600 .navbar-nav .dropdown-item:hover, .navbar-theme-gray-600 .navbar-nav .dropdown-item:focus,
.navbar-theme-gray-600 .navbar-nav .list-group-item.active,
.navbar-theme-gray-600 .navbar-nav .list-group-item:hover,
.navbar-theme-gray-600 .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(147, 165, 190, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-gray-600 .navbar-nav .nav-link, .navbar-theme-gray-600 .navbar-nav .nav-link:focus, .navbar-theme-gray-600 .navbar-nav .nav-link.active, .navbar-theme-gray-600 .navbar-nav .nav-link:hover,
  .navbar-theme-gray-600 .navbar-nav .show > .nav-link,
  .navbar-theme-gray-600 .navbar-nav .show > .nav-link:focus,
  .navbar-theme-gray-600 .navbar-nav .show > .nav-link.active,
  .navbar-theme-gray-600 .navbar-nav .show > .nav-link:hover,
  .navbar-theme-gray-600 .navbar-nav .dropdown-item,
  .navbar-theme-gray-600 .navbar-nav .dropdown-item:focus,
  .navbar-theme-gray-600 .navbar-nav .dropdown-item.active,
  .navbar-theme-gray-600 .navbar-nav .dropdown-item:hover,
  .navbar-theme-gray-600 .navbar-nav .list-group-item,
  .navbar-theme-gray-600 .navbar-nav .list-group-item:focus,
  .navbar-theme-gray-600 .navbar-nav .list-group-item.active,
  .navbar-theme-gray-600 .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-gray-600 .navbar-nav .nav-link.disabled,
  .navbar-theme-gray-600 .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-gray-600 .navbar-nav .dropdown-item.disabled,
  .navbar-theme-gray-600 .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-gray-600 .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-gray-600 .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-gray-600 .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-gray-700:not(.headroom) {
    background-color: #66799e;
}

.navbar-theme-gray-700:not(.navbar-transparent) {
    background-color: #66799e;
}

.navbar-theme-gray-700.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-gray-700.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-gray-700.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-gray-700.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-gray-700.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-gray-700.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: #161a22;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-gray-700.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-gray-700.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-gray-700.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-gray-700.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-gray-700.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-gray-700.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-gray-700.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-gray-700.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-gray-700.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-gray-700.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-gray-700.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-gray-700.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-gray-700.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-gray-700.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-gray-700.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-gray-700.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-gray-700 .navbar-nav .dropdown-item.active, .navbar-theme-gray-700 .navbar-nav .dropdown-item:hover, .navbar-theme-gray-700 .navbar-nav .dropdown-item:focus,
.navbar-theme-gray-700 .navbar-nav .list-group-item.active,
.navbar-theme-gray-700 .navbar-nav .list-group-item:hover,
.navbar-theme-gray-700 .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(102, 121, 158, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-gray-700 .navbar-nav .nav-link, .navbar-theme-gray-700 .navbar-nav .nav-link:focus, .navbar-theme-gray-700 .navbar-nav .nav-link.active, .navbar-theme-gray-700 .navbar-nav .nav-link:hover,
  .navbar-theme-gray-700 .navbar-nav .show > .nav-link,
  .navbar-theme-gray-700 .navbar-nav .show > .nav-link:focus,
  .navbar-theme-gray-700 .navbar-nav .show > .nav-link.active,
  .navbar-theme-gray-700 .navbar-nav .show > .nav-link:hover,
  .navbar-theme-gray-700 .navbar-nav .dropdown-item,
  .navbar-theme-gray-700 .navbar-nav .dropdown-item:focus,
  .navbar-theme-gray-700 .navbar-nav .dropdown-item.active,
  .navbar-theme-gray-700 .navbar-nav .dropdown-item:hover,
  .navbar-theme-gray-700 .navbar-nav .list-group-item,
  .navbar-theme-gray-700 .navbar-nav .list-group-item:focus,
  .navbar-theme-gray-700 .navbar-nav .list-group-item.active,
  .navbar-theme-gray-700 .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-gray-700 .navbar-nav .nav-link.disabled,
  .navbar-theme-gray-700 .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-gray-700 .navbar-nav .dropdown-item.disabled,
  .navbar-theme-gray-700 .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-gray-700 .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-gray-700 .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-gray-700 .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-gray-800:not(.headroom) {
    background-color: #525480;
}

.navbar-theme-gray-800:not(.navbar-transparent) {
    background-color: #525480;
}

.navbar-theme-gray-800.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-gray-800.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-gray-800.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-gray-800.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-gray-800.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-gray-800.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: #020204;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-gray-800.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-gray-800.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-gray-800.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-gray-800.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-gray-800.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-gray-800.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-gray-800.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-gray-800.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-gray-800.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-gray-800.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-gray-800.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-gray-800.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-gray-800.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-gray-800.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-gray-800.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-gray-800.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-gray-800 .navbar-nav .dropdown-item.active, .navbar-theme-gray-800 .navbar-nav .dropdown-item:hover, .navbar-theme-gray-800 .navbar-nav .dropdown-item:focus,
.navbar-theme-gray-800 .navbar-nav .list-group-item.active,
.navbar-theme-gray-800 .navbar-nav .list-group-item:hover,
.navbar-theme-gray-800 .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(82, 84, 128, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-gray-800 .navbar-nav .nav-link, .navbar-theme-gray-800 .navbar-nav .nav-link:focus, .navbar-theme-gray-800 .navbar-nav .nav-link.active, .navbar-theme-gray-800 .navbar-nav .nav-link:hover,
  .navbar-theme-gray-800 .navbar-nav .show > .nav-link,
  .navbar-theme-gray-800 .navbar-nav .show > .nav-link:focus,
  .navbar-theme-gray-800 .navbar-nav .show > .nav-link.active,
  .navbar-theme-gray-800 .navbar-nav .show > .nav-link:hover,
  .navbar-theme-gray-800 .navbar-nav .dropdown-item,
  .navbar-theme-gray-800 .navbar-nav .dropdown-item:focus,
  .navbar-theme-gray-800 .navbar-nav .dropdown-item.active,
  .navbar-theme-gray-800 .navbar-nav .dropdown-item:hover,
  .navbar-theme-gray-800 .navbar-nav .list-group-item,
  .navbar-theme-gray-800 .navbar-nav .list-group-item:focus,
  .navbar-theme-gray-800 .navbar-nav .list-group-item.active,
  .navbar-theme-gray-800 .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-gray-800 .navbar-nav .nav-link.disabled,
  .navbar-theme-gray-800 .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-gray-800 .navbar-nav .dropdown-item.disabled,
  .navbar-theme-gray-800 .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-gray-800 .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-gray-800 .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-gray-800 .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-facebook:not(.headroom) {
    background-color: #3b5999;
}

.navbar-theme-facebook:not(.navbar-transparent) {
    background-color: #3b5999;
}

.navbar-theme-facebook.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-facebook.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-facebook.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-facebook.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-facebook.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-facebook.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: #020306;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-facebook.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-facebook.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-facebook.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-facebook.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-facebook.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-facebook.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-facebook.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-facebook.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-facebook.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-facebook.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-facebook.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-facebook.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-facebook.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-facebook.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-facebook.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-facebook.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-facebook .navbar-nav .dropdown-item.active, .navbar-theme-facebook .navbar-nav .dropdown-item:hover, .navbar-theme-facebook .navbar-nav .dropdown-item:focus,
.navbar-theme-facebook .navbar-nav .list-group-item.active,
.navbar-theme-facebook .navbar-nav .list-group-item:hover,
.navbar-theme-facebook .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(59, 89, 153, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-facebook .navbar-nav .nav-link, .navbar-theme-facebook .navbar-nav .nav-link:focus, .navbar-theme-facebook .navbar-nav .nav-link.active, .navbar-theme-facebook .navbar-nav .nav-link:hover,
  .navbar-theme-facebook .navbar-nav .show > .nav-link,
  .navbar-theme-facebook .navbar-nav .show > .nav-link:focus,
  .navbar-theme-facebook .navbar-nav .show > .nav-link.active,
  .navbar-theme-facebook .navbar-nav .show > .nav-link:hover,
  .navbar-theme-facebook .navbar-nav .dropdown-item,
  .navbar-theme-facebook .navbar-nav .dropdown-item:focus,
  .navbar-theme-facebook .navbar-nav .dropdown-item.active,
  .navbar-theme-facebook .navbar-nav .dropdown-item:hover,
  .navbar-theme-facebook .navbar-nav .list-group-item,
  .navbar-theme-facebook .navbar-nav .list-group-item:focus,
  .navbar-theme-facebook .navbar-nav .list-group-item.active,
  .navbar-theme-facebook .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-facebook .navbar-nav .nav-link.disabled,
  .navbar-theme-facebook .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-facebook .navbar-nav .dropdown-item.disabled,
  .navbar-theme-facebook .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-facebook .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-facebook .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-facebook .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-dribbble:not(.headroom) {
    background-color: #ea4c89;
}

.navbar-theme-dribbble:not(.navbar-transparent) {
    background-color: #ea4c89;
}

.navbar-theme-dribbble.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-dribbble.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-dribbble.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-dribbble.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-dribbble.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-dribbble.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: #5f0b2b;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-dribbble.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-dribbble.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-dribbble.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-dribbble.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-dribbble.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-dribbble.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-dribbble.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-dribbble.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-dribbble.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-dribbble.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-dribbble.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-dribbble.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-dribbble.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-dribbble.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-dribbble.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-dribbble.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-dribbble .navbar-nav .dropdown-item.active, .navbar-theme-dribbble .navbar-nav .dropdown-item:hover, .navbar-theme-dribbble .navbar-nav .dropdown-item:focus,
.navbar-theme-dribbble .navbar-nav .list-group-item.active,
.navbar-theme-dribbble .navbar-nav .list-group-item:hover,
.navbar-theme-dribbble .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(234, 76, 137, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-dribbble .navbar-nav .nav-link, .navbar-theme-dribbble .navbar-nav .nav-link:focus, .navbar-theme-dribbble .navbar-nav .nav-link.active, .navbar-theme-dribbble .navbar-nav .nav-link:hover,
  .navbar-theme-dribbble .navbar-nav .show > .nav-link,
  .navbar-theme-dribbble .navbar-nav .show > .nav-link:focus,
  .navbar-theme-dribbble .navbar-nav .show > .nav-link.active,
  .navbar-theme-dribbble .navbar-nav .show > .nav-link:hover,
  .navbar-theme-dribbble .navbar-nav .dropdown-item,
  .navbar-theme-dribbble .navbar-nav .dropdown-item:focus,
  .navbar-theme-dribbble .navbar-nav .dropdown-item.active,
  .navbar-theme-dribbble .navbar-nav .dropdown-item:hover,
  .navbar-theme-dribbble .navbar-nav .list-group-item,
  .navbar-theme-dribbble .navbar-nav .list-group-item:focus,
  .navbar-theme-dribbble .navbar-nav .list-group-item.active,
  .navbar-theme-dribbble .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-dribbble .navbar-nav .nav-link.disabled,
  .navbar-theme-dribbble .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-dribbble .navbar-nav .dropdown-item.disabled,
  .navbar-theme-dribbble .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-dribbble .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-dribbble .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-dribbble .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-github:not(.headroom) {
    background-color: #222222;
}

.navbar-theme-github:not(.navbar-transparent) {
    background-color: #222222;
}

.navbar-theme-github.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-github.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-github.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-github.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-github.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-github.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: black;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-github.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-github.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-github.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-github.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-github.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-github.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-github.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-github.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-github.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-github.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-github.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-github.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-github.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-github.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-github.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-github.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-github .navbar-nav .dropdown-item.active, .navbar-theme-github .navbar-nav .dropdown-item:hover, .navbar-theme-github .navbar-nav .dropdown-item:focus,
.navbar-theme-github .navbar-nav .list-group-item.active,
.navbar-theme-github .navbar-nav .list-group-item:hover,
.navbar-theme-github .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(34, 34, 34, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-github .navbar-nav .nav-link, .navbar-theme-github .navbar-nav .nav-link:focus, .navbar-theme-github .navbar-nav .nav-link.active, .navbar-theme-github .navbar-nav .nav-link:hover,
  .navbar-theme-github .navbar-nav .show > .nav-link,
  .navbar-theme-github .navbar-nav .show > .nav-link:focus,
  .navbar-theme-github .navbar-nav .show > .nav-link.active,
  .navbar-theme-github .navbar-nav .show > .nav-link:hover,
  .navbar-theme-github .navbar-nav .dropdown-item,
  .navbar-theme-github .navbar-nav .dropdown-item:focus,
  .navbar-theme-github .navbar-nav .dropdown-item.active,
  .navbar-theme-github .navbar-nav .dropdown-item:hover,
  .navbar-theme-github .navbar-nav .list-group-item,
  .navbar-theme-github .navbar-nav .list-group-item:focus,
  .navbar-theme-github .navbar-nav .list-group-item.active,
  .navbar-theme-github .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-github .navbar-nav .nav-link.disabled,
  .navbar-theme-github .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-github .navbar-nav .dropdown-item.disabled,
  .navbar-theme-github .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-github .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-github .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-github .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-behance:not(.headroom) {
    background-color: #0057ff;
}

.navbar-theme-behance:not(.navbar-transparent) {
    background-color: #0057ff;
}

.navbar-theme-behance.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-behance.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-behance.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-behance.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-behance.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-behance.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: #001133;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-behance.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-behance.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-behance.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-behance.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-behance.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-behance.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-behance.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-behance.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-behance.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-behance.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-behance.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-behance.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-behance.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-behance.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-behance.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-behance.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-behance .navbar-nav .dropdown-item.active, .navbar-theme-behance .navbar-nav .dropdown-item:hover, .navbar-theme-behance .navbar-nav .dropdown-item:focus,
.navbar-theme-behance .navbar-nav .list-group-item.active,
.navbar-theme-behance .navbar-nav .list-group-item:hover,
.navbar-theme-behance .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(0, 87, 255, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-behance .navbar-nav .nav-link, .navbar-theme-behance .navbar-nav .nav-link:focus, .navbar-theme-behance .navbar-nav .nav-link.active, .navbar-theme-behance .navbar-nav .nav-link:hover,
  .navbar-theme-behance .navbar-nav .show > .nav-link,
  .navbar-theme-behance .navbar-nav .show > .nav-link:focus,
  .navbar-theme-behance .navbar-nav .show > .nav-link.active,
  .navbar-theme-behance .navbar-nav .show > .nav-link:hover,
  .navbar-theme-behance .navbar-nav .dropdown-item,
  .navbar-theme-behance .navbar-nav .dropdown-item:focus,
  .navbar-theme-behance .navbar-nav .dropdown-item.active,
  .navbar-theme-behance .navbar-nav .dropdown-item:hover,
  .navbar-theme-behance .navbar-nav .list-group-item,
  .navbar-theme-behance .navbar-nav .list-group-item:focus,
  .navbar-theme-behance .navbar-nav .list-group-item.active,
  .navbar-theme-behance .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-behance .navbar-nav .nav-link.disabled,
  .navbar-theme-behance .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-behance .navbar-nav .dropdown-item.disabled,
  .navbar-theme-behance .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-behance .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-behance .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-behance .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-twitter:not(.headroom) {
    background-color: #1da1f2;
}

.navbar-theme-twitter:not(.navbar-transparent) {
    background-color: #1da1f2;
}

.navbar-theme-twitter.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-twitter.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-twitter.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-twitter.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-twitter.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-twitter.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: #04293f;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-twitter.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-twitter.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-twitter.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-twitter.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-twitter.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-twitter.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-twitter.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-twitter.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-twitter.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-twitter.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-twitter.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-twitter.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-twitter.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-twitter.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-twitter.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-twitter.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-twitter .navbar-nav .dropdown-item.active, .navbar-theme-twitter .navbar-nav .dropdown-item:hover, .navbar-theme-twitter .navbar-nav .dropdown-item:focus,
.navbar-theme-twitter .navbar-nav .list-group-item.active,
.navbar-theme-twitter .navbar-nav .list-group-item:hover,
.navbar-theme-twitter .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(29, 161, 242, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-twitter .navbar-nav .nav-link, .navbar-theme-twitter .navbar-nav .nav-link:focus, .navbar-theme-twitter .navbar-nav .nav-link.active, .navbar-theme-twitter .navbar-nav .nav-link:hover,
  .navbar-theme-twitter .navbar-nav .show > .nav-link,
  .navbar-theme-twitter .navbar-nav .show > .nav-link:focus,
  .navbar-theme-twitter .navbar-nav .show > .nav-link.active,
  .navbar-theme-twitter .navbar-nav .show > .nav-link:hover,
  .navbar-theme-twitter .navbar-nav .dropdown-item,
  .navbar-theme-twitter .navbar-nav .dropdown-item:focus,
  .navbar-theme-twitter .navbar-nav .dropdown-item.active,
  .navbar-theme-twitter .navbar-nav .dropdown-item:hover,
  .navbar-theme-twitter .navbar-nav .list-group-item,
  .navbar-theme-twitter .navbar-nav .list-group-item:focus,
  .navbar-theme-twitter .navbar-nav .list-group-item.active,
  .navbar-theme-twitter .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-twitter .navbar-nav .nav-link.disabled,
  .navbar-theme-twitter .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-twitter .navbar-nav .dropdown-item.disabled,
  .navbar-theme-twitter .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-twitter .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-twitter .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-twitter .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-theme-slack:not(.headroom) {
    background-color: #3aaf85;
}

.navbar-theme-slack:not(.navbar-transparent) {
    background-color: #3aaf85;
}

.navbar-theme-slack.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active, .navbar-theme-slack.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover, .navbar-theme-slack.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
.navbar-theme-slack.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
.navbar-theme-slack.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover,
.navbar-theme-slack.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus {
    color: #071611;
    background: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-slack.navbar-light:not(.headroom) .navbar-nav .nav-link, .navbar-theme-slack.navbar-light:not(.headroom) .navbar-nav .nav-link:focus, .navbar-theme-slack.navbar-light:not(.headroom) .navbar-nav .nav-link.active, .navbar-theme-slack.navbar-light:not(.headroom) .navbar-nav .nav-link:hover,
  .navbar-theme-slack.navbar-light:not(.headroom) .navbar-nav .show > .nav-link,
  .navbar-theme-slack.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:focus,
  .navbar-theme-slack.navbar-light:not(.headroom) .navbar-nav .show > .nav-link.active,
  .navbar-theme-slack.navbar-light:not(.headroom) .navbar-nav .show > .nav-link:hover,
  .navbar-theme-slack.navbar-light:not(.headroom) .navbar-nav .dropdown-item,
  .navbar-theme-slack.navbar-light:not(.headroom) .navbar-nav .dropdown-item:focus,
  .navbar-theme-slack.navbar-light:not(.headroom) .navbar-nav .dropdown-item.active,
  .navbar-theme-slack.navbar-light:not(.headroom) .navbar-nav .dropdown-item:hover,
  .navbar-theme-slack.navbar-light:not(.headroom) .navbar-nav .list-group-item,
  .navbar-theme-slack.navbar-light:not(.headroom) .navbar-nav .list-group-item:focus,
  .navbar-theme-slack.navbar-light:not(.headroom) .navbar-nav .list-group-item.active,
  .navbar-theme-slack.navbar-light:not(.headroom) .navbar-nav .list-group-item:hover {
        background: #e6e7ee;
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    }
}

.navbar-theme-slack .navbar-nav .dropdown-item.active, .navbar-theme-slack .navbar-nav .dropdown-item:hover, .navbar-theme-slack .navbar-nav .dropdown-item:focus,
.navbar-theme-slack .navbar-nav .list-group-item.active,
.navbar-theme-slack .navbar-nav .list-group-item:hover,
.navbar-theme-slack .navbar-nav .list-group-item:focus {
    color: #31344b;
    background: rgba(58, 175, 133, 0.1);
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (max-width: 991.98px) {
    .navbar-theme-slack .navbar-nav .nav-link, .navbar-theme-slack .navbar-nav .nav-link:focus, .navbar-theme-slack .navbar-nav .nav-link.active, .navbar-theme-slack .navbar-nav .nav-link:hover,
  .navbar-theme-slack .navbar-nav .show > .nav-link,
  .navbar-theme-slack .navbar-nav .show > .nav-link:focus,
  .navbar-theme-slack .navbar-nav .show > .nav-link.active,
  .navbar-theme-slack .navbar-nav .show > .nav-link:hover,
  .navbar-theme-slack .navbar-nav .dropdown-item,
  .navbar-theme-slack .navbar-nav .dropdown-item:focus,
  .navbar-theme-slack .navbar-nav .dropdown-item.active,
  .navbar-theme-slack .navbar-nav .dropdown-item:hover,
  .navbar-theme-slack .navbar-nav .list-group-item,
  .navbar-theme-slack .navbar-nav .list-group-item:focus,
  .navbar-theme-slack .navbar-nav .list-group-item.active,
  .navbar-theme-slack .navbar-nav .list-group-item:hover {
        color: #31344b;
        background: transparent;
    }

    .navbar-theme-slack .navbar-nav .nav-link.disabled,
  .navbar-theme-slack .navbar-nav .show > .nav-link.disabled,
  .navbar-theme-slack .navbar-nav .dropdown-item.disabled,
  .navbar-theme-slack .navbar-nav .list-group-item.disabled {
        color: rgba(82, 84, 128, 0.9);
    }

    .navbar-theme-slack .navbar-nav .dropdown .dropdown-menu {
        padding: 5px 15px;
    }

    .navbar-theme-slack .navbar-nav .dropdown-item {
        font-size: 1rem;
    }

    .navbar-theme-slack .navbar-nav .dropdown:not(.mega-dropdown) .dropdown-item {
        padding-left: 8px;
        margin-bottom: 5px;
        border-radius: 0.55rem;
    }
}

.navbar-transparent {
    background-color: transparent;
    border: 0;
}

@media (min-width: 992px) {
    .navbar-nav .nav-item {
        margin-right: .5rem;
    }

    .navbar-nav .nav-item [data-toggle="dropdown"]::after {
        transition: all 0.2s ease;
    }

    .navbar-nav .nav-item.show [data-toggle="dropdown"]::after {
        transform: rotate(180deg);
    }

    .navbar-nav .nav-link {
        padding-top: 1rem;
        padding-bottom: 1rem;
        border-radius: 0.55rem;
    }

    .navbar-nav .nav-link i {
        margin-right: .3rem;
        font-size: 0.75rem;
    }

    .navbar-nav .nav-link-icon {
        padding-left: .5rem;
        padding-right: .5rem;
        font-size: 1rem;
        border-radius: 0.55rem;
    }

    .navbar-nav .nav-link-icon i {
        margin-right: 0;
    }

    .navbar-nav .dropdown-menu {
        opacity: 0;
        pointer-events: none;
        margin: 0;
        border-radius: 0.55rem;
    }

    .navbar-nav .dropdown-menu-right:before {
        right: 20px;
        left: auto;
    }

    .navbar-nav .dropdown-menu.show {
        opacity: 1;
        pointer-events: auto;
        animation: show-navbar-dropdown .25s ease forwards;
    }

    .navbar-nav .dropdown-menu.close {
        display: block;
        animation: hide-navbar-dropdown .15s ease backwards;
    }

    .navbar-nav .dropdown-menu {
        display: block;
        opacity: 0;
        pointer-events: none;
        transition: all 0.2s ease;
    }

    .navbar-nav .dropdown:hover > .dropdown-menu,
  .navbar-nav .dropdown-submenu:hover > .dropdown-menu {
        display: block;
        opacity: 1;
        pointer-events: auto;
    }

    .navbar-nav .dropdown:hover .nav-link > .nav-link-arrow {
        transform: rotate(180deg);
    }

    .navbar-nav .dropdown-submenu:hover .dropdown-item > .nav-link-arrow {
        transform: rotate(90deg);
    }

    .navbar-nav .dropdown-menu-inner {
        position: relative;
        padding: 1rem;
    }

    .navbar-transparent .navbar-nav .nav-link.disabled {
        color: rgba(236, 240, 243, 0.25);
    }

    .navbar-transparent .navbar-brand {
        color: #31344b;
    }

    .navbar-transparent .navbar-brand:hover, .navbar-transparent .navbar-brand:focus {
        color: #31344b;
    }
}

.navbar-collapse-header {
    display: none;
}

@media (max-width: 991.98px) {
    .navbar-nav .nav-link {
        padding: .625rem 0;
        display: flex;
        -moz-justify-content: space-between;
        -ms-justify-content: space-between;
        justify-content: space-between;
        -ms-flex-pack: space-between;
    }

    .navbar-nav .dropdown-menu {
        box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
        min-width: auto;
    }

    .navbar-nav .dropdown-menu .media svg {
        width: 30px;
    }

    .navbar-collapse {
        width: 100%;
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        z-index: 1050;
        overflow-y: auto;
        height: calc(100vh - 30px) !important;
        opacity: 0;
    }

    .navbar-collapse .navbar-toggler {
        position: relative;
        display: inline-block;
        width: 20px;
        height: 20px;
        padding: 0;
    }

    .navbar-collapse .navbar-toggler span {
        display: block;
        position: absolute;
        width: 100%;
        height: 2px;
        border-radius: 2px;
        opacity: 1;
        background: #283448;
    }

    .navbar-collapse .navbar-collapse-header {
        display: block;
        padding-bottom: 1rem;
        margin-bottom: 1rem;
    }

    .navbar-collapse .collapse-brand img {
        height: 25px;
    }

    .navbar-collapse .collapse-close {
        text-align: right;
    }

    .dropdown.show .nav-link > .nav-link-arrow {
        transform: rotate(180deg);
    }

    .dropdown-submenu.show .dropdown-item > .nav-link-arrow {
        transform: rotate(90deg);
    }

    .navbar-collapse.collapsing,
  .navbar-collapse.show {
        padding: 1.5rem;
        color: #31344b;
        border-radius: 0.55rem;
        background: #e6e7ee;
        animation: show-navbar-collapse .2s ease forwards;
        box-shadow: 6px 6px 12px #b8b9be, -6px -6px 12px #ffffff;
    }

    .navbar-collapse.collapsing-out {
        animation: hide-navbar-collapse .2s ease forwards;
    }
}

/**
 * = Sections
 */
.section {
    position: relative;
    padding-top: 3rem;
    padding-bottom: 3rem;
}

.section-header {
    position: relative;
    padding-top: 6rem;
    padding-bottom: 3rem;
}

@media (min-width: 576px) {
    .section {
        position: relative;
        padding-top: 6rem;
        padding-bottom: 6rem;
    }

    .section-header {
        position: relative;
        padding-top: 10rem;
        padding-bottom: 10rem;
    }

    .section-header.section-sm {
        padding-top: 4rem;
        padding-bottom: 3rem;
    }

    .section-xl {
        padding-top: 10rem;
        padding-bottom: 10rem;
    }

    .section-lg {
        padding-top: 8rem;
        padding-bottom: 8rem;
    }

    .section-sm {
        padding-top: 4rem;
        padding-bottom: 4rem;
    }
}

@media (min-width: 768px) {
    .section-hero {
        height: 100vh;
    }
}

.section-profile-cover {
    height: 580px;
    background-size: cover;
    background-position: center center;
}

@media (max-width: 991.98px) {
    .section-profile-cover {
        height: 400px;
    }
}

.components-section > .form-control + .form-control {
    margin-top: .5rem;
}

.components-section > .nav + .nav,
.components-section > .alert + .alert,
.components-section > .navbar + .navbar,
.components-section > .progress + .progress,
.components-section > .progress + .btn,
.components-section .badge,
.components-section .btn {
    margin-right: .75rem;
    margin-bottom: .75rem;
}

.components-section .btn-group {
    margin-top: .5rem;
    margin-bottom: .5rem;
}

.components-section .btn-group .btn {
    margin: 0;
}

.components-section .alert {
    margin: 0;
}

.components-section .alert + .alert {
    margin-top: 1.25rem;
}

.components-section .badge {
    margin-right: .5rem;
}

.components-section .modal-footer .btn {
    margin: 0;
}

.card-box {
    -o-perspective: 900px;
    perspective: 900px;
    width: 250px;
    position: relative;
}

.card-box .card-component {
    transform-style: preserve-3d;
    position: relative;
    height: 300px;
}

@media (min-width: 992px) {
    .card-box .card-component {
        height: 450px;
    }
}

.card-box .card-component.card-component-lg {
    height: auto;
    max-height: 800px;
}

@media (min-width: 768px) {
    .card-box .card-component.card-component-lg {
        max-height: 410px;
    }
}

.card-box .card-component.card-component-xs {
    height: auto;
    max-height: 230px;
}

.card-box .card-component .front {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    overflow: hidden;
    box-shadow: 3px 3px 6px #b8b9be, -3px -3px 6px #ffffff;
    border-radius: 0.55rem;
}

.card-box .card-component .front:hover {
    cursor: pointer;
}

.card-box .page-card {
    box-shadow: 3px 3px 6px #b8b9be, -3px -3px 6px #ffffff;
    border-radius: 0.55rem;
}

.card-box .page-card:hover {
    cursor: pointer;
}

@media (max-width: 991.98px) {
    .card-box {
        width: 200px;
    }
}

@media (min-width: 992px) {
    .card-box {
        width: 260px;
    }
}

.copy-docs {
    position: absolute;
    top: 5px;
    right: 5px;
    transition: all 0.2s ease;
}

.copy-docs.copied {
    background: #18634B;
}

.copy-docs:hover {
    cursor: pointer;
}

.index-icon {
    position: absolute;
    font-size: 38px;
    color: #dcdcdc;
    transition: 0.3s all ease;
}

.index-icon-javascript {
    bottom: 80px;
    left: 40px;
}

.index-icon-javascript:hover {
    color: #f1da1c;
}

.index-icon-bootstrap {
    bottom: -150px;
    right: -7%;
}

.index-icon-bootstrap:hover {
    color: #553d7c;
}

.icon-sass:hover {
    color: #CD6799;
}

.index-icon-code {
    bottom: 180px;
    left: -80px;
}

.index-icon-code:hover {
    color: #ff7f66;
}

.index-icon-gulp:hover {
    color: #e34a4f;
}

.index-icon-gulp {
    left: 250px;
    bottom: -10px;
}

.index-icon-html5 {
    right: 30px;
    bottom: 150px;
}

.index-icon-html5:hover {
    color: #e54b20;
}

.index-icon-css3 {
    right: 40px;
    bottom: -20px;
}

.index-icon-css3:hover {
    color: #e54b20;
}

.index-icon-npm {
    right: 180px;
    bottom: 20px;
}

.index-icon-npm:hover {
    color: #cc3f3d;
}

.index-icon-fontawesome {
    right: 340px;
    bottom: -40px;
}

.index-icon-fontawesome:hover {
    color: #3499EF;
}

.index-icon-illustrations {
    left: 20px;
    bottom: -40px;
}

.index-icon-illustrations:hover {
    color: #2D4CC8;
}

/**
 * = Footers
 */
.footer-links li {
    display: block;
    margin-left: -5px;
}

.footer-links li:hover a {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.footer-links li a {
    display: block;
    border-radius: 0.55rem;
    padding: 5px;
}

.footer-links li a:hover {
    color: inherit !important;
}

.footer-brand {
    font-size: 1.25rem;
    font-weight: 600;
}

.footer-brand img, .footer-brand svg {
    width: 40px;
}

.footer-brand:hover, .footer-brand:focus {
    color: #262833;
}

.copyright {
    font-size: 0.875rem;
}

#producthunt-badge {
    position: fixed;
    bottom: 25px;
    right: 25px;
    z-index: 99;
}

@media (max-width: 767.98px) {
    #producthunt-badge {
        display: none;
    }
}

/**
 * = Sidebars
 */
#doc-index:not(.collapse.show), .doc-sidebar {
    display: none;
}

@media (min-width: 992px) {
    #doc-index {
        display: block;
    }

    .doc-sidebar {
        display: block;
        height: calc(100vh - 2rem);
        overflow-y: scroll;
        position: sticky;
        top: 2rem;
    }

    .doc-sidebar .nav-link[data-toggle="collapse"] > .icon {
        transform: rotateZ(-90deg);
        position: relative;
        right: .25rem;
    }

    .doc-sidebar .nav .nav-item {
        font-size: 0.875rem;
    }
}

/**
 * = Accordions
 */
.accordion .card {
    margin-bottom: 1.5rem;
}

.accordion-panel-header {
    display: flex;
    -moz-justify-content: space-between;
    -ms-justify-content: space-between;
    justify-content: space-between;
    -ms-flex-pack: space-between;
    -moz-align-items: center;
    -ms-align-items: center;
    align-items: center;
    -webkit-user-select: none;
    user-select: none;
}

.accordion-panel-header .icon {
    color: #31344b;
    transition: all 0.2s ease;
}

.accordion-panel-header .icon span {
    font-size: 0.875rem;
}

.accordion-panel-header .icon-title {
    margin-right: 1rem;
}

.accordion-panel-header .icon-title span {
    margin-right: 1rem;
}

.accordion-panel-header .icon-title + .icon {
    height: 1rem;
}

.accordion-panel-header[aria-expanded="true"] > .icon {
    transform: rotateZ(45deg);
}

.accordion-panel-header[aria-expanded="true"] > *, .accordion-panel-header:hover > * {
    color: #262833;
}

.accordion-panel-header[aria-expanded="true"] > * span, .accordion-panel-header:hover > * span {
    fill: #262833;
}

.accordion-panel-header:hover {
    cursor: pointer;
}

/**
 * = Alerts
 */
.alert {
    padding: 1rem 1.5rem;
    border: #44476A;
    font-size: 0.875rem;
    border: 0.0625rem solid #D1D9E6;
}

.alert.alert-sm {
    padding: .5rem 1rem;
}

.alert .alert-inner--icon {
    font-size: 1.25rem;
    margin-right: .375rem;
}

.alert .alert-inner--text {
    display: inline-block;
}

.alert .alert-inner--text a {
    font-weight: 600;
}

.alert-heading {
    font-weight: 600;
    font-size: 1.5rem;
}

.alert-dismissible .close {
    top: 50%;
    right: 1.5rem;
    padding: 0;
    transform: translateY(-50%);
    color: #31344b;
    opacity: 1;
}

@media (max-width: 575.98px) {
    .alert-dismissible .close {
        top: 1rem;
        right: .5rem;
    }
}

.alert-dismissible .close > span:not(.sr-only) {
    font-size: 1.5rem;
    background-color: transparent;
    color: #44476A;
}

.alert-primary {
    background: #e6e7ee;
    color: #e6e7ee;
}

.alert-secondary {
    background: #e6e7ee;
    color: #2D4CC8;
}

.alert-success {
    background: #e6e7ee;
    color: #18634B;
}

.alert-info {
    background: #e6e7ee;
    color: #0056B3;
}

.alert-warning {
    background: #e6e7ee;
    color: #F0B400;
}

.alert-danger {
    background: #e6e7ee;
    color: #A91E2C;
}

.alert-light {
    background: #e6e7ee;
    color: #D1D9E6;
}

.alert-dark {
    background: #e6e7ee;
    color: #31344b;
}

.alert-default {
    background: #e6e7ee;
    color: #262833;
}

.alert-white {
    background: #e6e7ee;
    color: #ECF0F3;
}

.alert-gray {
    background: #e6e7ee;
    color: #44476A;
}

.alert-neutral {
    background: #e6e7ee;
    color: #ECF0F3;
}

.alert-soft {
    background: #e6e7ee;
    color: #e6e7ee;
}

.alert-black {
    background: #e6e7ee;
    color: #262833;
}

.alert-purple {
    background: #e6e7ee;
    color: #6f42c1;
}

.alert-gray-100 {
    background: #e6e7ee;
    color: #f3f7fa;
}

.alert-gray-200 {
    background: #e6e7ee;
    color: #fafbfe;
}

.alert-gray-300 {
    background: #e6e7ee;
    color: #e6e7ee;
}

.alert-gray-400 {
    background: #e6e7ee;
    color: #D1D9E6;
}

.alert-gray-500 {
    background: #e6e7ee;
    color: #b1bcce;
}

.alert-gray-600 {
    background: #e6e7ee;
    color: #93a5be;
}

.alert-gray-700 {
    background: #e6e7ee;
    color: #66799e;
}

.alert-gray-800 {
    background: #e6e7ee;
    color: #525480;
}

.alert-facebook {
    background: #e6e7ee;
    color: #3b5999;
}

.alert-dribbble {
    background: #e6e7ee;
    color: #ea4c89;
}

.alert-github {
    background: #e6e7ee;
    color: #222222;
}

.alert-behance {
    background: #e6e7ee;
    color: #0057ff;
}

.alert-twitter {
    background: #e6e7ee;
    color: #1da1f2;
}

.alert-slack {
    background: #e6e7ee;
    color: #3aaf85;
}

/**
 * = Avatars
 */
.avatar + .avatar-content {
    display: inline-block;
    margin-left: .75rem;
}

.avatar-link img {
    width: 4rem;
    height: 4rem;
}

.avatar-group .avatar {
    position: relative;
    z-index: 2;
    border: 2px solid #e6e7ee;
}

.avatar-group .avatar:hover {
    z-index: 3;
}

.avatar-group .avatar + .avatar {
    margin-left: -1rem;
}

/**
 * = Badges
 */
.badge {
    font-size: 0.7rem;
    font-weight: 600;
    border: 0.0625rem solid #D1D9E6;
}

.badge a {
    color: #ECF0F3;
}

.badge-pill {
    padding-right: 0.875em;
    padding-left: 0.875em;
}

.badge-inline {
    margin-right: .625rem;
}

.badge-inline + span {
    top: 2px;
    position: relative;
}

.badge-inline + span > a {
    text-decoration: underline;
}

.badge-md {
    padding: .4rem .55rem;
}

.badge-lg {
    padding: .65rem .85rem;
}

.wi-tags a {
    background-color: #e6e7ee;
    display: inline-block;
    padding: 0.125rem 0.875rem;
    margin: 0.45rem;
    line-height: 2;
    font-size: 0.875rem;
    box-shadow: 3px 3px 6px #b8b9be, -3px -3px 6px #ffffff;
    border-radius: 0.55rem;
}

.presentation-badge {
    position: relative;
    font-size: 1.25rem;
    text-transform: uppercase;
    font-weight: 600;
    right: -15px;
    padding: 5px 14px;
    top: -45px;
    background: #ECF0F3;
    border-radius: 0.55rem;
    box-shadow: 0 0.125rem 0.25rem rgba(38, 40, 51, 0.075);
}

@media (max-width: 991.98px) {
    .presentation-badge {
        font-size: 0.875rem;
        right: -13px;
        padding: 5px 10px;
        top: -23px;
    }
}

.badge-primary {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #e6e7ee;
}

a.badge-primary:hover, a.badge-primary:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-secondary {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #2D4CC8;
}

a.badge-secondary:hover, a.badge-secondary:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-success {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #18634B;
}

a.badge-success:hover, a.badge-success:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-info {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #0056B3;
}

a.badge-info:hover, a.badge-info:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-warning {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #F0B400;
}

a.badge-warning:hover, a.badge-warning:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-danger {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #A91E2C;
}

a.badge-danger:hover, a.badge-danger:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-light {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #D1D9E6;
}

a.badge-light:hover, a.badge-light:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-dark {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #31344b;
}

a.badge-dark:hover, a.badge-dark:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-default {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #262833;
}

a.badge-default:hover, a.badge-default:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-white {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #ECF0F3;
}

a.badge-white:hover, a.badge-white:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-gray {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #44476A;
}

a.badge-gray:hover, a.badge-gray:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-neutral {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #ECF0F3;
}

a.badge-neutral:hover, a.badge-neutral:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-soft {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #e6e7ee;
}

a.badge-soft:hover, a.badge-soft:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-black {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #262833;
}

a.badge-black:hover, a.badge-black:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-purple {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #6f42c1;
}

a.badge-purple:hover, a.badge-purple:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-gray-100 {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #f3f7fa;
}

a.badge-gray-100:hover, a.badge-gray-100:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-gray-200 {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #fafbfe;
}

a.badge-gray-200:hover, a.badge-gray-200:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-gray-300 {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #e6e7ee;
}

a.badge-gray-300:hover, a.badge-gray-300:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-gray-400 {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #D1D9E6;
}

a.badge-gray-400:hover, a.badge-gray-400:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-gray-500 {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #b1bcce;
}

a.badge-gray-500:hover, a.badge-gray-500:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-gray-600 {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #93a5be;
}

a.badge-gray-600:hover, a.badge-gray-600:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-gray-700 {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #66799e;
}

a.badge-gray-700:hover, a.badge-gray-700:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-gray-800 {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #525480;
}

a.badge-gray-800:hover, a.badge-gray-800:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-facebook {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #3b5999;
}

a.badge-facebook:hover, a.badge-facebook:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-dribbble {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #ea4c89;
}

a.badge-dribbble:hover, a.badge-dribbble:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-github {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #222222;
}

a.badge-github:hover, a.badge-github:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-behance {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #0057ff;
}

a.badge-behance:hover, a.badge-behance:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-twitter {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #1da1f2;
}

a.badge-twitter:hover, a.badge-twitter:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

.badge-slack {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    color: #3aaf85;
}

a.badge-slack:hover, a.badge-slack:focus {
    color: #31344b;
    background-color: #e6e7ee;
}

/**
 * = Buttons
 */
.btn {
    position: relative;
    transition: all 0.2s ease;
    letter-spacing: 0.025em;
    font-size: 1rem;
    border-color: #D1D9E6;
    box-shadow: 3px 3px 6px #b8b9be, -3px -3px 6px #ffffff;
}

.btn.btn-pill {
    border-radius: 2rem;
}

.btn.btn-circle {
    border-radius: 50%;
}

.btn-group .btn, .input-group .btn {
    margin-right: 0;
    transform: translateY(0);
}

.btn .toggle-arrow {
    transition: all 0.2s ease;
}

.btn[aria-expanded="true"] .toggle-arrow {
    transform: rotate(180deg);
}

.btn.btn-dropdown {
    box-shadow: 3px 3px 6px #b8b9be, -3px -3px 6px #ffffff;
}

.btn-group > .btn:not(:first-child),
.btn-group > .btn-group:not(:first-child) {
    box-shadow: 3px 3px 6px #b8b9be, 0px -3px 6px #ffffff;
}

.btn-xs {
    padding: 0.25rem 0.45rem;
    box-shadow: 3px 3px 6px #b8b9be, -3px -3px 6px #ffffff;
    line-height: 1.8;
}

.btn-xs, .btn-xs i {
    font-size: 0.75rem !important;
}

.btn-sm, .btn-group-sm > .btn, .btn-sm i, .btn-group-sm > .btn i {
    font-size: 0.875rem !important;
}

.btn-md, .btn-md i {
    font-size: 0.1rem !important;
}

.btn-lg, .btn-group-lg > .btn, .btn-lg i, .btn-group-lg > .btn i {
    font-size: 1.25rem !important;
}

[class*="btn-outline-"] {
    border-width: 2px;
}

.btn-outline-secondary {
    color: #2D4CC8;
}

.btn-inner-icon i:not(.fa) {
    position: relative;
}

.btn-link {
    font-weight: 400;
    box-shadow: none;
    padding: 0;
}

.btn-link:hover, .btn-link:focus, .btn-link:active {
    background-color: transparent;
    box-shadow: none;
    transform: none;
}

.btn-icon {
    display: inline-block;
}

.btn-icon .btn-inner-icon:first-of-type {
    margin-right: .3rem;
}

.btn-icon .btn-inner-icon:last-of-type {
    margin-left: .3rem;
}

.btn-icon-only {
    position: relative;
    width: 2.575rem;
    height: 2.575rem;
    padding: 0;
}

.btn-icon-only span, .btn-icon-only i {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.btn-icon-onlya {
    line-height: 2.5;
}

.btn-icon-only.btn-xs {
    width: 1.7rem;
    height: 1.7rem;
}

.btn-icon-only.btn-sm, .btn-group-sm > .btn-icon-only.btn {
    width: 2rem;
    height: 2rem;
}

.spinner-border,
.spinner-brow {
    vertical-align: middle;
}

.btn-loading-overlay .spinner {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    opacity: 0;
}

.btn-loading-overlay .btn-inner-text,
.btn-loading-overlay .spinner {
    transition: all 0.2s ease;
}

.btn-loading-overlay .btn-inner-text {
    opacity: 1;
}

.btn-loading-overlay.btn-loading .spinner {
    opacity: 1;
}

.btn-loading-overlay.btn-loading .btn-inner-text {
    opacity: 0;
}

.btn-group .dropdown-arrow,
.btn-vertical .dropdown-arrow {
    transition: all 0.2s ease;
}

.btn-group.show .dropdown-arrow,
.btn-vertical.show .dropdown-arrow {
    transform: rotate(180deg);
}

.btn-group.show.dropright .dropdown-arrow,
.btn-vertical.show.dropright .dropdown-arrow {
    transform: rotate(90deg);
}

.btn-group.show.dropleft .dropdown-arrow,
.btn-vertical.show.dropleft .dropdown-arrow {
    transform: rotate(-90deg);
}

.btn-group > .btn:hover,
.btn-vertical > .btn:hover {
    z-index: 0;
}

.btn-group > .btn:focus, .btn-group > .btn:active, .btn-group > .btn.active,
.btn-vertical > .btn:focus,
.btn-vertical > .btn:active,
.btn-vertical > .btn.active {
    z-index: 0;
}

.btn-primary {
    color: #31344b;
    background-color: #e6e7ee;
}

.btn-primary:hover {
    color: #31344b;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-primary.disabled, .btn-primary:disabled {
    color: #31344b;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
}

.btn-primary:focus, .btn-primary.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-primary:not(:disabled):not(.disabled):active, .btn-primary:not(:disabled):not(.disabled).active,
  .show > .btn-primary.dropdown-toggle {
    color: #31344b;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
}

.btn-primary:not(:disabled):not(.disabled):active:focus, .btn-primary:not(:disabled):not(.disabled).active:focus,
    .show > .btn-primary.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-secondary {
    color: #ECF0F3;
    background-color: #2D4CC8;
}

.btn-secondary:hover {
    color: #ECF0F3;
    background-color: #2d4cc8;
    border-color: #2d4cc8;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-secondary.disabled, .btn-secondary:disabled {
    color: #ECF0F3;
    background-color: #2D4CC8;
    border-color: #2D4CC8;
}

.btn-secondary:focus, .btn-secondary.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-secondary:not(:disabled):not(.disabled):active, .btn-secondary:not(:disabled):not(.disabled).active,
  .show > .btn-secondary.dropdown-toggle {
    color: #ECF0F3;
    background-color: #2D4CC8;
    border-color: #2d4cc8;
}

.btn-secondary:not(:disabled):not(.disabled):active:focus, .btn-secondary:not(:disabled):not(.disabled).active:focus,
    .show > .btn-secondary.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-success {
    color: #ECF0F3;
    background-color: #18634B;
}

.btn-success:hover {
    color: #ECF0F3;
    background-color: #18634b;
    border-color: #18634b;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-success.disabled, .btn-success:disabled {
    color: #ECF0F3;
    background-color: #18634B;
    border-color: #18634B;
}

.btn-success:focus, .btn-success.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-success:not(:disabled):not(.disabled):active, .btn-success:not(:disabled):not(.disabled).active,
  .show > .btn-success.dropdown-toggle {
    color: #ECF0F3;
    background-color: #18634B;
    border-color: #18634b;
}

.btn-success:not(:disabled):not(.disabled):active:focus, .btn-success:not(:disabled):not(.disabled).active:focus,
    .show > .btn-success.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-info {
    color: #ECF0F3;
    background-color: #0056B3;
}

.btn-info:hover {
    color: #ECF0F3;
    background-color: #0056b3;
    border-color: #0056b3;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-info.disabled, .btn-info:disabled {
    color: #ECF0F3;
    background-color: #0056B3;
    border-color: #0056B3;
}

.btn-info:focus, .btn-info.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-info:not(:disabled):not(.disabled):active, .btn-info:not(:disabled):not(.disabled).active,
  .show > .btn-info.dropdown-toggle {
    color: #ECF0F3;
    background-color: #0056B3;
    border-color: #0056b3;
}

.btn-info:not(:disabled):not(.disabled):active:focus, .btn-info:not(:disabled):not(.disabled).active:focus,
    .show > .btn-info.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-warning {
    color: #ECF0F3;
    background-color: #F0B400;
}

.btn-warning:hover {
    color: #ECF0F3;
    background-color: #f0b400;
    border-color: #f0b400;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-warning.disabled, .btn-warning:disabled {
    color: #ECF0F3;
    background-color: #F0B400;
    border-color: #F0B400;
}

.btn-warning:focus, .btn-warning.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-warning:not(:disabled):not(.disabled):active, .btn-warning:not(:disabled):not(.disabled).active,
  .show > .btn-warning.dropdown-toggle {
    color: #ECF0F3;
    background-color: #F0B400;
    border-color: #f0b400;
}

.btn-warning:not(:disabled):not(.disabled):active:focus, .btn-warning:not(:disabled):not(.disabled).active:focus,
    .show > .btn-warning.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-danger {
    color: #ECF0F3;
    background-color: #A91E2C;
}

.btn-danger:hover {
    color: #ECF0F3;
    background-color: #a91e2c;
    border-color: #a91e2c;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-danger.disabled, .btn-danger:disabled {
    color: #ECF0F3;
    background-color: #A91E2C;
    border-color: #A91E2C;
}

.btn-danger:focus, .btn-danger.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-danger:not(:disabled):not(.disabled):active, .btn-danger:not(:disabled):not(.disabled).active,
  .show > .btn-danger.dropdown-toggle {
    color: #ECF0F3;
    background-color: #A91E2C;
    border-color: #a91e2c;
}

.btn-danger:not(:disabled):not(.disabled):active:focus, .btn-danger:not(:disabled):not(.disabled).active:focus,
    .show > .btn-danger.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-light {
    color: #31344b;
    background-color: #D1D9E6;
}

.btn-light:hover {
    color: #31344b;
    background-color: #d1d9e6;
    border-color: #d1d9e6;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-light.disabled, .btn-light:disabled {
    color: #31344b;
    background-color: #D1D9E6;
    border-color: #D1D9E6;
}

.btn-light:focus, .btn-light.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-light:not(:disabled):not(.disabled):active, .btn-light:not(:disabled):not(.disabled).active,
  .show > .btn-light.dropdown-toggle {
    color: #31344b;
    background-color: #D1D9E6;
    border-color: #d1d9e6;
}

.btn-light:not(:disabled):not(.disabled):active:focus, .btn-light:not(:disabled):not(.disabled).active:focus,
    .show > .btn-light.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-dark {
    color: #ECF0F3;
    background-color: #31344b;
}

.btn-dark:hover {
    color: #ECF0F3;
    background-color: #31344b;
    border-color: #31344b;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-dark.disabled, .btn-dark:disabled {
    color: #ECF0F3;
    background-color: #31344b;
    border-color: #31344b;
}

.btn-dark:focus, .btn-dark.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-dark:not(:disabled):not(.disabled):active, .btn-dark:not(:disabled):not(.disabled).active,
  .show > .btn-dark.dropdown-toggle {
    color: #ECF0F3;
    background-color: #31344b;
    border-color: #31344b;
}

.btn-dark:not(:disabled):not(.disabled):active:focus, .btn-dark:not(:disabled):not(.disabled).active:focus,
    .show > .btn-dark.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-default {
    color: #ECF0F3;
    background-color: #262833;
}

.btn-default:hover {
    color: #ECF0F3;
    background-color: #262833;
    border-color: #262833;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-default.disabled, .btn-default:disabled {
    color: #ECF0F3;
    background-color: #262833;
    border-color: #262833;
}

.btn-default:focus, .btn-default.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-default:not(:disabled):not(.disabled):active, .btn-default:not(:disabled):not(.disabled).active,
  .show > .btn-default.dropdown-toggle {
    color: #ECF0F3;
    background-color: #262833;
    border-color: #262833;
}

.btn-default:not(:disabled):not(.disabled):active:focus, .btn-default:not(:disabled):not(.disabled).active:focus,
    .show > .btn-default.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-white {
    color: #31344b;
    background-color: #ECF0F3;
}

.btn-white:hover {
    color: #31344b;
    background-color: #ecf0f3;
    border-color: #ecf0f3;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-white.disabled, .btn-white:disabled {
    color: #31344b;
    background-color: #ECF0F3;
    border-color: #ECF0F3;
}

.btn-white:focus, .btn-white.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-white:not(:disabled):not(.disabled):active, .btn-white:not(:disabled):not(.disabled).active,
  .show > .btn-white.dropdown-toggle {
    color: #31344b;
    background-color: #ECF0F3;
    border-color: #ecf0f3;
}

.btn-white:not(:disabled):not(.disabled):active:focus, .btn-white:not(:disabled):not(.disabled).active:focus,
    .show > .btn-white.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray {
    color: #ECF0F3;
    background-color: #44476A;
}

.btn-gray:hover {
    color: #ECF0F3;
    background-color: #44476a;
    border-color: #44476a;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray.disabled, .btn-gray:disabled {
    color: #ECF0F3;
    background-color: #44476A;
    border-color: #44476A;
}

.btn-gray:focus, .btn-gray.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray:not(:disabled):not(.disabled):active, .btn-gray:not(:disabled):not(.disabled).active,
  .show > .btn-gray.dropdown-toggle {
    color: #ECF0F3;
    background-color: #44476A;
    border-color: #44476a;
}

.btn-gray:not(:disabled):not(.disabled):active:focus, .btn-gray:not(:disabled):not(.disabled).active:focus,
    .show > .btn-gray.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-neutral {
    color: #31344b;
    background-color: #ECF0F3;
}

.btn-neutral:hover {
    color: #31344b;
    background-color: #ecf0f3;
    border-color: #ecf0f3;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-neutral.disabled, .btn-neutral:disabled {
    color: #31344b;
    background-color: #ECF0F3;
    border-color: #ECF0F3;
}

.btn-neutral:focus, .btn-neutral.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-neutral:not(:disabled):not(.disabled):active, .btn-neutral:not(:disabled):not(.disabled).active,
  .show > .btn-neutral.dropdown-toggle {
    color: #31344b;
    background-color: #ECF0F3;
    border-color: #ecf0f3;
}

.btn-neutral:not(:disabled):not(.disabled):active:focus, .btn-neutral:not(:disabled):not(.disabled).active:focus,
    .show > .btn-neutral.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-soft {
    color: #31344b;
    background-color: #e6e7ee;
}

.btn-soft:hover {
    color: #31344b;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-soft.disabled, .btn-soft:disabled {
    color: #31344b;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
}

.btn-soft:focus, .btn-soft.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-soft:not(:disabled):not(.disabled):active, .btn-soft:not(:disabled):not(.disabled).active,
  .show > .btn-soft.dropdown-toggle {
    color: #31344b;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
}

.btn-soft:not(:disabled):not(.disabled):active:focus, .btn-soft:not(:disabled):not(.disabled).active:focus,
    .show > .btn-soft.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-black {
    color: #ECF0F3;
    background-color: #262833;
}

.btn-black:hover {
    color: #ECF0F3;
    background-color: #262833;
    border-color: #262833;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-black.disabled, .btn-black:disabled {
    color: #ECF0F3;
    background-color: #262833;
    border-color: #262833;
}

.btn-black:focus, .btn-black.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-black:not(:disabled):not(.disabled):active, .btn-black:not(:disabled):not(.disabled).active,
  .show > .btn-black.dropdown-toggle {
    color: #ECF0F3;
    background-color: #262833;
    border-color: #262833;
}

.btn-black:not(:disabled):not(.disabled):active:focus, .btn-black:not(:disabled):not(.disabled).active:focus,
    .show > .btn-black.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-purple {
    color: #ECF0F3;
    background-color: #6f42c1;
}

.btn-purple:hover {
    color: #ECF0F3;
    background-color: #6f42c1;
    border-color: #6f42c1;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-purple.disabled, .btn-purple:disabled {
    color: #ECF0F3;
    background-color: #6f42c1;
    border-color: #6f42c1;
}

.btn-purple:focus, .btn-purple.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-purple:not(:disabled):not(.disabled):active, .btn-purple:not(:disabled):not(.disabled).active,
  .show > .btn-purple.dropdown-toggle {
    color: #ECF0F3;
    background-color: #6f42c1;
    border-color: #6f42c1;
}

.btn-purple:not(:disabled):not(.disabled):active:focus, .btn-purple:not(:disabled):not(.disabled).active:focus,
    .show > .btn-purple.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray-100 {
    color: #31344b;
    background-color: #f3f7fa;
}

.btn-gray-100:hover {
    color: #31344b;
    background-color: #f3f7fa;
    border-color: #f3f7fa;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray-100.disabled, .btn-gray-100:disabled {
    color: #31344b;
    background-color: #f3f7fa;
    border-color: #f3f7fa;
}

.btn-gray-100:focus, .btn-gray-100.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray-100:not(:disabled):not(.disabled):active, .btn-gray-100:not(:disabled):not(.disabled).active,
  .show > .btn-gray-100.dropdown-toggle {
    color: #31344b;
    background-color: #f3f7fa;
    border-color: #f3f7fa;
}

.btn-gray-100:not(:disabled):not(.disabled):active:focus, .btn-gray-100:not(:disabled):not(.disabled).active:focus,
    .show > .btn-gray-100.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray-200 {
    color: #31344b;
    background-color: #fafbfe;
}

.btn-gray-200:hover {
    color: #31344b;
    background-color: #fafbfe;
    border-color: #fafbfe;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray-200.disabled, .btn-gray-200:disabled {
    color: #31344b;
    background-color: #fafbfe;
    border-color: #fafbfe;
}

.btn-gray-200:focus, .btn-gray-200.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray-200:not(:disabled):not(.disabled):active, .btn-gray-200:not(:disabled):not(.disabled).active,
  .show > .btn-gray-200.dropdown-toggle {
    color: #31344b;
    background-color: #fafbfe;
    border-color: #fafbfe;
}

.btn-gray-200:not(:disabled):not(.disabled):active:focus, .btn-gray-200:not(:disabled):not(.disabled).active:focus,
    .show > .btn-gray-200.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray-300 {
    color: #31344b;
    background-color: #e6e7ee;
}

.btn-gray-300:hover {
    color: #31344b;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray-300.disabled, .btn-gray-300:disabled {
    color: #31344b;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
}

.btn-gray-300:focus, .btn-gray-300.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray-300:not(:disabled):not(.disabled):active, .btn-gray-300:not(:disabled):not(.disabled).active,
  .show > .btn-gray-300.dropdown-toggle {
    color: #31344b;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
}

.btn-gray-300:not(:disabled):not(.disabled):active:focus, .btn-gray-300:not(:disabled):not(.disabled).active:focus,
    .show > .btn-gray-300.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray-400 {
    color: #31344b;
    background-color: #D1D9E6;
}

.btn-gray-400:hover {
    color: #31344b;
    background-color: #d1d9e6;
    border-color: #d1d9e6;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray-400.disabled, .btn-gray-400:disabled {
    color: #31344b;
    background-color: #D1D9E6;
    border-color: #D1D9E6;
}

.btn-gray-400:focus, .btn-gray-400.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray-400:not(:disabled):not(.disabled):active, .btn-gray-400:not(:disabled):not(.disabled).active,
  .show > .btn-gray-400.dropdown-toggle {
    color: #31344b;
    background-color: #D1D9E6;
    border-color: #d1d9e6;
}

.btn-gray-400:not(:disabled):not(.disabled):active:focus, .btn-gray-400:not(:disabled):not(.disabled).active:focus,
    .show > .btn-gray-400.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray-500 {
    color: #ECF0F3;
    background-color: #b1bcce;
}

.btn-gray-500:hover {
    color: #ECF0F3;
    background-color: #b1bcce;
    border-color: #b1bcce;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray-500.disabled, .btn-gray-500:disabled {
    color: #ECF0F3;
    background-color: #b1bcce;
    border-color: #b1bcce;
}

.btn-gray-500:focus, .btn-gray-500.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray-500:not(:disabled):not(.disabled):active, .btn-gray-500:not(:disabled):not(.disabled).active,
  .show > .btn-gray-500.dropdown-toggle {
    color: #ECF0F3;
    background-color: #b1bcce;
    border-color: #b1bcce;
}

.btn-gray-500:not(:disabled):not(.disabled):active:focus, .btn-gray-500:not(:disabled):not(.disabled).active:focus,
    .show > .btn-gray-500.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray-600 {
    color: #ECF0F3;
    background-color: #93a5be;
}

.btn-gray-600:hover {
    color: #ECF0F3;
    background-color: #93a5be;
    border-color: #93a5be;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray-600.disabled, .btn-gray-600:disabled {
    color: #ECF0F3;
    background-color: #93a5be;
    border-color: #93a5be;
}

.btn-gray-600:focus, .btn-gray-600.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray-600:not(:disabled):not(.disabled):active, .btn-gray-600:not(:disabled):not(.disabled).active,
  .show > .btn-gray-600.dropdown-toggle {
    color: #ECF0F3;
    background-color: #93a5be;
    border-color: #93a5be;
}

.btn-gray-600:not(:disabled):not(.disabled):active:focus, .btn-gray-600:not(:disabled):not(.disabled).active:focus,
    .show > .btn-gray-600.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray-700 {
    color: #ECF0F3;
    background-color: #66799e;
}

.btn-gray-700:hover {
    color: #ECF0F3;
    background-color: #66799e;
    border-color: #66799e;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray-700.disabled, .btn-gray-700:disabled {
    color: #ECF0F3;
    background-color: #66799e;
    border-color: #66799e;
}

.btn-gray-700:focus, .btn-gray-700.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray-700:not(:disabled):not(.disabled):active, .btn-gray-700:not(:disabled):not(.disabled).active,
  .show > .btn-gray-700.dropdown-toggle {
    color: #ECF0F3;
    background-color: #66799e;
    border-color: #66799e;
}

.btn-gray-700:not(:disabled):not(.disabled):active:focus, .btn-gray-700:not(:disabled):not(.disabled).active:focus,
    .show > .btn-gray-700.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray-800 {
    color: #ECF0F3;
    background-color: #525480;
}

.btn-gray-800:hover {
    color: #ECF0F3;
    background-color: #525480;
    border-color: #525480;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray-800.disabled, .btn-gray-800:disabled {
    color: #ECF0F3;
    background-color: #525480;
    border-color: #525480;
}

.btn-gray-800:focus, .btn-gray-800.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-gray-800:not(:disabled):not(.disabled):active, .btn-gray-800:not(:disabled):not(.disabled).active,
  .show > .btn-gray-800.dropdown-toggle {
    color: #ECF0F3;
    background-color: #525480;
    border-color: #525480;
}

.btn-gray-800:not(:disabled):not(.disabled):active:focus, .btn-gray-800:not(:disabled):not(.disabled).active:focus,
    .show > .btn-gray-800.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-facebook {
    color: #ECF0F3;
    background-color: #3b5999;
}

.btn-facebook:hover {
    color: #ECF0F3;
    background-color: #3b5999;
    border-color: #3b5999;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-facebook.disabled, .btn-facebook:disabled {
    color: #ECF0F3;
    background-color: #3b5999;
    border-color: #3b5999;
}

.btn-facebook:focus, .btn-facebook.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-facebook:not(:disabled):not(.disabled):active, .btn-facebook:not(:disabled):not(.disabled).active,
  .show > .btn-facebook.dropdown-toggle {
    color: #ECF0F3;
    background-color: #3b5999;
    border-color: #3b5999;
}

.btn-facebook:not(:disabled):not(.disabled):active:focus, .btn-facebook:not(:disabled):not(.disabled).active:focus,
    .show > .btn-facebook.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-dribbble {
    color: #ECF0F3;
    background-color: #ea4c89;
}

.btn-dribbble:hover {
    color: #ECF0F3;
    background-color: #ea4c89;
    border-color: #ea4c89;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-dribbble.disabled, .btn-dribbble:disabled {
    color: #ECF0F3;
    background-color: #ea4c89;
    border-color: #ea4c89;
}

.btn-dribbble:focus, .btn-dribbble.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-dribbble:not(:disabled):not(.disabled):active, .btn-dribbble:not(:disabled):not(.disabled).active,
  .show > .btn-dribbble.dropdown-toggle {
    color: #ECF0F3;
    background-color: #ea4c89;
    border-color: #ea4c89;
}

.btn-dribbble:not(:disabled):not(.disabled):active:focus, .btn-dribbble:not(:disabled):not(.disabled).active:focus,
    .show > .btn-dribbble.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-github {
    color: #ECF0F3;
    background-color: #222222;
}

.btn-github:hover {
    color: #ECF0F3;
    background-color: #222222;
    border-color: #222222;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-github.disabled, .btn-github:disabled {
    color: #ECF0F3;
    background-color: #222222;
    border-color: #222222;
}

.btn-github:focus, .btn-github.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-github:not(:disabled):not(.disabled):active, .btn-github:not(:disabled):not(.disabled).active,
  .show > .btn-github.dropdown-toggle {
    color: #ECF0F3;
    background-color: #222222;
    border-color: #222222;
}

.btn-github:not(:disabled):not(.disabled):active:focus, .btn-github:not(:disabled):not(.disabled).active:focus,
    .show > .btn-github.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-behance {
    color: #ECF0F3;
    background-color: #0057ff;
}

.btn-behance:hover {
    color: #ECF0F3;
    background-color: #0057ff;
    border-color: #0057ff;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-behance.disabled, .btn-behance:disabled {
    color: #ECF0F3;
    background-color: #0057ff;
    border-color: #0057ff;
}

.btn-behance:focus, .btn-behance.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-behance:not(:disabled):not(.disabled):active, .btn-behance:not(:disabled):not(.disabled).active,
  .show > .btn-behance.dropdown-toggle {
    color: #ECF0F3;
    background-color: #0057ff;
    border-color: #0057ff;
}

.btn-behance:not(:disabled):not(.disabled):active:focus, .btn-behance:not(:disabled):not(.disabled).active:focus,
    .show > .btn-behance.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-twitter {
    color: #ECF0F3;
    background-color: #1da1f2;
}

.btn-twitter:hover {
    color: #ECF0F3;
    background-color: #1da1f2;
    border-color: #1da1f2;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-twitter.disabled, .btn-twitter:disabled {
    color: #ECF0F3;
    background-color: #1da1f2;
    border-color: #1da1f2;
}

.btn-twitter:focus, .btn-twitter.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-twitter:not(:disabled):not(.disabled):active, .btn-twitter:not(:disabled):not(.disabled).active,
  .show > .btn-twitter.dropdown-toggle {
    color: #ECF0F3;
    background-color: #1da1f2;
    border-color: #1da1f2;
}

.btn-twitter:not(:disabled):not(.disabled):active:focus, .btn-twitter:not(:disabled):not(.disabled).active:focus,
    .show > .btn-twitter.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-slack {
    color: #ECF0F3;
    background-color: #3aaf85;
}

.btn-slack:hover {
    color: #ECF0F3;
    background-color: #3aaf85;
    border-color: #3aaf85;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-slack.disabled, .btn-slack:disabled {
    color: #ECF0F3;
    background-color: #3aaf85;
    border-color: #3aaf85;
}

.btn-slack:focus, .btn-slack.focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-slack:not(:disabled):not(.disabled):active, .btn-slack:not(:disabled):not(.disabled).active,
  .show > .btn-slack.dropdown-toggle {
    color: #ECF0F3;
    background-color: #3aaf85;
    border-color: #3aaf85;
}

.btn-slack:not(:disabled):not(.disabled):active:focus, .btn-slack:not(:disabled):not(.disabled).active:focus,
    .show > .btn-slack.dropdown-toggle:focus {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.btn-facebook {
    background-color: #e6e7ee;
    color: #3b5999;
    border-color: #D1D9E6;
}

.btn-facebook:hover {
    color: #3b5999;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    border-color: #D1D9E6;
}

.btn-facebook.btn-link {
    color: #3b5999;
    background: transparent;
    border: 0;
    border-style: none;
}

.btn-facebook.btn-link:hover, .btn-facebook.btn-link:focus, .btn-facebook.btn-link.active {
    background-color: none !important;
    border: 0;
    color: #3b5999;
}

.btn-twitter {
    background-color: #e6e7ee;
    color: #1da1f2;
    border-color: #D1D9E6;
}

.btn-twitter:hover {
    color: #1da1f2;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    border-color: #D1D9E6;
}

.btn-twitter.btn-link {
    color: #1da1f2;
    background: transparent;
    border: 0;
    border-style: none;
}

.btn-twitter.btn-link:hover, .btn-twitter.btn-link:focus, .btn-twitter.btn-link.active {
    background-color: none !important;
    border: 0;
    color: #1da1f2;
}

.btn-google-plus {
    background-color: #e6e7ee;
    color: #dd4b39;
    border-color: #D1D9E6;
}

.btn-google-plus:hover {
    color: #dd4b39;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    border-color: #D1D9E6;
}

.btn-google-plus.btn-link {
    color: #dd4b39;
    background: transparent;
    border: 0;
    border-style: none;
}

.btn-google-plus.btn-link:hover, .btn-google-plus.btn-link:focus, .btn-google-plus.btn-link.active {
    background-color: none !important;
    border: 0;
    color: #dd4b39;
}

.btn-instagram {
    background-color: #e6e7ee;
    color: #e4405f;
    border-color: #D1D9E6;
}

.btn-instagram:hover {
    color: #e4405f;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    border-color: #D1D9E6;
}

.btn-instagram.btn-link {
    color: #e4405f;
    background: transparent;
    border: 0;
    border-style: none;
}

.btn-instagram.btn-link:hover, .btn-instagram.btn-link:focus, .btn-instagram.btn-link.active {
    background-color: none !important;
    border: 0;
    color: #e4405f;
}

.btn-pinterest {
    background-color: #e6e7ee;
    color: #bd081c;
    border-color: #D1D9E6;
}

.btn-pinterest:hover {
    color: #bd081c;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    border-color: #D1D9E6;
}

.btn-pinterest.btn-link {
    color: #bd081c;
    background: transparent;
    border: 0;
    border-style: none;
}

.btn-pinterest.btn-link:hover, .btn-pinterest.btn-link:focus, .btn-pinterest.btn-link.active {
    background-color: none !important;
    border: 0;
    color: #bd081c;
}

.btn-youtube {
    background-color: #e6e7ee;
    color: #cd201f;
    border-color: #D1D9E6;
}

.btn-youtube:hover {
    color: #cd201f;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    border-color: #D1D9E6;
}

.btn-youtube.btn-link {
    color: #cd201f;
    background: transparent;
    border: 0;
    border-style: none;
}

.btn-youtube.btn-link:hover, .btn-youtube.btn-link:focus, .btn-youtube.btn-link.active {
    background-color: none !important;
    border: 0;
    color: #cd201f;
}

.btn-slack {
    background-color: #e6e7ee;
    color: #3aaf85;
    border-color: #D1D9E6;
}

.btn-slack:hover {
    color: #3aaf85;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    border-color: #D1D9E6;
}

.btn-slack.btn-link {
    color: #3aaf85;
    background: transparent;
    border: 0;
    border-style: none;
}

.btn-slack.btn-link:hover, .btn-slack.btn-link:focus, .btn-slack.btn-link.active {
    background-color: none !important;
    border: 0;
    color: #3aaf85;
}

.btn-dribbble {
    background-color: #e6e7ee;
    color: #ea4c89;
    border-color: #D1D9E6;
}

.btn-dribbble:hover {
    color: #ea4c89;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    border-color: #D1D9E6;
}

.btn-dribbble.btn-link {
    color: #ea4c89;
    background: transparent;
    border: 0;
    border-style: none;
}

.btn-dribbble.btn-link:hover, .btn-dribbble.btn-link:focus, .btn-dribbble.btn-link.active {
    background-color: none !important;
    border: 0;
    color: #ea4c89;
}

.btn-dropbox {
    background-color: #e6e7ee;
    color: #1E90FF;
    border-color: #D1D9E6;
}

.btn-dropbox:hover {
    color: #1E90FF;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    border-color: #D1D9E6;
}

.btn-dropbox.btn-link {
    color: #1E90FF;
    background: transparent;
    border: 0;
    border-style: none;
}

.btn-dropbox.btn-link:hover, .btn-dropbox.btn-link:focus, .btn-dropbox.btn-link.active {
    background-color: none !important;
    border: 0;
    color: #1E90FF;
}

.btn-twitch {
    background-color: #e6e7ee;
    color: #4B367C;
    border-color: #D1D9E6;
}

.btn-twitch:hover {
    color: #4B367C;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    border-color: #D1D9E6;
}

.btn-twitch.btn-link {
    color: #4B367C;
    background: transparent;
    border: 0;
    border-style: none;
}

.btn-twitch.btn-link:hover, .btn-twitch.btn-link:focus, .btn-twitch.btn-link.active {
    background-color: none !important;
    border: 0;
    color: #4B367C;
}

.btn-paypal {
    background-color: #e6e7ee;
    color: #ecb32c;
    border-color: #D1D9E6;
}

.btn-paypal:hover {
    color: #ecb32c;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    border-color: #D1D9E6;
}

.btn-paypal.btn-link {
    color: #ecb32c;
    background: transparent;
    border: 0;
    border-style: none;
}

.btn-paypal.btn-link:hover, .btn-paypal.btn-link:focus, .btn-paypal.btn-link.active {
    background-color: none !important;
    border: 0;
    color: #ecb32c;
}

.btn-behance {
    background-color: #e6e7ee;
    color: #0057ff;
    border-color: #D1D9E6;
}

.btn-behance:hover {
    color: #0057ff;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    border-color: #D1D9E6;
}

.btn-behance.btn-link {
    color: #0057ff;
    background: transparent;
    border: 0;
    border-style: none;
}

.btn-behance.btn-link:hover, .btn-behance.btn-link:focus, .btn-behance.btn-link.active {
    background-color: none !important;
    border: 0;
    color: #0057ff;
}

.btn-reddit {
    background-color: #e6e7ee;
    color: #E84422;
    border-color: #D1D9E6;
}

.btn-reddit:hover {
    color: #E84422;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    border-color: #D1D9E6;
}

.btn-reddit.btn-link {
    color: #E84422;
    background: transparent;
    border: 0;
    border-style: none;
}

.btn-reddit.btn-link:hover, .btn-reddit.btn-link:focus, .btn-reddit.btn-link.active {
    background-color: none !important;
    border: 0;
    color: #E84422;
}

.btn-github {
    background-color: #e6e7ee;
    color: #222222;
    border-color: #D1D9E6;
}

.btn-github:hover {
    color: #222222;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
    border-color: #D1D9E6;
}

.btn-github.btn-link {
    color: #222222;
    background: transparent;
    border: 0;
    border-style: none;
}

.btn-github.btn-link:hover, .btn-github.btn-link:focus, .btn-github.btn-link.active {
    background-color: none !important;
    border: 0;
    color: #222222;
}

/**
 * = Breadcrumbs
 */
.breadcrumb-item, .breadcrumb-item a {
    color: #66799e;
    font-weight: 400;
    font-size: 0.75rem;
}

@media (min-width: 576px) {
    .breadcrumb-item, .breadcrumb-item a {
        font-size: 1rem;
    }
}

.breadcrumb-item.active {
    font-weight: 400;
}

.breadcrumb-item + .breadcrumb-item:before {
    content: "\f101";
    font-family: "Font Awesome 5 Free";
    font-weight: 900;
    font-size: .625rem;
    color: #66799e;
}

.breadcrumb-transparent {
    background: transparent;
    padding: 0;
}

.breadcrumb-primary {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-primary .breadcrumb-item a {
    color: #e6e7ee;
}

.breadcrumb-primary .breadcrumb-item::before {
    color: #e6e7ee;
}

.breadcrumb-primary .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-primary.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-primary.breadcrumb-transparent .breadcrumb-item.active {
    color: #e6e7ee;
}

.breadcrumb-secondary {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-secondary .breadcrumb-item a {
    color: #2D4CC8;
}

.breadcrumb-secondary .breadcrumb-item::before {
    color: #2D4CC8;
}

.breadcrumb-secondary .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-secondary.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-secondary.breadcrumb-transparent .breadcrumb-item.active {
    color: #2D4CC8;
}

.breadcrumb-success {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-success .breadcrumb-item a {
    color: #18634B;
}

.breadcrumb-success .breadcrumb-item::before {
    color: #18634B;
}

.breadcrumb-success .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-success.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-success.breadcrumb-transparent .breadcrumb-item.active {
    color: #18634B;
}

.breadcrumb-info {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-info .breadcrumb-item a {
    color: #0056B3;
}

.breadcrumb-info .breadcrumb-item::before {
    color: #0056B3;
}

.breadcrumb-info .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-info.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-info.breadcrumb-transparent .breadcrumb-item.active {
    color: #0056B3;
}

.breadcrumb-warning {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-warning .breadcrumb-item a {
    color: #F0B400;
}

.breadcrumb-warning .breadcrumb-item::before {
    color: #F0B400;
}

.breadcrumb-warning .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-warning.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-warning.breadcrumb-transparent .breadcrumb-item.active {
    color: #F0B400;
}

.breadcrumb-danger {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-danger .breadcrumb-item a {
    color: #A91E2C;
}

.breadcrumb-danger .breadcrumb-item::before {
    color: #A91E2C;
}

.breadcrumb-danger .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-danger.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-danger.breadcrumb-transparent .breadcrumb-item.active {
    color: #A91E2C;
}

.breadcrumb-light {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-light .breadcrumb-item a {
    color: #D1D9E6;
}

.breadcrumb-light .breadcrumb-item::before {
    color: #D1D9E6;
}

.breadcrumb-light .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-light.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-light.breadcrumb-transparent .breadcrumb-item.active {
    color: #D1D9E6;
}

.breadcrumb-dark {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-dark .breadcrumb-item a {
    color: #31344b;
}

.breadcrumb-dark .breadcrumb-item::before {
    color: #31344b;
}

.breadcrumb-dark .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-dark.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-dark.breadcrumb-transparent .breadcrumb-item.active {
    color: #31344b;
}

.breadcrumb-default {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-default .breadcrumb-item a {
    color: #262833;
}

.breadcrumb-default .breadcrumb-item::before {
    color: #262833;
}

.breadcrumb-default .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-default.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-default.breadcrumb-transparent .breadcrumb-item.active {
    color: #262833;
}

.breadcrumb-white {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-white .breadcrumb-item a {
    color: #ECF0F3;
}

.breadcrumb-white .breadcrumb-item::before {
    color: #ECF0F3;
}

.breadcrumb-white .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-white.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-white.breadcrumb-transparent .breadcrumb-item.active {
    color: #ECF0F3;
}

.breadcrumb-gray {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-gray .breadcrumb-item a {
    color: #44476A;
}

.breadcrumb-gray .breadcrumb-item::before {
    color: #44476A;
}

.breadcrumb-gray .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-gray.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-gray.breadcrumb-transparent .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-neutral {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-neutral .breadcrumb-item a {
    color: #ECF0F3;
}

.breadcrumb-neutral .breadcrumb-item::before {
    color: #ECF0F3;
}

.breadcrumb-neutral .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-neutral.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-neutral.breadcrumb-transparent .breadcrumb-item.active {
    color: #ECF0F3;
}

.breadcrumb-soft {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-soft .breadcrumb-item a {
    color: #e6e7ee;
}

.breadcrumb-soft .breadcrumb-item::before {
    color: #e6e7ee;
}

.breadcrumb-soft .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-soft.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-soft.breadcrumb-transparent .breadcrumb-item.active {
    color: #e6e7ee;
}

.breadcrumb-black {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-black .breadcrumb-item a {
    color: #262833;
}

.breadcrumb-black .breadcrumb-item::before {
    color: #262833;
}

.breadcrumb-black .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-black.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-black.breadcrumb-transparent .breadcrumb-item.active {
    color: #262833;
}

.breadcrumb-purple {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-purple .breadcrumb-item a {
    color: #6f42c1;
}

.breadcrumb-purple .breadcrumb-item::before {
    color: #6f42c1;
}

.breadcrumb-purple .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-purple.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-purple.breadcrumb-transparent .breadcrumb-item.active {
    color: #6f42c1;
}

.breadcrumb-gray-100 {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-gray-100 .breadcrumb-item a {
    color: #f3f7fa;
}

.breadcrumb-gray-100 .breadcrumb-item::before {
    color: #f3f7fa;
}

.breadcrumb-gray-100 .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-gray-100.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-gray-100.breadcrumb-transparent .breadcrumb-item.active {
    color: #f3f7fa;
}

.breadcrumb-gray-200 {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-gray-200 .breadcrumb-item a {
    color: #fafbfe;
}

.breadcrumb-gray-200 .breadcrumb-item::before {
    color: #fafbfe;
}

.breadcrumb-gray-200 .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-gray-200.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-gray-200.breadcrumb-transparent .breadcrumb-item.active {
    color: #fafbfe;
}

.breadcrumb-gray-300 {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-gray-300 .breadcrumb-item a {
    color: #e6e7ee;
}

.breadcrumb-gray-300 .breadcrumb-item::before {
    color: #e6e7ee;
}

.breadcrumb-gray-300 .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-gray-300.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-gray-300.breadcrumb-transparent .breadcrumb-item.active {
    color: #e6e7ee;
}

.breadcrumb-gray-400 {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-gray-400 .breadcrumb-item a {
    color: #D1D9E6;
}

.breadcrumb-gray-400 .breadcrumb-item::before {
    color: #D1D9E6;
}

.breadcrumb-gray-400 .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-gray-400.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-gray-400.breadcrumb-transparent .breadcrumb-item.active {
    color: #D1D9E6;
}

.breadcrumb-gray-500 {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-gray-500 .breadcrumb-item a {
    color: #b1bcce;
}

.breadcrumb-gray-500 .breadcrumb-item::before {
    color: #b1bcce;
}

.breadcrumb-gray-500 .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-gray-500.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-gray-500.breadcrumb-transparent .breadcrumb-item.active {
    color: #b1bcce;
}

.breadcrumb-gray-600 {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-gray-600 .breadcrumb-item a {
    color: #93a5be;
}

.breadcrumb-gray-600 .breadcrumb-item::before {
    color: #93a5be;
}

.breadcrumb-gray-600 .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-gray-600.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-gray-600.breadcrumb-transparent .breadcrumb-item.active {
    color: #93a5be;
}

.breadcrumb-gray-700 {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-gray-700 .breadcrumb-item a {
    color: #66799e;
}

.breadcrumb-gray-700 .breadcrumb-item::before {
    color: #66799e;
}

.breadcrumb-gray-700 .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-gray-700.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-gray-700.breadcrumb-transparent .breadcrumb-item.active {
    color: #66799e;
}

.breadcrumb-gray-800 {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-gray-800 .breadcrumb-item a {
    color: #525480;
}

.breadcrumb-gray-800 .breadcrumb-item::before {
    color: #525480;
}

.breadcrumb-gray-800 .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-gray-800.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-gray-800.breadcrumb-transparent .breadcrumb-item.active {
    color: #525480;
}

.breadcrumb-facebook {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-facebook .breadcrumb-item a {
    color: #3b5999;
}

.breadcrumb-facebook .breadcrumb-item::before {
    color: #3b5999;
}

.breadcrumb-facebook .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-facebook.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-facebook.breadcrumb-transparent .breadcrumb-item.active {
    color: #3b5999;
}

.breadcrumb-dribbble {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-dribbble .breadcrumb-item a {
    color: #ea4c89;
}

.breadcrumb-dribbble .breadcrumb-item::before {
    color: #ea4c89;
}

.breadcrumb-dribbble .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-dribbble.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-dribbble.breadcrumb-transparent .breadcrumb-item.active {
    color: #ea4c89;
}

.breadcrumb-github {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-github .breadcrumb-item a {
    color: #222222;
}

.breadcrumb-github .breadcrumb-item::before {
    color: #222222;
}

.breadcrumb-github .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-github.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-github.breadcrumb-transparent .breadcrumb-item.active {
    color: #222222;
}

.breadcrumb-behance {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-behance .breadcrumb-item a {
    color: #0057ff;
}

.breadcrumb-behance .breadcrumb-item::before {
    color: #0057ff;
}

.breadcrumb-behance .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-behance.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-behance.breadcrumb-transparent .breadcrumb-item.active {
    color: #0057ff;
}

.breadcrumb-twitter {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-twitter .breadcrumb-item a {
    color: #1da1f2;
}

.breadcrumb-twitter .breadcrumb-item::before {
    color: #1da1f2;
}

.breadcrumb-twitter .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-twitter.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-twitter.breadcrumb-transparent .breadcrumb-item.active {
    color: #1da1f2;
}

.breadcrumb-slack {
    background-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.breadcrumb-slack .breadcrumb-item a {
    color: #3aaf85;
}

.breadcrumb-slack .breadcrumb-item::before {
    color: #3aaf85;
}

.breadcrumb-slack .breadcrumb-item.active {
    color: #44476A;
}

.breadcrumb-slack.breadcrumb-transparent {
    background: transparent;
    box-shadow: none;
}

.breadcrumb-slack.breadcrumb-transparent .breadcrumb-item.active {
    color: #3aaf85;
}

.breadcrumb-text-light .breadcrumb-item, .breadcrumb-text-light .breadcrumb-item a {
    color: #ECF0F3;
}

.breadcrumb-text-light .breadcrumb-item:before {
    color: #ECF0F3;
}

/**
 * = Cards
 */
.card-img,
.card-img-top {
    border-radius: 0;
}

.card-img,
.card-img-bottom {
    border-radius: 0;
}

.card {
    position: relative;
}

.card .card-header {
    background: transparent;
}

.card .price-list .list-group-item span {
    width: 26px;
    font-size: 1rem;
}

.profile-page .card-profile {
    margin-top: -150px;
}

.profile-page .card-profile .card-profile-image {
    position: relative;
}

.profile-page .card-profile .card-profile-image img {
    max-width: 180px;
    border-radius: 0.55rem;
    transform: translate(-50%, -30%);
    position: absolute;
    left: 50%;
    transition: all 0.2s ease;
}

.profile-page .card-profile .card-profile-image img:hover {
    transform: translate(-50%, -33%);
}

.profile-page .card-profile .card-profile-stats {
    padding: 1rem 0;
}

.profile-page .card-profile .card-profile-stats > div {
    text-align: center;
    margin-right: 1rem;
    padding: .875rem;
}

.profile-page .card-profile .card-profile-stats > div:last-child {
    margin-right: 0;
}

.profile-page .card-profile .card-profile-stats > div .heading {
    display: block;
    font-size: 1.1rem;
    font-weight: bold;
}

.profile-page .card-profile .card-profile-stats > div .description {
    font-size: .875rem;
    color: #b1bcce;
}

.profile-page .card-profile .card-profile-actions {
    padding: .875rem;
}

@media (max-width: 575.98px) {
    .profile-page .card-profile .card-profile-actions {
        margin-top: 110px;
    }
}

@media (min-width: 576px) and (max-width: 991.98px) {
    .profile-page .card-profile .card-profile-stats {
        margin-top: 30px;
    }
}

.card-footer {
    background-color: transparent;
}

.card .card-blockquote {
    position: relative;
    padding: 2rem;
}

.card .card-blockquote .svg-bg {
    display: block;
    position: absolute;
    width: 100%;
    height: 95px;
    top: -94px;
    left: 0;
}

.page-preview {
    display: block;
    position: relative;
}

.page-preview .show-on-hover {
    position: absolute;
    bottom: -33px;
    background: #e6e7ee;
    color: #31344b;
    padding: 10px 0;
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;
    width: calc(100% + 36px);
    left: -18px;
    opacity: 0;
    transition: 0.2s;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@media (prefers-reduced-motion: reduce) {
    .page-preview .show-on-hover {
        transition: none;
    }
}

.page-preview:hover .show-on-hover {
    z-index: 99;
    opacity: 1;
}

.card-lift-hover:hover {
    transform: translateY(-20px);
    transition: all 0.2s ease;
}

@media (prefers-reduced-motion: reduce) {
    .card-lift-hover:hover {
        transition: none;
    }
}

/**
 * = Bootstrap carousels
 */
.carousel-caption, .carousel-caption h5 {
    color: #ECF0F3;
}

.carousel-indicators {
    bottom: 30px;
}

.carousel-indicators li {
    height: 10px;
    width: 10px;
    border-radius: 50%;
    background: transparent;
    border: 2px solid #31344b;
}

.carousel-indicators .active {
    opacity: 1;
    background: #31344b;
}

.carousel-control-prev-icon,
.carousel-control-next-icon {
    width: auto;
    height: auto;
    font-weight: 900;
    color: #31344b;
}

.carousel-control-prev-icon {
    background-image: none;
}

.carousel-control-prev-icon::before {
    content: '\f060';
    font-family: "Font Awesome 5 Free";
    font-size: 2rem;
}

.carousel-control-next-icon {
    background-image: none;
}

.carousel-control-next-icon:before {
    font-family: "Font Awesome 5 Free";
    content: "\f061";
    font-size: 2rem;
}

/**
 * = Close
 */
.close {
    transition: all 0.2s ease;
}

.close > span:not(.sr-only) {
    display: block;
    height: 1.25rem;
    width: 1.25rem;
    background-color: transparent;
    color: rgba(0, 0, 0, 0.6);
    line-height: 17px;
    border-radius: 50%;
    font-size: 1.25rem;
    transition: all 0.2s ease;
}

.close:hover, .close:focus {
    background-color: transparent;
    color: rgba(0, 0, 0, 0.9);
    outline: none;
}

.close:hover span:not(.sr-only), .close:focus span:not(.sr-only) {
    background-color: transparent;
}

/**
 * = Counters
 */
/**
 * = Custom forms
 */
.custom-control-label:before {
    border: 0.125rem solid #D1D9E6;
    box-shadow: none;
    transition: all 0.3s ease-in-out;
}

.custom-control-label span {
    position: relative;
    top: 2px;
}

.custom-control-label {
    margin-bottom: 0;
}

.custom-control-input:active ~ .custom-control-label::before {
    border-color: #e6e7ee;
}

.custom-file-label {
    border: 0.0625rem solid #D1D9E6;
    font-size: 1rem;
    color: #44476A;
    box-shadow: 6px 6px 12px #b8b9be, -6px -6px 12px #ffffff;
}

.custom-file-label::after {
    height: 100%;
    background-color: #31344b;
    color: #ECF0F3;
    border: 0;
}

.custom-file-input:not(:disabled):hover {
    cursor: pointer;
}

.custom-file-input:not(:disabled):hover ~ .custom-file-label,
  .custom-file-input:not(:disabled):hover ~ .custom-file-label:before {
    border-color: #e6e7ee;
}

.custom-select {
    font-size: 1rem;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    border: 0;
}

.custom-select.custom-select-shadow {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    border: 0;
    transition: box-shadow .15s ease;
}

.custom-select:hover {
    cursor: pointer;
}

.custom-switch {
    padding-left: 4.25rem;
}

.custom-switch .custom-control-label::before {
    left: -4.25rem;
    width: 2.5rem;
    pointer-events: all;
    border: 0;
    border-radius: 0.625rem;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.custom-switch .custom-control-label::after {
    top: calc(0.125rem + 2px);
    left: calc(-4.25rem + 2px);
    width: calc(1.25rem - 4px);
    height: calc(1.25rem - 4px);
    background-color: #b1bcce;
    border-radius: 0.625rem;
    transition: transform 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}

@media (prefers-reduced-motion: reduce) {
    .custom-switch .custom-control-label::after {
        transition: none;
    }
}

.custom-switch .custom-control-input:checked ~ .custom-control-label::before {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.custom-switch .custom-control-input:checked ~ .custom-control-label::after {
    background-color: #31344b;
    transform: translateX(1.25rem);
}

.custom-switch .custom-control-input:disabled:checked ~ .custom-control-label::before {
    background-color: rgba(230, 231, 238, 0.7);
}

.custom-switch .custom-control-input:disabled:checked ~ .custom-control-label::after {
    background-color: #31344b;
    opacity: .4;
}

/**
 * = Dropdowns
 */
.dropdown-menu {
    min-width: 12rem;
}

.dropdown-menu .dropdown-header,
  .dropdown-menu .dropdown-item {
    padding: .5rem 1rem;
    font-size: 0.875rem;
}

.dropdown-menu .dropdown-header {
    color: #44476A;
    font-weight: 600;
}

.dropdown-menu .dropdown-item {
    color: #44476A;
    transition: all 0.2s ease;
    font-weight: 300;
}

.dropdown-menu .dropdown-item:hover {
    color: #31344b;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: transparent;
}

.show .dropdown-menu {
    animation: show-dropdown .2s ease forwards;
}

[data-toggle]:hover {
    cursor: pointer;
}

.dropdown-toggle:after, .dropright .dropdown-toggle:after, .dropleft .dropdown-toggle:before, .dropup .dropdown-toggle:after {
    display: none;
}

.dropdown-menu-sm {
    min-width: 100px;
    border: 0.3rem;
}

.dropdown-menu-md {
    min-width: 180px;
    border: 0.3rem;
}

.dropdown-menu-lg {
    min-width: 260px;
    border-radius: 0.3rem;
}

.dropdown-menu-xl {
    min-width: 450px;
    border-radius: 0.3rem;
}

/**
 * = Forms
 */
label {
    font-size: 0.875rem;
}

.form-group {
    position: relative;
}

.form-control {
    font-size: 1rem;
    border-radius: 0.55rem;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.form-control:focus:placeholder {
    color: #44476A;
}

.form-control:disabled, .form-control[readonly] {
    background-color: #e6e7ee;
    opacity: .6;
}

/* Textareas */
textarea[resize="none"] {
    resize: none !important;
}

textarea[resize="both"] {
    resize: both !important;
}

textarea[resize="vertical"] {
    resize: vertical !important;
}

textarea[resize="horizontal"] {
    resize: horizontal !important;
}

/* shadow styles */
.form-control-muted {
    background-color: #f3f7fa;
    border-color: #f3f7fa;
    box-shadow: none;
}

.form-control-muted:focus {
    background-color: #f3f7fa;
}

.form-control-lg {
    font-size: 1rem;
}

.form-control-xl {
    height: calc(2.25em + 1.75rem + 0.0625rem);
    padding: 0.875rem 1rem;
    line-height: 1.5;
    font-size: 1.25rem;
    border-radius: 0.3rem;
}

.has-danger .form-control::placeholder {
    color: #A91E2C;
}

.has-success .form-control::placeholder {
    color: #18634B;
}

.form-check {
    padding-left: 0;
}

.form-check-input:disabled ~ .form-check-label {
    color: #525480;
}

.form-check .form-check-label {
    display: inline-block;
    position: relative;
    padding-left: 1.375rem;
    font-weight: 400;
    line-height: 16px;
    margin-bottom: 0;
    transition: all 0.2s ease;
    color: #44476A;
}

@media (prefers-reduced-motion: reduce) {
    .form-check .form-check-label {
        transition: none;
    }
}

.form-check .form-check-label:hover {
    cursor: pointer;
}

.radio .form-check-sign {
    padding-left: 28px;
}

.form-check input[type="radio"] + .form-check-inline .form-check-label {
    padding-left: 5px;
    margin-right: 10px;
}

.form-check .form-check-label::before,
.form-check .form-check-label::after {
    content: " ";
    display: inline-block;
    position: absolute;
    width: 15px;
    height: 15px;
    left: 0;
    top: 0;
    background-color: #D1D9E6;
    border: 1px solid #b1bcce;
    transition: all 0.2s ease;
    border-radius: 50%;
    box-shadow: inset 1px 2px 2px #b8b9be, inset -5px -2px 4px #FFFFFF;
}

@media (prefers-reduced-motion: reduce) {
    .form-check .form-check-label::before,
    .form-check .form-check-label::after {
        transition: none;
    }
}

.form-check .form-check-label::before:hover,
  .form-check .form-check-label::after:hover {
    cursor: pointer;
}

.form-check.square-check .form-check-label::before {
    border-radius: 2px;
}

.form-check.square-check .form-check-label::after {
    border-radius: 2px;
}

.form-check .form-check-sign-white:before {
    background-color: #ECF0F3;
}

.form-check input[type="checkbox"]:checked + .form-check-sign::before,
.form-check input[type="checkbox"]:checked + .form-check-sign::before {
    border: none;
}

.form-check .form-check-label::after {
    content: "\f00c";
    font-family: 'Font Awesome 5 Free';
    top: 0px;
    text-align: center;
    opacity: 0;
    color: #31344b;
    font-weight: 900;
    border: 0;
}

.form-check.disabled .form-check-label,
.form-check.disabled .form-check-label {
    color: #525480;
    cursor: not-allowed;
}

.form-check input[type="checkbox"],
.form-check input[type="radio"] {
    opacity: 0;
    position: absolute;
    visibility: hidden;
}

.form-check input[type="checkbox"]:checked + .form-check-label::after {
    background-color: #e6e7ee;
    opacity: 1;
    font-size: .6rem;
    margin-top: 0;
    line-height: 1.6;
}

.form-check input[type="checkbox"]:disabled + .form-check-label::after {
    color: rgba(49, 52, 75, 0.7);
}

.form-check input[type="checkbox"] + .form-check-label::after {
    opacity: 0;
}

.form-control input[type="checkbox"]:disabled + .form-check-label::before,
.checkbox input[type="checkbox"]:disabled + .form-check-label::after {
    cursor: not-allowed;
}

.form-check input[type="checkbox"]:disabled + .form-check-label,
.form-check input[type="radio"]:disabled + .form-check-label {
    pointer-events: none;
}

.form-check input[type="radio"] + .form-check-label {
    padding-top: 3px;
}

.form-check input[type="radio"] + .form-check-label::before,
.form-check input[type="radio"] + .form-check-label::after {
    content: " ";
    width: 18px;
    height: 18px;
    border-radius: 50%;
    display: inline-block;
    position: absolute;
    left: 0px;
    top: 3px;
    padding: 1px;
    transition: opacity 0.3s linear;
}

@media (prefers-reduced-motion: reduce) {
    .form-check input[type="radio"] + .form-check-label::before,
    .form-check input[type="radio"] + .form-check-label::after {
        transition: none;
    }
}

.form-check input[type="radio"] + .form-check-label::before,
.form-check input[type="radio"] + .form-check-label::after {
    content: " ";
    width: 18px;
    height: 18px;
    border-radius: 50%;
    display: inline-block;
    position: absolute;
    left: 0px;
    top: 3px;
    padding: 1px;
    transition: opacity 0.3s linear;
}

@media (prefers-reduced-motion: reduce) {
    .form-check input[type="radio"] + .form-check-label::before,
    .form-check input[type="radio"] + .form-check-label::after {
        transition: none;
    }
}

.form-check input[type="radio"] + .form-check-label:after,
.form-check input[type="radio"] {
    opacity: 0;
}

.form-check input[type="radio"]:checked + .form-check-label::after {
    width: 8px;
    height: 8px;
    top: 7px;
    left: 4px;
    background-color: #31344b;
    border: 4px solid #31344b;
    opacity: 1;
}

.form-check input[type="radio"]:checked + .form-check-label::before {
    background-color: #e6e7ee;
}

.form-check input[type="radio"]:disabled + .form-check-label::before {
    color: rgba(49, 52, 75, 0.7);
}

.form-check input[type="radio"]:disabled + .form-check-label::before,
.form-check input[type="radio"]:disabled + .form-check-label::after {
    color: #525480;
}

.round-check .form-check-sign::before,
.round-check .form-check-sign::after {
    border-radius: 50%;
}

/**
 * = Icon boxes
 */
.icon {
    text-align: center;
    display: inline-flex;
    -moz-align-items: center;
    -ms-align-items: center;
    align-items: center;
    -moz-justify-content: center;
    -ms-justify-content: center;
    justify-content: center;
    -ms-flex-pack: center;
}

.icon span, .icon svg {
    font-size: 2.25rem;
}

.icon.icon-shape {
    width: 5.5rem;
    height: 5.5rem;
}

.icon.icon-shape-xs {
    width: 2.5rem;
    height: 2.5rem;
}

.icon.icon-shape-xs span, .icon.icon-shape-xs svg {
    font-size: 1.25rem;
}

.icon.icon-shape-sm {
    width: 4.5rem;
    height: 4.5rem;
}

.icon.icon-shape-sm span, .icon.icon-shape-sm svg {
    font-size: 1.75rem;
}

.icon.icon-sm span, .icon.icon-sm svg {
    font-size: 1.75rem;
}

.icon.icon-md span, .icon.icon-md svg {
    font-size: 2.25rem;
}

.icon.icon-xs span, .icon.icon-xs svg {
    font-size: 1.25rem;
}

.github-big-icon {
    position: absolute;
    right: -255px;
    top: 75px;
}

.github-big-icon span {
    font-size: 800px;
    opacity: .1;
}

/**
 * = Images
 */
.image-lg {
    height: 12rem;
}

.image-md {
    height: 5rem;
}

.image-sm {
    height: 3rem;
}

.image-xs {
    height: 1.875rem;
}

.img-thumbnail {
    border-width: 0.125rem;
    box-shadow: none;
}

.full-image {
    height: 100%;
}

.gallery-feed img {
    width: 20%;
    margin-right: .5rem;
    margin-bottom: .5rem;
    float: left;
}

@media (min-width: 1200px) {
    .effect-img-2 {
        position: absolute;
        right: 5rem;
        top: 19%;
        z-index: 2;
        margin: 0;
    }

    .effect-img-1, .effect-img-2 {
        margin: 0 0 3rem;
        width: 350px;
        height: auto;
    }
}

@media (max-width: 1199.98px) {
    .effect-img-2 {
        right: .425rem;
        top: 0;
    }
}

/**
 * = Input groups
 */
.input-group {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    border-radius: 0.55rem;
    transition: all 0.2s ease;
}

.input-group .form-control:not(:first-child) {
    border-left: 0;
}

.input-group .form-control:not(:last-child) {
    border-right: 0;
    padding-right: 0;
}

.input-group-text {
    font-size: 0.875rem;
    transition: all 0.3s ease-in-out;
}

.focused .input-group-text {
    color: #44476A;
    background-color: #e6e7ee;
}

/**
 * = List groups
 */
.list-group-space .list-group-item {
    margin-bottom: 1.5rem;
    border-radius: 0.55rem;
}

.list-group-item.active {
    z-index: 2;
    color: #44476A;
    background-color: #e6e7ee;
    border-color: #e6e7ee;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.list-group-item i {
    width: 1rem;
}

.list-group-img {
    width: 3rem;
    height: 3rem;
    border-radius: 50%;
    vertical-align: top;
    margin: -.1rem 1.2rem 0 -.2rem;
}

.list-group-content {
    flex: 1;
    min-width: 0;
}

.list-group-content > p {
    color: #b1bcce;
    line-height: 1.5;
    margin: .2rem 0 0;
}

.list-group-heading {
    font-size: 1rem;
    color: #525480;
}

.list-group-heading > small {
    float: right;
    color: #b1bcce;
    font-weight: 500;
}

.list-group-flush .list-group-item {
    background-color: transparent;
}

.list-group.simple-list .list-group-item {
    background: transparent;
    border: none;
    padding: 0.375rem 0.125rem;
}

.list-group.simple-list .list-group-item span {
    vertical-align: middle;
    width: 35px;
    display: inline-block;
}

/**
 * = Maps
 */
.map {
    height: 500px;
    width: 100%;
    -moz-filter: grayscale(100%);
    -ms-filter: grayscale(100%);
    -o-filter: grayscale(100%);
    filter: grayscale(100%);
}

/**
 * = Modals
 */
.modal.static-example {
    position: relative;
    display: block;
}

.modal-content {
    border: 1px solid #D1D9E6;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    outline: 0;
}

.modal-header {
    border-bottom: 1px solid #D1D9E6;
}

.modal-header .close {
    padding: 1.25rem;
    margin: -1rem -1rem -1rem auto;
}

.modal-fluid .modal-dialog {
    margin-top: 0;
    margin-bottom: 0;
}

.modal-fluid .modal-content {
    border-radius: 0;
}

.modal-primary .modal-title {
    color: #31344b;
}

.modal-primary .modal-header,
.modal-primary .modal-footer {
    border-color: rgba(49, 52, 75, 0.075);
}

.modal-primary .modal-content {
    background-color: #e6e7ee;
    color: #31344b;
}

.modal-primary .modal-content .heading {
    color: #31344b;
}

.modal-primary .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-secondary .modal-title {
    color: #ECF0F3;
}

.modal-secondary .modal-header,
.modal-secondary .modal-footer {
    border-color: rgba(236, 240, 243, 0.075);
}

.modal-secondary .modal-content {
    background-color: #2D4CC8;
    color: #ECF0F3;
}

.modal-secondary .modal-content .heading {
    color: #ECF0F3;
}

.modal-secondary .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-success .modal-title {
    color: #ECF0F3;
}

.modal-success .modal-header,
.modal-success .modal-footer {
    border-color: rgba(236, 240, 243, 0.075);
}

.modal-success .modal-content {
    background-color: #18634B;
    color: #ECF0F3;
}

.modal-success .modal-content .heading {
    color: #ECF0F3;
}

.modal-success .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-info .modal-title {
    color: #ECF0F3;
}

.modal-info .modal-header,
.modal-info .modal-footer {
    border-color: rgba(236, 240, 243, 0.075);
}

.modal-info .modal-content {
    background-color: #0056B3;
    color: #ECF0F3;
}

.modal-info .modal-content .heading {
    color: #ECF0F3;
}

.modal-info .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-warning .modal-title {
    color: #ECF0F3;
}

.modal-warning .modal-header,
.modal-warning .modal-footer {
    border-color: rgba(236, 240, 243, 0.075);
}

.modal-warning .modal-content {
    background-color: #F0B400;
    color: #ECF0F3;
}

.modal-warning .modal-content .heading {
    color: #ECF0F3;
}

.modal-warning .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-danger .modal-title {
    color: #ECF0F3;
}

.modal-danger .modal-header,
.modal-danger .modal-footer {
    border-color: rgba(236, 240, 243, 0.075);
}

.modal-danger .modal-content {
    background-color: #A91E2C;
    color: #ECF0F3;
}

.modal-danger .modal-content .heading {
    color: #ECF0F3;
}

.modal-danger .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-light .modal-title {
    color: #31344b;
}

.modal-light .modal-header,
.modal-light .modal-footer {
    border-color: rgba(49, 52, 75, 0.075);
}

.modal-light .modal-content {
    background-color: #D1D9E6;
    color: #31344b;
}

.modal-light .modal-content .heading {
    color: #31344b;
}

.modal-light .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-dark .modal-title {
    color: #ECF0F3;
}

.modal-dark .modal-header,
.modal-dark .modal-footer {
    border-color: rgba(236, 240, 243, 0.075);
}

.modal-dark .modal-content {
    background-color: #31344b;
    color: #ECF0F3;
}

.modal-dark .modal-content .heading {
    color: #ECF0F3;
}

.modal-dark .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-default .modal-title {
    color: #ECF0F3;
}

.modal-default .modal-header,
.modal-default .modal-footer {
    border-color: rgba(236, 240, 243, 0.075);
}

.modal-default .modal-content {
    background-color: #262833;
    color: #ECF0F3;
}

.modal-default .modal-content .heading {
    color: #ECF0F3;
}

.modal-default .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-white .modal-title {
    color: #31344b;
}

.modal-white .modal-header,
.modal-white .modal-footer {
    border-color: rgba(49, 52, 75, 0.075);
}

.modal-white .modal-content {
    background-color: #ECF0F3;
    color: #31344b;
}

.modal-white .modal-content .heading {
    color: #31344b;
}

.modal-white .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-gray .modal-title {
    color: #ECF0F3;
}

.modal-gray .modal-header,
.modal-gray .modal-footer {
    border-color: rgba(236, 240, 243, 0.075);
}

.modal-gray .modal-content {
    background-color: #44476A;
    color: #ECF0F3;
}

.modal-gray .modal-content .heading {
    color: #ECF0F3;
}

.modal-gray .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-neutral .modal-title {
    color: #31344b;
}

.modal-neutral .modal-header,
.modal-neutral .modal-footer {
    border-color: rgba(49, 52, 75, 0.075);
}

.modal-neutral .modal-content {
    background-color: #ECF0F3;
    color: #31344b;
}

.modal-neutral .modal-content .heading {
    color: #31344b;
}

.modal-neutral .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-soft .modal-title {
    color: #31344b;
}

.modal-soft .modal-header,
.modal-soft .modal-footer {
    border-color: rgba(49, 52, 75, 0.075);
}

.modal-soft .modal-content {
    background-color: #e6e7ee;
    color: #31344b;
}

.modal-soft .modal-content .heading {
    color: #31344b;
}

.modal-soft .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-black .modal-title {
    color: #ECF0F3;
}

.modal-black .modal-header,
.modal-black .modal-footer {
    border-color: rgba(236, 240, 243, 0.075);
}

.modal-black .modal-content {
    background-color: #262833;
    color: #ECF0F3;
}

.modal-black .modal-content .heading {
    color: #ECF0F3;
}

.modal-black .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-purple .modal-title {
    color: #ECF0F3;
}

.modal-purple .modal-header,
.modal-purple .modal-footer {
    border-color: rgba(236, 240, 243, 0.075);
}

.modal-purple .modal-content {
    background-color: #6f42c1;
    color: #ECF0F3;
}

.modal-purple .modal-content .heading {
    color: #ECF0F3;
}

.modal-purple .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-gray-100 .modal-title {
    color: #31344b;
}

.modal-gray-100 .modal-header,
.modal-gray-100 .modal-footer {
    border-color: rgba(49, 52, 75, 0.075);
}

.modal-gray-100 .modal-content {
    background-color: #f3f7fa;
    color: #31344b;
}

.modal-gray-100 .modal-content .heading {
    color: #31344b;
}

.modal-gray-100 .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-gray-200 .modal-title {
    color: #31344b;
}

.modal-gray-200 .modal-header,
.modal-gray-200 .modal-footer {
    border-color: rgba(49, 52, 75, 0.075);
}

.modal-gray-200 .modal-content {
    background-color: #fafbfe;
    color: #31344b;
}

.modal-gray-200 .modal-content .heading {
    color: #31344b;
}

.modal-gray-200 .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-gray-300 .modal-title {
    color: #31344b;
}

.modal-gray-300 .modal-header,
.modal-gray-300 .modal-footer {
    border-color: rgba(49, 52, 75, 0.075);
}

.modal-gray-300 .modal-content {
    background-color: #e6e7ee;
    color: #31344b;
}

.modal-gray-300 .modal-content .heading {
    color: #31344b;
}

.modal-gray-300 .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-gray-400 .modal-title {
    color: #31344b;
}

.modal-gray-400 .modal-header,
.modal-gray-400 .modal-footer {
    border-color: rgba(49, 52, 75, 0.075);
}

.modal-gray-400 .modal-content {
    background-color: #D1D9E6;
    color: #31344b;
}

.modal-gray-400 .modal-content .heading {
    color: #31344b;
}

.modal-gray-400 .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-gray-500 .modal-title {
    color: #ECF0F3;
}

.modal-gray-500 .modal-header,
.modal-gray-500 .modal-footer {
    border-color: rgba(236, 240, 243, 0.075);
}

.modal-gray-500 .modal-content {
    background-color: #b1bcce;
    color: #ECF0F3;
}

.modal-gray-500 .modal-content .heading {
    color: #ECF0F3;
}

.modal-gray-500 .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-gray-600 .modal-title {
    color: #ECF0F3;
}

.modal-gray-600 .modal-header,
.modal-gray-600 .modal-footer {
    border-color: rgba(236, 240, 243, 0.075);
}

.modal-gray-600 .modal-content {
    background-color: #93a5be;
    color: #ECF0F3;
}

.modal-gray-600 .modal-content .heading {
    color: #ECF0F3;
}

.modal-gray-600 .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-gray-700 .modal-title {
    color: #ECF0F3;
}

.modal-gray-700 .modal-header,
.modal-gray-700 .modal-footer {
    border-color: rgba(236, 240, 243, 0.075);
}

.modal-gray-700 .modal-content {
    background-color: #66799e;
    color: #ECF0F3;
}

.modal-gray-700 .modal-content .heading {
    color: #ECF0F3;
}

.modal-gray-700 .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-gray-800 .modal-title {
    color: #ECF0F3;
}

.modal-gray-800 .modal-header,
.modal-gray-800 .modal-footer {
    border-color: rgba(236, 240, 243, 0.075);
}

.modal-gray-800 .modal-content {
    background-color: #525480;
    color: #ECF0F3;
}

.modal-gray-800 .modal-content .heading {
    color: #ECF0F3;
}

.modal-gray-800 .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-facebook .modal-title {
    color: #ECF0F3;
}

.modal-facebook .modal-header,
.modal-facebook .modal-footer {
    border-color: rgba(236, 240, 243, 0.075);
}

.modal-facebook .modal-content {
    background-color: #3b5999;
    color: #ECF0F3;
}

.modal-facebook .modal-content .heading {
    color: #ECF0F3;
}

.modal-facebook .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-dribbble .modal-title {
    color: #ECF0F3;
}

.modal-dribbble .modal-header,
.modal-dribbble .modal-footer {
    border-color: rgba(236, 240, 243, 0.075);
}

.modal-dribbble .modal-content {
    background-color: #ea4c89;
    color: #ECF0F3;
}

.modal-dribbble .modal-content .heading {
    color: #ECF0F3;
}

.modal-dribbble .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-github .modal-title {
    color: #ECF0F3;
}

.modal-github .modal-header,
.modal-github .modal-footer {
    border-color: rgba(236, 240, 243, 0.075);
}

.modal-github .modal-content {
    background-color: #222222;
    color: #ECF0F3;
}

.modal-github .modal-content .heading {
    color: #ECF0F3;
}

.modal-github .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-behance .modal-title {
    color: #ECF0F3;
}

.modal-behance .modal-header,
.modal-behance .modal-footer {
    border-color: rgba(236, 240, 243, 0.075);
}

.modal-behance .modal-content {
    background-color: #0057ff;
    color: #ECF0F3;
}

.modal-behance .modal-content .heading {
    color: #ECF0F3;
}

.modal-behance .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-twitter .modal-title {
    color: #ECF0F3;
}

.modal-twitter .modal-header,
.modal-twitter .modal-footer {
    border-color: rgba(236, 240, 243, 0.075);
}

.modal-twitter .modal-content {
    background-color: #1da1f2;
    color: #ECF0F3;
}

.modal-twitter .modal-content .heading {
    color: #ECF0F3;
}

.modal-twitter .close > span:not(.sr-only) {
    color: #ECF0F3;
}

.modal-slack .modal-title {
    color: #ECF0F3;
}

.modal-slack .modal-header,
.modal-slack .modal-footer {
    border-color: rgba(236, 240, 243, 0.075);
}

.modal-slack .modal-content {
    background-color: #3aaf85;
    color: #ECF0F3;
}

.modal-slack .modal-content .heading {
    color: #ECF0F3;
}

.modal-slack .close > span:not(.sr-only) {
    color: #ECF0F3;
}

/**
 * = Navs
 */
.nav-link {
    color: #44476A;
}

.nav-link:hover, .nav-link.active {
    color: #31344b;
}

.nav-link:hover img, .nav-link.active img {
    opacity: inherit;
    transition: all 0.2s ease;
}

.nav-link i {
    position: relative;
    margin-right: .5rem;
}

.nav-link img {
    opacity: .5;
}

.nav-tabs .nav-item {
    margin-bottom: 0;
}

.nav-tabs .nav-link {
    border: 0;
    padding: 1rem 1rem;
}

.nav-pills .nav-item:not(:last-child) {
    padding-right: 2rem;
}

.nav-pills .nav-link {
    padding: 0.75rem 0.85rem;
    transition: all 0.2s ease;
    box-shadow: 6px 6px 12px #b8b9be, -6px -6px 12px #ffffff;
    border: 1px solid #D1D9E6;
}

.nav-pills .nav-link.avatar-link {
    border: 0;
}

.nav-pills .nav-link:hover {
    color: #31344b;
}

.nav-pills .nav-link.active,
.nav-pills .show > .nav-link {
    color: #31344b;
    background-color: #e6e7ee;
    border-color: #D1D9E6;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.nav-pills.rounded .nav-link {
    border-radius: 30px;
}

.nav-pills.rounded.vertical-tab .nav-link {
    margin-bottom: .625rem;
    min-width: 100px;
}

.nav-pills.rounded.vertical-tab .nav-item:not(:last-child) {
    padding-right: 0;
}

.nav-pills.bordered-pill-md .nav-link {
    border: 0.125rem solid #fafbfe;
    font-weight: 600;
}

.nav-pills.vertical-tab .nav-link {
    margin-bottom: .625rem;
}

.nav-pills.vertical-tab .nav-item:not(:last-child) {
    padding-right: 0;
}

@media (max-width: 575.98px) {
    .nav-pills .nav-item {
        margin-bottom: 1rem;
    }
}

@media (max-width: 767.98px) {
    .nav-pills:not(.nav-pills-circle) .nav-item {
        padding-right: 0;
    }
}

.nav-pill-circle .nav-link {
    display: flex;
    text-align: center;
    height: 80px;
    width: 80px;
    padding: 0;
    box-shadow: 6px 6px 12px #b8b9be, -6px -6px 12px #ffffff;
    border-radius: 50%;
    align-items: center;
    justify-content: center;
}

.nav-pill-circle .nav-link.avatar-link {
    box-shadow: none;
}

.nav-pill-circle.vertical-tab .nav-link-icon i, .nav-pill-circle.vertical-tab .nav-link-icon svg {
    font-size: 1.5rem;
}

.nav-pill-circle.vertical-tab .nav-item:not(:last-child) {
    padding-right: 0;
}

.nav-pill-circle .nav-link-icon i, .nav-pill-circle .nav-link-icon svg {
    font-size: 1.25rem;
    margin: 0;
    display: block;
}

.nav-pill-square .nav-link {
    text-align: center;
    min-width: 80px;
    box-shadow: 6px 6px 12px #b8b9be, -6px -6px 12px #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
}

.nav-pill-square.vertical-tab .nav-link {
    margin-bottom: .625rem;
    min-width: 100px;
}

.nav-pill-square.vertical-tab .nav-item:not(:last-child) {
    padding-right: 0;
}

.nav-pill-square .nav-link-icon i, .nav-pill-square .nav-link-icon svg {
    font-size: 1.25rem;
    margin: 0;
    display: block;
    line-height: 50px;
}

.nav-wrapper {
    padding: 1rem 0;
    border-top-left-radius: 0.55rem;
    border-top-right-radius: 0.55rem;
}

.nav-wrapper + .card {
    border-top-left-radius: 0;
    border-top-right-radius: 0;
    border-bottom-right-radius: 0.55rem;
    border-bottom-left-radius: 0.55rem;
}

.tab-content > .tab-pane {
    display: none;
}

.tab-content > .tab-pane pre {
    padding: 0;
    margin: 0;
}

.tab-content > .active {
    display: block;
}

/**
 * = Paginations
 */
.page-link {
    border: 0;
    background-color: #e6e7ee;
    box-shadow: 3px 3px 6px #b8b9be, -3px -3px 6px #ffffff;
}

.page-link:hover {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    background-color: #e6e7ee;
}

.circle-pagination .page-link,
.circle-pagination span {
    display: flex;
    border-radius: 50% !important;
    align-items: center;
    justify-content: center;
    width: 34px;
    height: 34px;
    padding: 0;
}

.page-item.active .page-link {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
    color: #525480;
}

.page-item .page-link,
.page-item span {
    margin: 0 4px;
    font-size: 0.875rem;
    color: #31344b;
    font-weight: 600;
}

.pagination-lg .page-item .page-link,
.pagination-lg .page-item span {
    width: 46px;
    height: 46px;
    line-height: 46px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.pagination-sm .page-item .page-link,
.pagination-sm .page-item span {
    display: flex;
    width: 30px;
    height: 30px;
    line-height: 30px;
    align-items: center;
    justify-content: center;
}

/**
 * = Popovers
 */
.popover-header {
    font-weight: 600;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.popover-primary {
    background-color: #e6e7ee;
}

.popover-primary .popover-header {
    background-color: #e6e7ee;
    color: #31344b;
}

.popover-primary .popover-body {
    color: #31344b;
}

.popover-primary .popover-header {
    border-color: rgba(49, 52, 75, 0.2);
}

.popover-primary.bs-popover-top .arrow::after, .popover-primary.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #e6e7ee;
}

.popover-primary.bs-popover-right .arrow::after, .popover-primary.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #e6e7ee;
}

.popover-primary.bs-popover-bottom .arrow::after, .popover-primary.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #e6e7ee;
}

.popover-primary.bs-popover-left .arrow::after, .popover-primary.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #e6e7ee;
}

.popover-secondary {
    background-color: #2D4CC8;
}

.popover-secondary .popover-header {
    background-color: #2D4CC8;
    color: #ECF0F3;
}

.popover-secondary .popover-body {
    color: #ECF0F3;
}

.popover-secondary .popover-header {
    border-color: rgba(236, 240, 243, 0.2);
}

.popover-secondary.bs-popover-top .arrow::after, .popover-secondary.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #2D4CC8;
}

.popover-secondary.bs-popover-right .arrow::after, .popover-secondary.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #2D4CC8;
}

.popover-secondary.bs-popover-bottom .arrow::after, .popover-secondary.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #2D4CC8;
}

.popover-secondary.bs-popover-left .arrow::after, .popover-secondary.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #2D4CC8;
}

.popover-success {
    background-color: #18634B;
}

.popover-success .popover-header {
    background-color: #18634B;
    color: #ECF0F3;
}

.popover-success .popover-body {
    color: #ECF0F3;
}

.popover-success .popover-header {
    border-color: rgba(236, 240, 243, 0.2);
}

.popover-success.bs-popover-top .arrow::after, .popover-success.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #18634B;
}

.popover-success.bs-popover-right .arrow::after, .popover-success.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #18634B;
}

.popover-success.bs-popover-bottom .arrow::after, .popover-success.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #18634B;
}

.popover-success.bs-popover-left .arrow::after, .popover-success.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #18634B;
}

.popover-info {
    background-color: #0056B3;
}

.popover-info .popover-header {
    background-color: #0056B3;
    color: #ECF0F3;
}

.popover-info .popover-body {
    color: #ECF0F3;
}

.popover-info .popover-header {
    border-color: rgba(236, 240, 243, 0.2);
}

.popover-info.bs-popover-top .arrow::after, .popover-info.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #0056B3;
}

.popover-info.bs-popover-right .arrow::after, .popover-info.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #0056B3;
}

.popover-info.bs-popover-bottom .arrow::after, .popover-info.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #0056B3;
}

.popover-info.bs-popover-left .arrow::after, .popover-info.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #0056B3;
}

.popover-warning {
    background-color: #F0B400;
}

.popover-warning .popover-header {
    background-color: #F0B400;
    color: #ECF0F3;
}

.popover-warning .popover-body {
    color: #ECF0F3;
}

.popover-warning .popover-header {
    border-color: rgba(236, 240, 243, 0.2);
}

.popover-warning.bs-popover-top .arrow::after, .popover-warning.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #F0B400;
}

.popover-warning.bs-popover-right .arrow::after, .popover-warning.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #F0B400;
}

.popover-warning.bs-popover-bottom .arrow::after, .popover-warning.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #F0B400;
}

.popover-warning.bs-popover-left .arrow::after, .popover-warning.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #F0B400;
}

.popover-danger {
    background-color: #A91E2C;
}

.popover-danger .popover-header {
    background-color: #A91E2C;
    color: #ECF0F3;
}

.popover-danger .popover-body {
    color: #ECF0F3;
}

.popover-danger .popover-header {
    border-color: rgba(236, 240, 243, 0.2);
}

.popover-danger.bs-popover-top .arrow::after, .popover-danger.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #A91E2C;
}

.popover-danger.bs-popover-right .arrow::after, .popover-danger.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #A91E2C;
}

.popover-danger.bs-popover-bottom .arrow::after, .popover-danger.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #A91E2C;
}

.popover-danger.bs-popover-left .arrow::after, .popover-danger.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #A91E2C;
}

.popover-light {
    background-color: #D1D9E6;
}

.popover-light .popover-header {
    background-color: #D1D9E6;
    color: #31344b;
}

.popover-light .popover-body {
    color: #31344b;
}

.popover-light .popover-header {
    border-color: rgba(49, 52, 75, 0.2);
}

.popover-light.bs-popover-top .arrow::after, .popover-light.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #D1D9E6;
}

.popover-light.bs-popover-right .arrow::after, .popover-light.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #D1D9E6;
}

.popover-light.bs-popover-bottom .arrow::after, .popover-light.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #D1D9E6;
}

.popover-light.bs-popover-left .arrow::after, .popover-light.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #D1D9E6;
}

.popover-dark {
    background-color: #31344b;
}

.popover-dark .popover-header {
    background-color: #31344b;
    color: #ECF0F3;
}

.popover-dark .popover-body {
    color: #ECF0F3;
}

.popover-dark .popover-header {
    border-color: rgba(236, 240, 243, 0.2);
}

.popover-dark.bs-popover-top .arrow::after, .popover-dark.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #31344b;
}

.popover-dark.bs-popover-right .arrow::after, .popover-dark.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #31344b;
}

.popover-dark.bs-popover-bottom .arrow::after, .popover-dark.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #31344b;
}

.popover-dark.bs-popover-left .arrow::after, .popover-dark.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #31344b;
}

.popover-default {
    background-color: #262833;
}

.popover-default .popover-header {
    background-color: #262833;
    color: #ECF0F3;
}

.popover-default .popover-body {
    color: #ECF0F3;
}

.popover-default .popover-header {
    border-color: rgba(236, 240, 243, 0.2);
}

.popover-default.bs-popover-top .arrow::after, .popover-default.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #262833;
}

.popover-default.bs-popover-right .arrow::after, .popover-default.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #262833;
}

.popover-default.bs-popover-bottom .arrow::after, .popover-default.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #262833;
}

.popover-default.bs-popover-left .arrow::after, .popover-default.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #262833;
}

.popover-white {
    background-color: #ECF0F3;
}

.popover-white .popover-header {
    background-color: #ECF0F3;
    color: #31344b;
}

.popover-white .popover-body {
    color: #31344b;
}

.popover-white .popover-header {
    border-color: rgba(49, 52, 75, 0.2);
}

.popover-white.bs-popover-top .arrow::after, .popover-white.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #ECF0F3;
}

.popover-white.bs-popover-right .arrow::after, .popover-white.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #ECF0F3;
}

.popover-white.bs-popover-bottom .arrow::after, .popover-white.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #ECF0F3;
}

.popover-white.bs-popover-left .arrow::after, .popover-white.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #ECF0F3;
}

.popover-gray {
    background-color: #44476A;
}

.popover-gray .popover-header {
    background-color: #44476A;
    color: #ECF0F3;
}

.popover-gray .popover-body {
    color: #ECF0F3;
}

.popover-gray .popover-header {
    border-color: rgba(236, 240, 243, 0.2);
}

.popover-gray.bs-popover-top .arrow::after, .popover-gray.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #44476A;
}

.popover-gray.bs-popover-right .arrow::after, .popover-gray.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #44476A;
}

.popover-gray.bs-popover-bottom .arrow::after, .popover-gray.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #44476A;
}

.popover-gray.bs-popover-left .arrow::after, .popover-gray.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #44476A;
}

.popover-neutral {
    background-color: #ECF0F3;
}

.popover-neutral .popover-header {
    background-color: #ECF0F3;
    color: #31344b;
}

.popover-neutral .popover-body {
    color: #31344b;
}

.popover-neutral .popover-header {
    border-color: rgba(49, 52, 75, 0.2);
}

.popover-neutral.bs-popover-top .arrow::after, .popover-neutral.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #ECF0F3;
}

.popover-neutral.bs-popover-right .arrow::after, .popover-neutral.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #ECF0F3;
}

.popover-neutral.bs-popover-bottom .arrow::after, .popover-neutral.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #ECF0F3;
}

.popover-neutral.bs-popover-left .arrow::after, .popover-neutral.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #ECF0F3;
}

.popover-soft {
    background-color: #e6e7ee;
}

.popover-soft .popover-header {
    background-color: #e6e7ee;
    color: #31344b;
}

.popover-soft .popover-body {
    color: #31344b;
}

.popover-soft .popover-header {
    border-color: rgba(49, 52, 75, 0.2);
}

.popover-soft.bs-popover-top .arrow::after, .popover-soft.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #e6e7ee;
}

.popover-soft.bs-popover-right .arrow::after, .popover-soft.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #e6e7ee;
}

.popover-soft.bs-popover-bottom .arrow::after, .popover-soft.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #e6e7ee;
}

.popover-soft.bs-popover-left .arrow::after, .popover-soft.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #e6e7ee;
}

.popover-black {
    background-color: #262833;
}

.popover-black .popover-header {
    background-color: #262833;
    color: #ECF0F3;
}

.popover-black .popover-body {
    color: #ECF0F3;
}

.popover-black .popover-header {
    border-color: rgba(236, 240, 243, 0.2);
}

.popover-black.bs-popover-top .arrow::after, .popover-black.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #262833;
}

.popover-black.bs-popover-right .arrow::after, .popover-black.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #262833;
}

.popover-black.bs-popover-bottom .arrow::after, .popover-black.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #262833;
}

.popover-black.bs-popover-left .arrow::after, .popover-black.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #262833;
}

.popover-purple {
    background-color: #6f42c1;
}

.popover-purple .popover-header {
    background-color: #6f42c1;
    color: #ECF0F3;
}

.popover-purple .popover-body {
    color: #ECF0F3;
}

.popover-purple .popover-header {
    border-color: rgba(236, 240, 243, 0.2);
}

.popover-purple.bs-popover-top .arrow::after, .popover-purple.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #6f42c1;
}

.popover-purple.bs-popover-right .arrow::after, .popover-purple.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #6f42c1;
}

.popover-purple.bs-popover-bottom .arrow::after, .popover-purple.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #6f42c1;
}

.popover-purple.bs-popover-left .arrow::after, .popover-purple.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #6f42c1;
}

.popover-gray-100 {
    background-color: #f3f7fa;
}

.popover-gray-100 .popover-header {
    background-color: #f3f7fa;
    color: #31344b;
}

.popover-gray-100 .popover-body {
    color: #31344b;
}

.popover-gray-100 .popover-header {
    border-color: rgba(49, 52, 75, 0.2);
}

.popover-gray-100.bs-popover-top .arrow::after, .popover-gray-100.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #f3f7fa;
}

.popover-gray-100.bs-popover-right .arrow::after, .popover-gray-100.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #f3f7fa;
}

.popover-gray-100.bs-popover-bottom .arrow::after, .popover-gray-100.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #f3f7fa;
}

.popover-gray-100.bs-popover-left .arrow::after, .popover-gray-100.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #f3f7fa;
}

.popover-gray-200 {
    background-color: #fafbfe;
}

.popover-gray-200 .popover-header {
    background-color: #fafbfe;
    color: #31344b;
}

.popover-gray-200 .popover-body {
    color: #31344b;
}

.popover-gray-200 .popover-header {
    border-color: rgba(49, 52, 75, 0.2);
}

.popover-gray-200.bs-popover-top .arrow::after, .popover-gray-200.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #fafbfe;
}

.popover-gray-200.bs-popover-right .arrow::after, .popover-gray-200.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #fafbfe;
}

.popover-gray-200.bs-popover-bottom .arrow::after, .popover-gray-200.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #fafbfe;
}

.popover-gray-200.bs-popover-left .arrow::after, .popover-gray-200.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #fafbfe;
}

.popover-gray-300 {
    background-color: #e6e7ee;
}

.popover-gray-300 .popover-header {
    background-color: #e6e7ee;
    color: #31344b;
}

.popover-gray-300 .popover-body {
    color: #31344b;
}

.popover-gray-300 .popover-header {
    border-color: rgba(49, 52, 75, 0.2);
}

.popover-gray-300.bs-popover-top .arrow::after, .popover-gray-300.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #e6e7ee;
}

.popover-gray-300.bs-popover-right .arrow::after, .popover-gray-300.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #e6e7ee;
}

.popover-gray-300.bs-popover-bottom .arrow::after, .popover-gray-300.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #e6e7ee;
}

.popover-gray-300.bs-popover-left .arrow::after, .popover-gray-300.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #e6e7ee;
}

.popover-gray-400 {
    background-color: #D1D9E6;
}

.popover-gray-400 .popover-header {
    background-color: #D1D9E6;
    color: #31344b;
}

.popover-gray-400 .popover-body {
    color: #31344b;
}

.popover-gray-400 .popover-header {
    border-color: rgba(49, 52, 75, 0.2);
}

.popover-gray-400.bs-popover-top .arrow::after, .popover-gray-400.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #D1D9E6;
}

.popover-gray-400.bs-popover-right .arrow::after, .popover-gray-400.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #D1D9E6;
}

.popover-gray-400.bs-popover-bottom .arrow::after, .popover-gray-400.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #D1D9E6;
}

.popover-gray-400.bs-popover-left .arrow::after, .popover-gray-400.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #D1D9E6;
}

.popover-gray-500 {
    background-color: #b1bcce;
}

.popover-gray-500 .popover-header {
    background-color: #b1bcce;
    color: #ECF0F3;
}

.popover-gray-500 .popover-body {
    color: #ECF0F3;
}

.popover-gray-500 .popover-header {
    border-color: rgba(236, 240, 243, 0.2);
}

.popover-gray-500.bs-popover-top .arrow::after, .popover-gray-500.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #b1bcce;
}

.popover-gray-500.bs-popover-right .arrow::after, .popover-gray-500.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #b1bcce;
}

.popover-gray-500.bs-popover-bottom .arrow::after, .popover-gray-500.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #b1bcce;
}

.popover-gray-500.bs-popover-left .arrow::after, .popover-gray-500.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #b1bcce;
}

.popover-gray-600 {
    background-color: #93a5be;
}

.popover-gray-600 .popover-header {
    background-color: #93a5be;
    color: #ECF0F3;
}

.popover-gray-600 .popover-body {
    color: #ECF0F3;
}

.popover-gray-600 .popover-header {
    border-color: rgba(236, 240, 243, 0.2);
}

.popover-gray-600.bs-popover-top .arrow::after, .popover-gray-600.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #93a5be;
}

.popover-gray-600.bs-popover-right .arrow::after, .popover-gray-600.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #93a5be;
}

.popover-gray-600.bs-popover-bottom .arrow::after, .popover-gray-600.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #93a5be;
}

.popover-gray-600.bs-popover-left .arrow::after, .popover-gray-600.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #93a5be;
}

.popover-gray-700 {
    background-color: #66799e;
}

.popover-gray-700 .popover-header {
    background-color: #66799e;
    color: #ECF0F3;
}

.popover-gray-700 .popover-body {
    color: #ECF0F3;
}

.popover-gray-700 .popover-header {
    border-color: rgba(236, 240, 243, 0.2);
}

.popover-gray-700.bs-popover-top .arrow::after, .popover-gray-700.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #66799e;
}

.popover-gray-700.bs-popover-right .arrow::after, .popover-gray-700.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #66799e;
}

.popover-gray-700.bs-popover-bottom .arrow::after, .popover-gray-700.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #66799e;
}

.popover-gray-700.bs-popover-left .arrow::after, .popover-gray-700.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #66799e;
}

.popover-gray-800 {
    background-color: #525480;
}

.popover-gray-800 .popover-header {
    background-color: #525480;
    color: #ECF0F3;
}

.popover-gray-800 .popover-body {
    color: #ECF0F3;
}

.popover-gray-800 .popover-header {
    border-color: rgba(236, 240, 243, 0.2);
}

.popover-gray-800.bs-popover-top .arrow::after, .popover-gray-800.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #525480;
}

.popover-gray-800.bs-popover-right .arrow::after, .popover-gray-800.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #525480;
}

.popover-gray-800.bs-popover-bottom .arrow::after, .popover-gray-800.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #525480;
}

.popover-gray-800.bs-popover-left .arrow::after, .popover-gray-800.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #525480;
}

.popover-facebook {
    background-color: #3b5999;
}

.popover-facebook .popover-header {
    background-color: #3b5999;
    color: #ECF0F3;
}

.popover-facebook .popover-body {
    color: #ECF0F3;
}

.popover-facebook .popover-header {
    border-color: rgba(236, 240, 243, 0.2);
}

.popover-facebook.bs-popover-top .arrow::after, .popover-facebook.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #3b5999;
}

.popover-facebook.bs-popover-right .arrow::after, .popover-facebook.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #3b5999;
}

.popover-facebook.bs-popover-bottom .arrow::after, .popover-facebook.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #3b5999;
}

.popover-facebook.bs-popover-left .arrow::after, .popover-facebook.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #3b5999;
}

.popover-dribbble {
    background-color: #ea4c89;
}

.popover-dribbble .popover-header {
    background-color: #ea4c89;
    color: #ECF0F3;
}

.popover-dribbble .popover-body {
    color: #ECF0F3;
}

.popover-dribbble .popover-header {
    border-color: rgba(236, 240, 243, 0.2);
}

.popover-dribbble.bs-popover-top .arrow::after, .popover-dribbble.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #ea4c89;
}

.popover-dribbble.bs-popover-right .arrow::after, .popover-dribbble.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #ea4c89;
}

.popover-dribbble.bs-popover-bottom .arrow::after, .popover-dribbble.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #ea4c89;
}

.popover-dribbble.bs-popover-left .arrow::after, .popover-dribbble.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #ea4c89;
}

.popover-github {
    background-color: #222222;
}

.popover-github .popover-header {
    background-color: #222222;
    color: #ECF0F3;
}

.popover-github .popover-body {
    color: #ECF0F3;
}

.popover-github .popover-header {
    border-color: rgba(236, 240, 243, 0.2);
}

.popover-github.bs-popover-top .arrow::after, .popover-github.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #222222;
}

.popover-github.bs-popover-right .arrow::after, .popover-github.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #222222;
}

.popover-github.bs-popover-bottom .arrow::after, .popover-github.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #222222;
}

.popover-github.bs-popover-left .arrow::after, .popover-github.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #222222;
}

.popover-behance {
    background-color: #0057ff;
}

.popover-behance .popover-header {
    background-color: #0057ff;
    color: #ECF0F3;
}

.popover-behance .popover-body {
    color: #ECF0F3;
}

.popover-behance .popover-header {
    border-color: rgba(236, 240, 243, 0.2);
}

.popover-behance.bs-popover-top .arrow::after, .popover-behance.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #0057ff;
}

.popover-behance.bs-popover-right .arrow::after, .popover-behance.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #0057ff;
}

.popover-behance.bs-popover-bottom .arrow::after, .popover-behance.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #0057ff;
}

.popover-behance.bs-popover-left .arrow::after, .popover-behance.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #0057ff;
}

.popover-twitter {
    background-color: #1da1f2;
}

.popover-twitter .popover-header {
    background-color: #1da1f2;
    color: #ECF0F3;
}

.popover-twitter .popover-body {
    color: #ECF0F3;
}

.popover-twitter .popover-header {
    border-color: rgba(236, 240, 243, 0.2);
}

.popover-twitter.bs-popover-top .arrow::after, .popover-twitter.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #1da1f2;
}

.popover-twitter.bs-popover-right .arrow::after, .popover-twitter.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #1da1f2;
}

.popover-twitter.bs-popover-bottom .arrow::after, .popover-twitter.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #1da1f2;
}

.popover-twitter.bs-popover-left .arrow::after, .popover-twitter.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #1da1f2;
}

.popover-slack {
    background-color: #3aaf85;
}

.popover-slack .popover-header {
    background-color: #3aaf85;
    color: #ECF0F3;
}

.popover-slack .popover-body {
    color: #ECF0F3;
}

.popover-slack .popover-header {
    border-color: rgba(236, 240, 243, 0.2);
}

.popover-slack.bs-popover-top .arrow::after, .popover-slack.bs-popover-auto[x-placement^="top"] .arrow::after {
    border-top-color: #3aaf85;
}

.popover-slack.bs-popover-right .arrow::after, .popover-slack.bs-popover-auto[x-placement^="right"] .arrow::after {
    border-right-color: #3aaf85;
}

.popover-slack.bs-popover-bottom .arrow::after, .popover-slack.bs-popover-auto[x-placement^="bottom"] .arrow::after {
    border-bottom-color: #3aaf85;
}

.popover-slack.bs-popover-left .arrow::after, .popover-slack.bs-popover-auto[x-placement^="left"] .arrow::after {
    border-left-color: #3aaf85;
}

/**
 * = Progress bars
 */
.progress-wrapper {
    position: relative;
}

.progress-bar {
    box-shadow: none;
    height: auto;
    border-radius: 0.55rem;
}

.progress {
    height: .6rem;
    border: 0.0625rem solid #D1D9E6;
    margin-bottom: 1rem;
    overflow: hidden;
    font-size: 0.75rem;
    font-weight: 600;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

.progress-xl {
    height: 0.9rem;
}

.progress-lg {
    height: 0.7rem;
}

.progress-info {
    display: flex;
    -moz-align-items: center;
    -ms-align-items: center;
    align-items: center;
    -moz-justify-content: space-between;
    -ms-justify-content: space-between;
    justify-content: space-between;
    -ms-flex-pack: space-between;
    margin-bottom: .5rem;
}

.progress-info .progress-label span {
    display: inline-block;
    font-size: 0.875rem;
    font-weight: 600;
}

.progress-info .progress-percentage {
    text-align: right;
}

.progress-info .progress-percentage span {
    display: inline-block;
    font-size: 0.75rem;
    font-weight: 600;
}

.info-xl .progress-label span,
.info-xl .progress-percentage span {
    font-size: 0.875rem;
}

.info-xl .progress-percentage {
    text-align: right;
}

.progress-tooltip {
    background: #e6e7ee;
    font-weight: 600;
    padding: .25rem .375rem;
    line-height: 1;
    font-size: 0.75rem;
    position: relative;
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

@keyframes animate-positive {
    0% {
        width: 0%;
    }
}

/**
 * = Profile cards
 */
.card-image .dropdown {
    position: absolute;
    right: 1rem;
    top: 1rem;
}

.profile-cover {
    background-repeat: no-repeat;
    background-position: top center;
    background-size: cover;
    height: 175px;
}

.profile-image {
    width: 10rem;
    height: 10rem;
}

.profile-image-small {
    width: 8rem;
    height: 8rem;
}

/**
 * = Shapes
 */
.pattern {
    overflow: hidden;
    z-index: 1;
    position: absolute;
    left: 0;
    width: 100%;
    line-height: 0;
    direction: ltr;
}

.pattern.bottom {
    bottom: -10px;
    transform: rotate(180deg);
}

.pattern.top {
    top: -10px;
}

.pattern svg {
    display: block;
    width: calc(100% + 1.3px);
    position: relative;
    left: 50%;
    transform: translateX(-50%);
}

.organic-radius {
    border-radius: 63% 37% 30% 70% / 50% 45% 55% 50%;
}

.avatar-sm {
    width: 1.5rem;
    height: 1.5rem;
}

.avatar-md {
    width: 2rem;
    height: 2rem;
}

.avatar-lg {
    width: 3rem;
    height: 3rem;
}

.color-shape {
    width: 7rem;
    height: 7rem;
}

/**
 * = Typography
 */
h1, h2, h3, h4, h5, h6,
.h1, .h2, .h3, .h4, .h5, .h6 {
    font-family: "Nunito Sans", sans-serif;
    font-weight: 400;
}

p, ol li, ul li {
    font-family: "Nunito Sans", sans-serif;
    font-size: 1rem;
    font-weight: 300;
    line-height: 1.6;
}

a, .text-action {
    color: #31344b;
    font-weight: 400;
    transition: all 0.2s ease;
}

a:hover, .text-action:hover {
    color: #262833;
    cursor: pointer;
}

article h1, article h2, article h3, article h4, article h5, article h6 {
    margin: 2.5rem 0 2rem 0;
}

article p, article blockquote {
    font-size: 1.27rem;
    margin-bottom: 2rem;
}

article ul li, article ol li {
    font-size: 1.27rem;
    margin-bottom: 1.5rem;
}

article ul, article ol {
    margin-bottom: 2.5rem;
}

article a {
    color: #2D4CC8;
    text-decoration: underline;
}

article a:hover {
    color: #2D4CC8;
    text-decoration: none;
}

.lead + .btn-wrapper {
    margin-top: 3rem;
}

@media (max-width: 991.98px) {
    .lead {
        font-size: 1rem;
    }
}

.text-italic {
    font-style: italic !important;
}

.description {
    font-size: 0.875rem;
}

.heading {
    letter-spacing: 0.025em;
    font-size: 2rem;
    text-transform: uppercase;
    font-weight: 600;
}

.heading-title {
    letter-spacing: 0.025em;
    font-size: 1.375rem;
    font-weight: 600;
    text-transform: uppercase;
}

.heading-section {
    letter-spacing: 0.025em;
    font-size: 1.375rem;
    font-weight: 600;
    text-transform: uppercase;
}

.heading-section img {
    display: block;
    width: 72px;
    height: 72px;
    margin-bottom: 1.5rem;
}

.heading-section.text-center img {
    margin-left: auto;
    margin-right: auto;
}

.display-1,
.display-2,
.display-3,
.display-4 {
    font-weight: 400;
}

.display-1 span,
  .display-2 span,
  .display-3 span,
  .display-4 span {
    font-weight: 300;
}

@media (max-width: 991.98px) {
    .display-2 {
        font-size: 1.875rem;
    }
}

@media (max-width: 1199.98px) {
    .display-3 {
        font-size: 1.875rem;
    }
}

@media (max-width: 767.98px) {
    .display-4 {
        font-size: 1.5rem;
    }
}

.blockquote {
    font-style: italic;
    font-weight: 400;
}

.blockquote .blockquote-footer {
    font-size: 0.875rem;
    font-weight: 700;
}

.font-small {
    font-size: 0.875rem;
}

.font-base {
    font-size: 1rem;
    font-weight: 300;
}

.font-medium {
    font-size: 1.25rem;
    font-weight: 300;
}

.folder-structure li {
    font-size: 1.2rem;
}

.text-primary, .text-primary:hover {
    color: #e6e7ee !important;
}

.text-primary a:not(.btn), .text-primary h1, .text-primary h2, .text-primary h3, .text-primary h4, .text-primary h5, .text-primary h6, .text-primary .h1, .text-primary .h2, .text-primary .h3, .text-primary .h4, .text-primary .h5, .text-primary .h6, .text-primary .display-1, .text-primary .display-2, .text-primary .display-3, .text-primary .display-4 {
    color: #e6e7ee;
}

.text-primary .text-muted {
    color: rgba(230, 231, 238, 0.7) !important;
}

.text-secondary, .text-secondary:hover {
    color: #2D4CC8 !important;
}

.text-secondary a:not(.btn), .text-secondary h1, .text-secondary h2, .text-secondary h3, .text-secondary h4, .text-secondary h5, .text-secondary h6, .text-secondary .h1, .text-secondary .h2, .text-secondary .h3, .text-secondary .h4, .text-secondary .h5, .text-secondary .h6, .text-secondary .display-1, .text-secondary .display-2, .text-secondary .display-3, .text-secondary .display-4 {
    color: #2D4CC8;
}

.text-secondary .text-muted {
    color: rgba(45, 76, 200, 0.7) !important;
}

.text-success, .text-success:hover {
    color: #18634B !important;
}

.text-success a:not(.btn), .text-success h1, .text-success h2, .text-success h3, .text-success h4, .text-success h5, .text-success h6, .text-success .h1, .text-success .h2, .text-success .h3, .text-success .h4, .text-success .h5, .text-success .h6, .text-success .display-1, .text-success .display-2, .text-success .display-3, .text-success .display-4 {
    color: #18634B;
}

.text-success .text-muted {
    color: rgba(24, 99, 75, 0.7) !important;
}

.text-info, .text-info:hover {
    color: #0056B3 !important;
}

.text-info a:not(.btn), .text-info h1, .text-info h2, .text-info h3, .text-info h4, .text-info h5, .text-info h6, .text-info .h1, .text-info .h2, .text-info .h3, .text-info .h4, .text-info .h5, .text-info .h6, .text-info .display-1, .text-info .display-2, .text-info .display-3, .text-info .display-4 {
    color: #0056B3;
}

.text-info .text-muted {
    color: rgba(0, 86, 179, 0.7) !important;
}

.text-warning, .text-warning:hover {
    color: #F0B400 !important;
}

.text-warning a:not(.btn), .text-warning h1, .text-warning h2, .text-warning h3, .text-warning h4, .text-warning h5, .text-warning h6, .text-warning .h1, .text-warning .h2, .text-warning .h3, .text-warning .h4, .text-warning .h5, .text-warning .h6, .text-warning .display-1, .text-warning .display-2, .text-warning .display-3, .text-warning .display-4 {
    color: #F0B400;
}

.text-warning .text-muted {
    color: rgba(240, 180, 0, 0.7) !important;
}

.text-danger, .text-danger:hover {
    color: #A91E2C !important;
}

.text-danger a:not(.btn), .text-danger h1, .text-danger h2, .text-danger h3, .text-danger h4, .text-danger h5, .text-danger h6, .text-danger .h1, .text-danger .h2, .text-danger .h3, .text-danger .h4, .text-danger .h5, .text-danger .h6, .text-danger .display-1, .text-danger .display-2, .text-danger .display-3, .text-danger .display-4 {
    color: #A91E2C;
}

.text-danger .text-muted {
    color: rgba(169, 30, 44, 0.7) !important;
}

.text-light, .text-light:hover {
    color: #D1D9E6 !important;
}

.text-light a:not(.btn), .text-light h1, .text-light h2, .text-light h3, .text-light h4, .text-light h5, .text-light h6, .text-light .h1, .text-light .h2, .text-light .h3, .text-light .h4, .text-light .h5, .text-light .h6, .text-light .display-1, .text-light .display-2, .text-light .display-3, .text-light .display-4 {
    color: #D1D9E6;
}

.text-light .text-muted {
    color: rgba(209, 217, 230, 0.7) !important;
}

.text-dark, .text-dark:hover {
    color: #31344b !important;
}

.text-dark a:not(.btn), .text-dark h1, .text-dark h2, .text-dark h3, .text-dark h4, .text-dark h5, .text-dark h6, .text-dark .h1, .text-dark .h2, .text-dark .h3, .text-dark .h4, .text-dark .h5, .text-dark .h6, .text-dark .display-1, .text-dark .display-2, .text-dark .display-3, .text-dark .display-4 {
    color: #31344b;
}

.text-dark .text-muted {
    color: rgba(49, 52, 75, 0.7) !important;
}

.text-default, .text-default:hover {
    color: #262833 !important;
}

.text-default a:not(.btn), .text-default h1, .text-default h2, .text-default h3, .text-default h4, .text-default h5, .text-default h6, .text-default .h1, .text-default .h2, .text-default .h3, .text-default .h4, .text-default .h5, .text-default .h6, .text-default .display-1, .text-default .display-2, .text-default .display-3, .text-default .display-4 {
    color: #262833;
}

.text-default .text-muted {
    color: rgba(38, 40, 51, 0.7) !important;
}

.text-white, .text-white:hover {
    color: #ECF0F3 !important;
}

.text-white a:not(.btn), .text-white h1, .text-white h2, .text-white h3, .text-white h4, .text-white h5, .text-white h6, .text-white .h1, .text-white .h2, .text-white .h3, .text-white .h4, .text-white .h5, .text-white .h6, .text-white .display-1, .text-white .display-2, .text-white .display-3, .text-white .display-4 {
    color: #ECF0F3;
}

.text-white .text-muted {
    color: rgba(236, 240, 243, 0.7) !important;
}

.text-gray, .text-gray:hover {
    color: #44476A !important;
}

.text-gray a:not(.btn), .text-gray h1, .text-gray h2, .text-gray h3, .text-gray h4, .text-gray h5, .text-gray h6, .text-gray .h1, .text-gray .h2, .text-gray .h3, .text-gray .h4, .text-gray .h5, .text-gray .h6, .text-gray .display-1, .text-gray .display-2, .text-gray .display-3, .text-gray .display-4 {
    color: #44476A;
}

.text-gray .text-muted {
    color: rgba(68, 71, 106, 0.7) !important;
}

.text-neutral, .text-neutral:hover {
    color: #ECF0F3 !important;
}

.text-neutral a:not(.btn), .text-neutral h1, .text-neutral h2, .text-neutral h3, .text-neutral h4, .text-neutral h5, .text-neutral h6, .text-neutral .h1, .text-neutral .h2, .text-neutral .h3, .text-neutral .h4, .text-neutral .h5, .text-neutral .h6, .text-neutral .display-1, .text-neutral .display-2, .text-neutral .display-3, .text-neutral .display-4 {
    color: #ECF0F3;
}

.text-neutral .text-muted {
    color: rgba(236, 240, 243, 0.7) !important;
}

.text-soft, .text-soft:hover {
    color: #e6e7ee !important;
}

.text-soft a:not(.btn), .text-soft h1, .text-soft h2, .text-soft h3, .text-soft h4, .text-soft h5, .text-soft h6, .text-soft .h1, .text-soft .h2, .text-soft .h3, .text-soft .h4, .text-soft .h5, .text-soft .h6, .text-soft .display-1, .text-soft .display-2, .text-soft .display-3, .text-soft .display-4 {
    color: #e6e7ee;
}

.text-soft .text-muted {
    color: rgba(230, 231, 238, 0.7) !important;
}

.text-black, .text-black:hover {
    color: #262833 !important;
}

.text-black a:not(.btn), .text-black h1, .text-black h2, .text-black h3, .text-black h4, .text-black h5, .text-black h6, .text-black .h1, .text-black .h2, .text-black .h3, .text-black .h4, .text-black .h5, .text-black .h6, .text-black .display-1, .text-black .display-2, .text-black .display-3, .text-black .display-4 {
    color: #262833;
}

.text-black .text-muted {
    color: rgba(38, 40, 51, 0.7) !important;
}

.text-purple, .text-purple:hover {
    color: #6f42c1 !important;
}

.text-purple a:not(.btn), .text-purple h1, .text-purple h2, .text-purple h3, .text-purple h4, .text-purple h5, .text-purple h6, .text-purple .h1, .text-purple .h2, .text-purple .h3, .text-purple .h4, .text-purple .h5, .text-purple .h6, .text-purple .display-1, .text-purple .display-2, .text-purple .display-3, .text-purple .display-4 {
    color: #6f42c1;
}

.text-purple .text-muted {
    color: rgba(111, 66, 193, 0.7) !important;
}

.text-gray-100, .text-gray-100:hover {
    color: #f3f7fa !important;
}

.text-gray-100 a:not(.btn), .text-gray-100 h1, .text-gray-100 h2, .text-gray-100 h3, .text-gray-100 h4, .text-gray-100 h5, .text-gray-100 h6, .text-gray-100 .h1, .text-gray-100 .h2, .text-gray-100 .h3, .text-gray-100 .h4, .text-gray-100 .h5, .text-gray-100 .h6, .text-gray-100 .display-1, .text-gray-100 .display-2, .text-gray-100 .display-3, .text-gray-100 .display-4 {
    color: #f3f7fa;
}

.text-gray-100 .text-muted {
    color: rgba(243, 247, 250, 0.7) !important;
}

.text-gray-200, .text-gray-200:hover {
    color: #fafbfe !important;
}

.text-gray-200 a:not(.btn), .text-gray-200 h1, .text-gray-200 h2, .text-gray-200 h3, .text-gray-200 h4, .text-gray-200 h5, .text-gray-200 h6, .text-gray-200 .h1, .text-gray-200 .h2, .text-gray-200 .h3, .text-gray-200 .h4, .text-gray-200 .h5, .text-gray-200 .h6, .text-gray-200 .display-1, .text-gray-200 .display-2, .text-gray-200 .display-3, .text-gray-200 .display-4 {
    color: #fafbfe;
}

.text-gray-200 .text-muted {
    color: rgba(250, 251, 254, 0.7) !important;
}

.text-gray-300, .text-gray-300:hover {
    color: #e6e7ee !important;
}

.text-gray-300 a:not(.btn), .text-gray-300 h1, .text-gray-300 h2, .text-gray-300 h3, .text-gray-300 h4, .text-gray-300 h5, .text-gray-300 h6, .text-gray-300 .h1, .text-gray-300 .h2, .text-gray-300 .h3, .text-gray-300 .h4, .text-gray-300 .h5, .text-gray-300 .h6, .text-gray-300 .display-1, .text-gray-300 .display-2, .text-gray-300 .display-3, .text-gray-300 .display-4 {
    color: #e6e7ee;
}

.text-gray-300 .text-muted {
    color: rgba(230, 231, 238, 0.7) !important;
}

.text-gray-400, .text-gray-400:hover {
    color: #D1D9E6 !important;
}

.text-gray-400 a:not(.btn), .text-gray-400 h1, .text-gray-400 h2, .text-gray-400 h3, .text-gray-400 h4, .text-gray-400 h5, .text-gray-400 h6, .text-gray-400 .h1, .text-gray-400 .h2, .text-gray-400 .h3, .text-gray-400 .h4, .text-gray-400 .h5, .text-gray-400 .h6, .text-gray-400 .display-1, .text-gray-400 .display-2, .text-gray-400 .display-3, .text-gray-400 .display-4 {
    color: #D1D9E6;
}

.text-gray-400 .text-muted {
    color: rgba(209, 217, 230, 0.7) !important;
}

.text-gray-500, .text-gray-500:hover {
    color: #b1bcce !important;
}

.text-gray-500 a:not(.btn), .text-gray-500 h1, .text-gray-500 h2, .text-gray-500 h3, .text-gray-500 h4, .text-gray-500 h5, .text-gray-500 h6, .text-gray-500 .h1, .text-gray-500 .h2, .text-gray-500 .h3, .text-gray-500 .h4, .text-gray-500 .h5, .text-gray-500 .h6, .text-gray-500 .display-1, .text-gray-500 .display-2, .text-gray-500 .display-3, .text-gray-500 .display-4 {
    color: #b1bcce;
}

.text-gray-500 .text-muted {
    color: rgba(177, 188, 206, 0.7) !important;
}

.text-gray-600, .text-gray-600:hover {
    color: #93a5be !important;
}

.text-gray-600 a:not(.btn), .text-gray-600 h1, .text-gray-600 h2, .text-gray-600 h3, .text-gray-600 h4, .text-gray-600 h5, .text-gray-600 h6, .text-gray-600 .h1, .text-gray-600 .h2, .text-gray-600 .h3, .text-gray-600 .h4, .text-gray-600 .h5, .text-gray-600 .h6, .text-gray-600 .display-1, .text-gray-600 .display-2, .text-gray-600 .display-3, .text-gray-600 .display-4 {
    color: #93a5be;
}

.text-gray-600 .text-muted {
    color: rgba(147, 165, 190, 0.7) !important;
}

.text-gray-700, .text-gray-700:hover {
    color: #66799e !important;
}

.text-gray-700 a:not(.btn), .text-gray-700 h1, .text-gray-700 h2, .text-gray-700 h3, .text-gray-700 h4, .text-gray-700 h5, .text-gray-700 h6, .text-gray-700 .h1, .text-gray-700 .h2, .text-gray-700 .h3, .text-gray-700 .h4, .text-gray-700 .h5, .text-gray-700 .h6, .text-gray-700 .display-1, .text-gray-700 .display-2, .text-gray-700 .display-3, .text-gray-700 .display-4 {
    color: #66799e;
}

.text-gray-700 .text-muted {
    color: rgba(102, 121, 158, 0.7) !important;
}

.text-gray-800, .text-gray-800:hover {
    color: #525480 !important;
}

.text-gray-800 a:not(.btn), .text-gray-800 h1, .text-gray-800 h2, .text-gray-800 h3, .text-gray-800 h4, .text-gray-800 h5, .text-gray-800 h6, .text-gray-800 .h1, .text-gray-800 .h2, .text-gray-800 .h3, .text-gray-800 .h4, .text-gray-800 .h5, .text-gray-800 .h6, .text-gray-800 .display-1, .text-gray-800 .display-2, .text-gray-800 .display-3, .text-gray-800 .display-4 {
    color: #525480;
}

.text-gray-800 .text-muted {
    color: rgba(82, 84, 128, 0.7) !important;
}

.text-facebook, .text-facebook:hover {
    color: #3b5999 !important;
}

.text-facebook a:not(.btn), .text-facebook h1, .text-facebook h2, .text-facebook h3, .text-facebook h4, .text-facebook h5, .text-facebook h6, .text-facebook .h1, .text-facebook .h2, .text-facebook .h3, .text-facebook .h4, .text-facebook .h5, .text-facebook .h6, .text-facebook .display-1, .text-facebook .display-2, .text-facebook .display-3, .text-facebook .display-4 {
    color: #3b5999;
}

.text-facebook .text-muted {
    color: rgba(59, 89, 153, 0.7) !important;
}

.text-dribbble, .text-dribbble:hover {
    color: #ea4c89 !important;
}

.text-dribbble a:not(.btn), .text-dribbble h1, .text-dribbble h2, .text-dribbble h3, .text-dribbble h4, .text-dribbble h5, .text-dribbble h6, .text-dribbble .h1, .text-dribbble .h2, .text-dribbble .h3, .text-dribbble .h4, .text-dribbble .h5, .text-dribbble .h6, .text-dribbble .display-1, .text-dribbble .display-2, .text-dribbble .display-3, .text-dribbble .display-4 {
    color: #ea4c89;
}

.text-dribbble .text-muted {
    color: rgba(234, 76, 137, 0.7) !important;
}

.text-github, .text-github:hover {
    color: #222222 !important;
}

.text-github a:not(.btn), .text-github h1, .text-github h2, .text-github h3, .text-github h4, .text-github h5, .text-github h6, .text-github .h1, .text-github .h2, .text-github .h3, .text-github .h4, .text-github .h5, .text-github .h6, .text-github .display-1, .text-github .display-2, .text-github .display-3, .text-github .display-4 {
    color: #222222;
}

.text-github .text-muted {
    color: rgba(34, 34, 34, 0.7) !important;
}

.text-behance, .text-behance:hover {
    color: #0057ff !important;
}

.text-behance a:not(.btn), .text-behance h1, .text-behance h2, .text-behance h3, .text-behance h4, .text-behance h5, .text-behance h6, .text-behance .h1, .text-behance .h2, .text-behance .h3, .text-behance .h4, .text-behance .h5, .text-behance .h6, .text-behance .display-1, .text-behance .display-2, .text-behance .display-3, .text-behance .display-4 {
    color: #0057ff;
}

.text-behance .text-muted {
    color: rgba(0, 87, 255, 0.7) !important;
}

.text-twitter, .text-twitter:hover {
    color: #1da1f2 !important;
}

.text-twitter a:not(.btn), .text-twitter h1, .text-twitter h2, .text-twitter h3, .text-twitter h4, .text-twitter h5, .text-twitter h6, .text-twitter .h1, .text-twitter .h2, .text-twitter .h3, .text-twitter .h4, .text-twitter .h5, .text-twitter .h6, .text-twitter .display-1, .text-twitter .display-2, .text-twitter .display-3, .text-twitter .display-4 {
    color: #1da1f2;
}

.text-twitter .text-muted {
    color: rgba(29, 161, 242, 0.7) !important;
}

.text-slack, .text-slack:hover {
    color: #3aaf85 !important;
}

.text-slack a:not(.btn), .text-slack h1, .text-slack h2, .text-slack h3, .text-slack h4, .text-slack h5, .text-slack h6, .text-slack .h1, .text-slack .h2, .text-slack .h3, .text-slack .h4, .text-slack .h5, .text-slack .h6, .text-slack .display-1, .text-slack .display-2, .text-slack .display-3, .text-slack .display-4 {
    color: #3aaf85;
}

.text-slack .text-muted {
    color: rgba(58, 175, 133, 0.7) !important;
}

.tooltip-inner {
    box-shadow: inset 2px 2px 5px #b8b9be, inset -3px -3px 7px #FFFFFF;
}

/*# sourceMappingURL=neumorphism.css.map */