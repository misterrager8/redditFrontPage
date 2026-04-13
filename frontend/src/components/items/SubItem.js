import Button from "../atoms/Button";
import { Context } from "../../context";
import { useContext } from "react";

export default function SubItem({ item }) {
  const ctx = useContext(Context);

  return (
    <div
      className={"sub-item" + (ctx.selectedSub === item ? " active" : "")}
      onClick={() =>
        ctx.setSelectedSub(item === ctx.selectedSub ? null : item)
      }>
      {item}
    </div>
  );
}
