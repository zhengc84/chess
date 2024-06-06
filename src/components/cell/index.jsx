import React, { useContext } from "react";
import { isLightSquare, Cell as BoardCell } from '../../functions/';
import PropTypes from 'prop-types';
import { GameContext } from '../../context/GameContext';
import Piece from '../piece';
import './cell-styles.css';

const Cell = ({ cell, index, makeMove, setFromPos }) => {
    const light = isLightSquare(cell.pos, index);

    const { possibleMoves, turn, check } = useContext(GameContext);
    const isPossibleMove = possibleMoves.includes(cell.pos);

    const color = cell.piece.toUpperCase() === cell.piece ? 'w' : 'b';

    const inCheck = () => {
        const king = cell.piece.toUpperCase() === 'K';
        return turn === color && king && check;
    }

    const handleDrop = () => {
        makeMove(cell.pos);
    };

    return (
        <div className={`cell ${light ? 'light' : 'dark'}`}
        onDrop={handleDrop}
        onDragOver={(e) => e.preventDefault()}
        >
            <div className={`overlay ${isPossibleMove && 'possible-move'} ${
                    inCheck() && 'check'
                }`}>
                <Piece pos={cell.pos} name={cell.piece} setFromPos={setFromPos} />
            </div>
        </div>
    );
};

Cell.prototype = {
    cell: PropTypes.instanceOf(BoardCell).isRequired,
    index: PropTypes.number.isRequired,
    makeMove: PropTypes.func,
    setFromPos: PropTypes.func,
};

export default Cell;