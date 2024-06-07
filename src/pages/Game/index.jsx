import React, { useState, useRef, useEffect, useContext } from 'react';
import { Chess } from 'chess.js';
import { GameContext } from '../../context/GameContext';
import { createBoard } from '../../functions';
import Board from '../../components/board';
import { types } from '../../context/actions';
import GameOver from '../../components/gameover';
import getGameOverState from '../../functions/game-over.js';

//const FEN = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1';
//const FEN = 'rnb1kbnr/pppp1ppp/8/4p3/5PPq/8/PPPPP2P/RNBQKBNR w KQkq - 1 3';
const FEN = '4k3/4P3/4K3/8/8/8/8/8 b - - 0 78';
const Game = () => {
    const [fen, setFen] = useState(FEN);
    const { current: chess } = useRef(new Chess(fen));
    const [board, setBoard] = useState(createBoard(fen));
    const { dispatch, gameOver } = useContext(GameContext);

    useEffect(() => {
        setBoard(createBoard(fen));
    }, [fen]);

    useEffect(() => {
        const [gameOver, status] = getGameOverState(chess);
        if (gameOver) {
            dispatch({ type: types.GAME_OVER, status, player: chess.turn() });
            return;
        }
        dispatch({
            type: types.SET_TURN,
            player: chess.turn(),
            check: chess.inCheck(),
        });
    }, [fen, dispatch, chess]);

    const fromPos = useRef();
    
    const makeMove = (pos) => {
        const from = fromPos.current; 
        chess.move({ from, to: pos });
        dispatch({ tpe: types.CLEAR_POSSIBLE_MOVES })
        setFen(chess.fen());
    };

    const setFromPos = (pos) => {
        fromPos.current = pos;
        dispatch({
            type: types.SET_POSSIBLE_MOVES,
            moves: chess.moves({ square: pos }),
        });
    };

    if (gameOver) {
        return <GameOver />;
    }

    return (
        <div className="game">
            <Board cells={board} makeMove={makeMove} setFromPos={setFromPos} />
        </div>
    );
};

export default Game;