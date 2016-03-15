% Copyright 2014
%
%    Licensed under the Apache License, Version 2.0 (the "License");
%    you may not use this file except in compliance with the License.
%    You may obtain a copy of the License at
%
%        http://www.apache.org/licenses/LICENSE-2.0
%
%    Unless required by applicable law or agreed to in writing, software
%    distributed under the License is distributed on an "AS IS" BASIS,
%    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
%    See the License for the specific language governing permissions and
%    limitations under the License.

function drawlineFromPoints(FemmProblem,i,j,c)
if nargin<4
    c='b';
else
    switch c
        case 'b'
            c=[0 0 1];
        case 'g'
            c=[0 1 0];
        case 'r'
            c=[1 0 0];
        otherwise
            c=[0 0 0 ];
    end
end
a=FemmProblem.Nodes(i+1).Coords;
b=FemmProblem.Nodes(j+1).Coords;
H=line(a,b);
set(H,'color',c)